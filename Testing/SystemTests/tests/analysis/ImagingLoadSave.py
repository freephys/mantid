import os
import unittest
import stresstesting

from mantid.simpleapi import CompareWorkspaces, DeleteWorkspace, LoadFITS, SaveFITS, mtd
from mantid import config

class ImagingLoadSaveTests(unittest.TestCase):
    """
    Tests load/save images. This is just around FITS format at the
    moment. There should be tests on other formats and conversions
    when we have the algorithms Load/SaveImage.
    """

    def setUp(self):
        # Sharing some files with the ImggAggregateWavelengths system test
        data_root = config['datasearch.directories'].split(';')[0]
        self._fits_files_dir = os.path.join(data_root, 'wavelength_dependent_images')

        # subdir and filename components
        self._fits_files_comps = [
            ('angle0', 'LARMOR00005471_Metals_000_00000.fits'),
            ('angle0', 'LARMOR00005471_Metals_000_00001.fits'),
            ('angle0', 'LARMOR00005471_Metals_000_00002.fits'),
            ('angle0', 'LARMOR00005471_Metals_000_00003.fits'),
            ('angle0', 'LARMOR00005471_Metals_000_00004.fits'),
            ('angle0', 'LARMOR00005471_Metals_000_00005.fits'),
            ('angle1', 'LARMOR00005329_Metals_000_00000.fits'),
            ('angle1', 'LARMOR00005329_Metals_000_00001.fits'),
            ('angle1', 'LARMOR00005329_Metals_000_00002.fits'),
            ('angle2', 'LARMOR00005330_Metals_000_01343.fits'),
            ('angle2', 'LARMOR00005330_Metals_000_01344.fits'),
            ('angle5', 'LARMOR00005333_Metals_000_00690.fits')
        ]

        self._fits_paths = [os.path.join(self._fits_files_dir, comps[0], comps[1])\
                            for comps in self._fits_files_comps]


    def test_load_all_indiv(self):
        """
        Load a few files with different options and check they load correctly
        """

        group_name = 'all_fits_rect'
        for fpath in self._fits_paths:
            group = LoadFITS(Filename=fpath, LoadAsRectImg=True, OutputWorkspace=group_name)

        group_norect_name = 'all_fits_norect'
        for fpath in self._fits_paths:
            group_norect = LoadFITS(Filename=fpath, LoadAsRectImg=False, OutputWorkspace=group_norect_name)

        self.assertEquals(group.size(), group_norect.size())
        for idx in range(0, group.size()):
            img_a = group.getItem(idx)
            size_a = img_a.getNumberHistograms() * img_a.blocksize()
            img_b = group_norect.getItem(idx)
            size_b = img_b.getNumberHistograms() * img_b.blocksize()
            self.assertEquals(size_a, size_b)
            self.assertEquals(img_a.getTitle(), img_b.getTitle())

            for row in [0, 100, 200, 300, 400, 511]:
                self.assertEquals(img_a.readY(row)[0], img_b.readY(row*img_a.blocksize() + 0))

        DeleteWorkspace(group_name)
        DeleteWorkspace(group_norect_name)

    def test_load_all_at_once(self):
        """
        A batch load, as when stacks are loaded at once
        """
        all_filepaths = ','.join(self._fits_paths)
        group = LoadFITS(Filename=all_filepaths, LoadAsRectImg=True)

        self.assertEquals(group.size(), len(self._fits_paths))

        DeleteWorkspace(group)

    def test_load_save_load(self):
        """
        Check that nothing is lost in a Load/Save/Load cycle
        """
        group_name = 'all_indiv'
        for fpath in self._fits_paths:
            LoadFITS(Filename=fpath, LoadAsRectImg=True, OutputWorkspace=group_name)
        group = mtd[group_name]

        for idx in range(0, group.size()):
            # Save
            img_loaded = group.getItem(idx)
            save_filename = 'test.fits'
            SaveFITS(Filename=save_filename, InputWorkspace=img_loaded)

            # Re-load and compare
            reload_name = 'indiv_fits_reloaded'
            grp_reloaded = LoadFITS(Filename=save_filename, LoadAsRectImg=True, OutputWorkspace=reload_name)
            self.assertEquals(1, grp_reloaded.size())
            img_reloaded = grp_reloaded.getItem(0)

            self.assertEquals(img_loaded.getNumberHistograms(), img_reloaded.getNumberHistograms())
            self.assertEquals(img_loaded.blocksize(), img_reloaded.blocksize())

            (comp_result, tbl_messages) = CompareWorkspaces(img_loaded, img_reloaded)
            num_rows = tbl_messages.rowCount()
            txt_messages = [tbl_messages.row(idx) for idx in range(0, num_rows)]
            self.assertTrue(comp_result,
                            "Workspace comparison failed. Details: {0}".format(txt_messages))
            DeleteWorkspace(grp_reloaded)

        DeleteWorkspace(group_name)

# Runs the unittest tests defined above in the mantid stress testing framework
class ImagingAggregateWavelengths(stresstesting.MantidStressTest):

    _success = False

    def __init__(self, *args, **kwargs):
        # super(ImagingAggregateWavelengths, self).__init__(*args, **kwargs)
        # old-style
        stresstesting.MantidStressTest.__init__(self, *args, **kwargs)
        self._success = False

        self._raw_in_files = [ 'wavelength_dependent_images/angle0/LARMOR00005471_Metals_000_00000.fits',
                               'wavelength_dependent_images/angle0/LARMOR00005471_Metals_000_00001.fits',
                               'wavelength_dependent_images/angle0/LARMOR00005471_Metals_000_00002.fits',
                               'wavelength_dependent_images/angle0/LARMOR00005471_Metals_000_00003.fits',
                               'wavelength_dependent_images/angle0/LARMOR00005471_Metals_000_00004.fits',
                               'wavelength_dependent_images/angle0/LARMOR00005471_Metals_000_00005.fits',
                               'wavelength_dependent_images/angle1/LARMOR00005329_Metals_000_00000.fits',
                               'wavelength_dependent_images/angle1/LARMOR00005329_Metals_000_00001.fits',
                               'wavelength_dependent_images/angle1/LARMOR00005329_Metals_000_00002.fits',
                               'wavelength_dependent_images/angle2/LARMOR00005330_Metals_000_01343.fits',
                               'wavelength_dependent_images/angle2/LARMOR00005330_Metals_000_01344.fits',
                               'wavelength_dependent_images/angle5/LARMOR00005333_Metals_000_00690.fits',
                             ]

    def requiredFiles(self):
        return set(self._raw_in_files)

    def runTest(self):
        self._success = False
        # Custom code to create and run this single test suite
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(ImagingLoadSaveTests, "test") )
        runner = unittest.TextTestRunner()
        res = runner.run(suite)
        self._success = res.wasSuccessful()

    def validate(self):
        return self._success
