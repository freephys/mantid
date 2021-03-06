from __future__ import (absolute_import, division, print_function)
import unittest
from mantid.kernel import (V3D, Quat)
from mantid.api import AnalysisDataService
from sans.common.general_functions import (quaternion_to_angle_and_axis, create_unmanaged_algorithm, add_to_sample_log,
                                           get_standard_output_workspace_name, sanitise_instrument_name,
                                           get_reduced_can_workspace_from_ads, write_hash_into_reduced_can_workspace,
                                           convert_instrument_and_detector_type_to_bank_name,
                                           convert_bank_name_to_detector_type_isis,
                                           get_facility)
from sans.common.constants import (SANS2D, LOQ, LARMOR)
from sans.common.enums import (ISISReductionMode, ReductionDimensionality, OutputParts,
                               SANSInstrument, DetectorType, SANSFacility)
from sans.test_helper.test_director import TestDirector
from sans.state.data import StateData


class SANSFunctionsTest(unittest.TestCase):
    @staticmethod
    def _prepare_workspaces(number_of_workspaces, tagged_workspace_names=None, state=None, reduction_mode=None):
        create_name = "CreateSampleWorkspace"
        create_options = {"OutputWorkspace": "test",
                          "NumBanks": 1,
                          "BankPixelWidth": 2,
                          "XMin": 1,
                          "XMax": 10,
                          "BinWidth": 2}
        create_alg = create_unmanaged_algorithm(create_name, **create_options)

        for index in range(number_of_workspaces):
            create_alg.execute()
            workspace = create_alg.getProperty("OutputWorkspace").value
            workspace_name = "test" + "_" + str(index)
            AnalysisDataService.addOrReplace(workspace_name, workspace)

        if tagged_workspace_names is not None:
            for key, value in list(tagged_workspace_names.items()):
                create_alg.execute()
                workspace = create_alg.getProperty("OutputWorkspace").value
                AnalysisDataService.addOrReplace(value, workspace)
                write_hash_into_reduced_can_workspace(state, workspace, reduction_mode, key)

    @staticmethod
    def _create_sample_workspace():
        sample_name = "CreateSampleWorkspace"
        sample_options = {"OutputWorkspace": "dummy"}
        sample_alg = create_unmanaged_algorithm(sample_name, **sample_options)
        sample_alg.execute()
        return sample_alg.getProperty("OutputWorkspace").value

    def _do_test_quaternion(self, angle, axis, expected_axis=None):
        # Act
        quaternion = Quat(angle, axis)
        converted_angle, converted_axis = quaternion_to_angle_and_axis(quaternion)

        # Assert
        if expected_axis is not None:
            axis = expected_axis
        self.assertAlmostEqual(angle, converted_angle)
        self.assertAlmostEqual(axis[0], converted_axis[0])
        self.assertAlmostEqual(axis[1], converted_axis[1])
        self.assertAlmostEqual(axis[2], converted_axis[2])

    @staticmethod
    def _get_state():
        test_director = TestDirector()
        state = test_director.construct()

        state.data.sample_scatter_run_number = 12345
        state.data.sample_scatter_period = StateData.ALL_PERIODS

        state.reduction.dimensionality = ReductionDimensionality.OneDim

        state.wavelength.wavelength_low = 12.0
        state.wavelength.wavelength_high = 34.0

        state.mask.phi_min = 12.0
        state.mask.phi_max = 56.0

        state.slice.start_time = [4.56778]
        state.slice.end_time = [12.373938]
        return state

    def test_that_quaternion_can_be_converted_to_axis_and_angle_for_regular(self):
        # Arrange
        angle = 23.0
        axis = V3D(0.0, 1.0, 0.0)
        self._do_test_quaternion(angle, axis)

    def test_that_quaternion_can_be_converted_to_axis_and_angle_for_0_degree(self):
        # Arrange
        angle = 0.0
        axis = V3D(1.0, 0.0, 0.0)
        # There shouldn't be an axis for angle 0
        expected_axis = V3D(0.0, 0.0, 0.0)
        self._do_test_quaternion(angle, axis, expected_axis)

    def test_that_quaternion_can_be_converted_to_axis_and_angle_for_180_degree(self):
        # Arrange
        angle = 180.0
        axis = V3D(0.0, 1.0, 0.0)
        # There shouldn't be an axis for angle 0
        self._do_test_quaternion(angle, axis)

    def test_that_sample_log_is_added(self):
        # Arrange
        workspace = SANSFunctionsTest._create_sample_workspace()
        log_name = "TestName"
        log_value = "TestValue"
        log_type = "String"

        # Act
        add_to_sample_log(workspace, log_name, log_value, log_type)

        # Assert
        run = workspace.run()
        self.assertTrue(run.hasProperty(log_name))
        self.assertTrue(run.getProperty(log_name).value == log_value)

    def test_that_sample_log_raises_for_non_string_type_arguments(self):
        # Arrange
        workspace = SANSFunctionsTest._create_sample_workspace()
        log_name = "TestName"
        log_value = 123
        log_type = "String"

        # Act + Assert
        try:
            add_to_sample_log(workspace, log_name, log_value, log_type)
            did_raise = False
        except TypeError:
            did_raise = True
        self.assertTrue(did_raise)

    def test_that_sample_log_raises_for_wrong_type_selection(self):
        # Arrange
        workspace = SANSFunctionsTest._create_sample_workspace()
        log_name = "TestName"
        log_value = "test"
        log_type = "sdfsdfsdf"

        # Act + Assert
        try:
            add_to_sample_log(workspace, log_name, log_value, log_type)
            did_raise = False
        except ValueError:
            did_raise = True
        self.assertTrue(did_raise)

    def test_that_unknown_reduction_mode_raises(self):
        # Arrange
        state = SANSFunctionsTest._get_state()

        # Act + Assert
        try:
            get_standard_output_workspace_name(state, ISISReductionMode.All)
            did_raise = False
        except RuntimeError:
            did_raise = True
        self.assertTrue(did_raise)

    def test_that_creates_correct_workspace_name_for_1D(self):
        # Arrange
        state = SANSFunctionsTest._get_state()
        # Act
        output_workspace, _ = get_standard_output_workspace_name(state, ISISReductionMode.LAB)
        # Assert
        self.assertTrue("12345rear_1D_12.0_34.0Phi12.0_56.0_t4.57_T12.37" == output_workspace)

    def test_that_creates_correct_transmission_workspace_name(self):
        # Arrange
        state = SANSFunctionsTest._get_state()
        # Act
        output_workspace, _ = get_standard_output_workspace_name(state, ISISReductionMode.LAB, data_type = 'Sample', transmission = True)
        # Assert
        self.assertTrue("12345_trans_Sample_12.0_34.0Phi12.0_56.0_t4.57_T12.37" == output_workspace)

    def test_that_sanitises_instrument_names(self):
        name1 = sanitise_instrument_name("LOQ_trans")
        self.assertTrue(LOQ == name1)

        name2 = sanitise_instrument_name("sans2d")
        self.assertTrue(SANS2D == name2)

        name3 = sanitise_instrument_name("__LArMOR_")
        self.assertTrue(LARMOR == name3)

        name4 = sanitise_instrument_name("OThER")
        self.assertTrue("OThER" == name4)

    def test_that_can_find_can_reduction_if_it_exists(self):
        # Arrange
        test_director = TestDirector()
        state = test_director.construct()
        tagged_workspace_names = {None: "test_ws",
                                  OutputParts.Count: "test_ws_count",
                                  OutputParts.Norm: "test_ws_norm"}
        SANSFunctionsTest._prepare_workspaces(number_of_workspaces=4,
                                              tagged_workspace_names=tagged_workspace_names,
                                              state=state,
                                              reduction_mode=ISISReductionMode.LAB)
        # Act
        workspace, workspace_count, workspace_norm = get_reduced_can_workspace_from_ads(state, output_parts=True,
                                                                              reduction_mode=ISISReductionMode.LAB)  # noqa

        # Assert
        self.assertTrue(workspace is not None)
        self.assertTrue(workspace.name() == AnalysisDataService.retrieve("test_ws").name())
        self.assertTrue(workspace_count is not None)
        self.assertTrue(workspace_count.name() == AnalysisDataService.retrieve("test_ws_count").name())
        self.assertTrue(workspace_norm is not None)
        self.assertTrue(workspace_norm.name() == AnalysisDataService.retrieve("test_ws_norm").name())

        # Clean up
        SANSFunctionsTest._remove_workspaces()

    @staticmethod
    def _remove_workspaces():
        for element in AnalysisDataService.getObjectNames():
            AnalysisDataService.remove(element)

    def test_that_returns_none_if_it_does_not_exist(self):
        # Arrange
        test_director = TestDirector()
        state = test_director.construct()
        SANSFunctionsTest._prepare_workspaces(number_of_workspaces=4, tagged_workspace_names=None,
                                              state=state, reduction_mode=ISISReductionMode.LAB)

        # Act
        workspace, workspace_count, workspace_norm = \
            get_reduced_can_workspace_from_ads(state, output_parts=False, reduction_mode=ISISReductionMode.LAB)

        # Assert
        self.assertTrue(workspace is None)
        self.assertTrue(workspace_count is None)
        self.assertTrue(workspace_norm is None)

        # Clean up
        SANSFunctionsTest._remove_workspaces()

    def test_that_convert_instrument_and_detector_type_to_bank_name_produces_expected_results(self):
        self.assertTrue("front-detector" == convert_instrument_and_detector_type_to_bank_name(SANSInstrument.SANS2D,
                                                                                              DetectorType.HAB))
        self.assertTrue("rear-detector" == convert_instrument_and_detector_type_to_bank_name(SANSInstrument.SANS2D,
                                                                                             DetectorType.LAB))
        self.assertTrue("HAB" == convert_instrument_and_detector_type_to_bank_name(SANSInstrument.LOQ,
                                                                                   DetectorType.HAB))
        self.assertTrue("main-detector-bank" == convert_instrument_and_detector_type_to_bank_name(SANSInstrument.LOQ,
                                                                                                  DetectorType.LAB))
        self.assertTrue("DetectorBench" == convert_instrument_and_detector_type_to_bank_name(SANSInstrument.LARMOR,
                                                                                             DetectorType.LAB))
        self.assertTrue("rear-detector" == convert_instrument_and_detector_type_to_bank_name(SANSInstrument.ZOOM,
                                                                                             DetectorType.LAB))

    def test_that_converts_detector_name_to_type(self):
        self.assertTrue(convert_bank_name_to_detector_type_isis("rEar-detector") is DetectorType.LAB)
        self.assertTrue(convert_bank_name_to_detector_type_isis("MAIN-detector-BANK") is DetectorType.LAB)
        self.assertTrue(convert_bank_name_to_detector_type_isis("DeTectorBench") is DetectorType.LAB)
        self.assertTrue(convert_bank_name_to_detector_type_isis("rear") is DetectorType.LAB)
        self.assertTrue(convert_bank_name_to_detector_type_isis("MAIN") is DetectorType.LAB)
        self.assertTrue(convert_bank_name_to_detector_type_isis("FRoNT-DETECTOR") is DetectorType.HAB)
        self.assertTrue(convert_bank_name_to_detector_type_isis("HaB") is DetectorType.HAB)
        self.assertTrue(convert_bank_name_to_detector_type_isis("front") is DetectorType.HAB)
        self.assertRaises(RuntimeError, convert_bank_name_to_detector_type_isis, "test")

    def test_that_gets_facility(self):
        self.assertTrue(get_facility(SANSInstrument.SANS2D) is SANSFacility.ISIS)
        self.assertTrue(get_facility(SANSInstrument.LOQ) is SANSFacility.ISIS)
        self.assertTrue(get_facility(SANSInstrument.LARMOR) is SANSFacility.ISIS)
        self.assertTrue(get_facility(SANSInstrument.ZOOM) is SANSFacility.ISIS)
        self.assertTrue(get_facility(SANSInstrument.NoInstrument) is SANSFacility.NoFacility)

if __name__ == '__main__':
    unittest.main()
