from __future__ import (absolute_import, division, print_function)

import mantid.simpleapi as mantid

from isis_powder.routines import common, instrument_settings
from isis_powder.abstract_inst import AbstractInst
from isis_powder.pearl_routines import pearl_advanced_config, pearl_algs, pearl_calibration_algs, pearl_output, \
    pearl_param_mapping


class Pearl(AbstractInst):

    def __init__(self, **kwargs):
        self._inst_settings = instrument_settings.InstrumentSettings(
           param_map=pearl_param_mapping.attr_mapping, adv_conf_dict=pearl_advanced_config.get_all_adv_variables(),
           kwargs=kwargs)

        super(Pearl, self).__init__(user_name=self._inst_settings.user_name,
                                    calibration_dir=self._inst_settings.calibration_dir,
                                    output_dir=self._inst_settings.output_dir, inst_prefix="PEARL")

        self._cached_run_details = {}

    def focus(self, **kwargs):
        self._switch_long_mode_inst_settings(kwargs.get("long_mode"))
        self._inst_settings.update_attributes(kwargs=kwargs)
        return self._focus(run_number_string=self._inst_settings.run_number,
                           do_absorb_corrections=self._inst_settings.absorb_corrections,
                           do_van_normalisation=self._inst_settings.van_norm)

    def create_vanadium(self, **kwargs):
        self._switch_long_mode_inst_settings(kwargs.get("long_mode"))
        kwargs["perform_attenuation"] = None  # Hard code this off as we do not need an attenuation file
        self._inst_settings.update_attributes(kwargs=kwargs)

        if str(self._inst_settings.tt_mode).lower() == "all":
            for new_tt_mode in ["tt35", "tt70", "tt88"]:
                self._inst_settings.tt_mode = new_tt_mode
                self._run_create_vanadium()
        else:
            self._run_create_vanadium()

    def create_cal(self, **kwargs):
        self._switch_long_mode_inst_settings(kwargs.get("long_mode"))
        self._inst_settings.update_attributes(kwargs=kwargs)
        run_details = self._get_run_details(self._inst_settings.run_number)

        cross_correlate_params = {"ReferenceSpectra": self._inst_settings.reference_spectra,
                                  "WorkspaceIndexMin": self._inst_settings.cross_corr_ws_min,
                                  "WorkspaceIndexMax": self._inst_settings.cross_corr_ws_max,
                                  "XMin": self._inst_settings.cross_corr_x_min,
                                  "XMax": self._inst_settings.cross_corr_x_max}
        get_detector_offsets_params = {"DReference": self._inst_settings.d_reference,
                                       "Step": self._inst_settings.get_det_offsets_step,
                                       "XMin": self._inst_settings.get_det_offsets_x_min,
                                       "XMax": self._inst_settings.get_det_offsets_x_max}

        return pearl_calibration_algs.create_calibration(calibration_runs=self._inst_settings.run_number,
                                                         instrument=self,
                                                         offset_file_name=run_details.offset_file_path,
                                                         grouping_file_name=run_details.grouping_file_path,
                                                         calibration_dir=self._inst_settings.calibration_dir,
                                                         rebin_1_params=self._inst_settings.cal_rebin_1,
                                                         rebin_2_params=self._inst_settings.cal_rebin_2,
                                                         cross_correlate_params=cross_correlate_params,
                                                         get_det_offset_params=get_detector_offsets_params)

    def _run_create_vanadium(self):
        # Provides a minimal wrapper so if we have tt_mode 'all' we can loop round
        return self._create_vanadium(run_number_string=self._inst_settings.run_in_range,
                                     do_absorb_corrections=self._inst_settings.absorb_corrections)

    def _get_run_details(self, run_number_string):
        run_number_string_key = self._generate_run_details_fingerprint(run_number_string,
                                                                       self._inst_settings.file_extension,
                                                                       self._inst_settings.tt_mode)
        if run_number_string_key in self._cached_run_details:
            return self._cached_run_details[run_number_string_key]

        self._cached_run_details[run_number_string_key] = pearl_algs.get_run_details(
            run_number_string=run_number_string, inst_settings=self._inst_settings, is_vanadium_run=self._is_vanadium)
        return self._cached_run_details[run_number_string_key]

    def _generate_output_file_name(self, run_number_string):
        inst = self._inst_settings
        return pearl_algs.generate_out_name(run_number_string=run_number_string,
                                            long_mode_on=inst.long_mode, tt_mode=inst.tt_mode)

    def _normalise_ws_current(self, ws_to_correct):
        monitor_spectra = self._inst_settings.monitor_spec_no

        monitor_ws = common.extract_single_spectrum(ws_to_process=ws_to_correct,
                                                    spectrum_number_to_extract=monitor_spectra)

        normalised_ws = pearl_algs.normalise_ws_current(ws_to_correct=ws_to_correct, monitor_ws=monitor_ws,
                                                        spline_coeff=self._inst_settings.monitor_spline,
                                                        integration_range=self._inst_settings.monitor_integration_range,
                                                        lambda_values=self._inst_settings.monitor_lambda,
                                                        ex_regions=self._inst_settings.monitor_mask_regions)
        common.remove_intermediate_workspace(monitor_ws)
        return normalised_ws

    def _get_current_tt_mode(self):
        return self._inst_settings.tt_mode

    def _spline_vanadium_ws(self, focused_vanadium_spectra):
        focused_vanadium_spectra = pearl_algs.strip_bragg_peaks(focused_vanadium_spectra)
        splined_list = common.spline_workspaces(focused_vanadium_spectra=focused_vanadium_spectra,
                                                num_splines=self._inst_settings.spline_coefficient)
        # Ensure the name is unique if we are in tt_mode all
        new_workspace_names = []
        for ws in splined_list:
            new_name = ws.getName() + '_' + self._inst_settings.tt_mode
            new_workspace_names.append(mantid.RenameWorkspace(InputWorkspace=ws, OutputWorkspace=new_name))

        return new_workspace_names

    def _output_focused_ws(self, processed_spectra, run_details, output_mode=None):
        if not output_mode:
            output_mode = self._inst_settings.focus_mode

        if self._inst_settings.perform_atten:
            attenuation_path = self._inst_settings.attenuation_file_path
        else:
            attenuation_path = None

        output_spectra = \
            pearl_output.generate_and_save_focus_output(self, processed_spectra=processed_spectra,
                                                        run_details=run_details, focus_mode=output_mode,
                                                        attenuation_filepath=attenuation_path)
        group_name = "PEARL" + str(run_details.output_run_string)
        group_name += '_' + self._inst_settings.tt_mode + "-Results-D-Grp"
        grouped_d_spacing = mantid.GroupWorkspaces(InputWorkspaces=output_spectra, OutputWorkspace=group_name)
        return grouped_d_spacing, None

    def _crop_banks_to_user_tof(self, focused_banks):
        return common.crop_banks_using_crop_list(focused_banks, self._inst_settings.tof_cropping_values)

    def _crop_raw_to_expected_tof_range(self, ws_to_crop):
        out_ws = common.crop_in_tof(ws_to_crop=ws_to_crop, x_min=self._inst_settings.raw_data_crop_vals[0],
                                    x_max=self._inst_settings.raw_data_crop_vals[-1])
        return out_ws

    def _crop_van_to_expected_tof_range(self, van_ws_to_crop):
        cropped_ws = common.crop_in_tof(ws_to_crop=van_ws_to_crop, x_min=self._inst_settings.van_tof_cropping[0],
                                        x_max=self._inst_settings.van_tof_cropping[-1])
        return cropped_ws

    def _apply_absorb_corrections(self, run_details, ws_to_correct):
        if self._inst_settings.gen_absorb:
            absorb_file_name = self._inst_settings.absorb_out_file
            if not absorb_file_name:
                raise RuntimeError("\"absorb_corrections_out_filename\" must be supplied when generating absorption "
                                   "corrections")
            absorb_corrections = pearl_algs.generate_vanadium_absorb_corrections(van_ws=ws_to_correct,
                                                                                 output_filename=absorb_file_name)
        else:
            absorb_corrections = None

        return pearl_algs.apply_vanadium_absorb_corrections(van_ws=ws_to_correct, run_details=run_details,
                                                            absorb_ws=absorb_corrections)

    def _switch_long_mode_inst_settings(self, long_mode_on):
        self._inst_settings.update_attributes(advanced_config=pearl_advanced_config.get_long_mode_dict(long_mode_on),
                                              suppress_warnings=True)
