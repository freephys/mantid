import unittest
from testhelpers import run_algorithm
from mantid.api import AnalysisDataService
from mantid.simpleapi import CreateSampleWorkspace, AddSampleLogMultiple, DeleteWorkspace, GroupWorkspaces


class CompareSampleLogsTest(unittest.TestCase):
    def setUp(self):
        ws1 = CreateSampleWorkspace()
        self.ws1 = ws1
        ws2 = CreateSampleWorkspace()
        self.ws2 = ws2
        lognames = 'run_title,deterota,wavelength,polarisation,flipper'
        logvalues = 'ws1,-10.0,4.2,x,ON'
        AddSampleLogMultiple(Workspace=ws1, LogNames=lognames, LogValues=logvalues, ParseType=True)
        logvalues = 'ws2,-12.0,4.2,x,OFF'
        AddSampleLogMultiple(Workspace=ws2, LogNames=lognames, LogValues=logvalues, ParseType=True)

    def test_workspaces_different_logs(self):
        wslist = [self.ws1, self.ws2]
        lognames = 'deterota,wavelength,polarisation,flipper,qqq'
        alg_test = run_algorithm("CompareSampleLogs", InputWorkspaces=wslist, SampleLogs=lognames,
                                 Tolerance=0.01)
        self.assertTrue(alg_test.isExecuted())
        # check for the returned value
        result = alg_test.getProperty('Result').value
        self.assertEqual('deterota,flipper,qqq', result)

    def test_groups_same_logs(self):
        GroupWorkspaces([self.ws1, self.ws2], OutputWorkspace='group')
        lognames = 'wavelength,polarisation'
        alg_test = run_algorithm("CompareSampleLogs", InputWorkspaces='group', SampleLogs=lognames,
                                 Tolerance=0.01)
        self.assertTrue(alg_test.isExecuted())
        result = alg_test.getProperty('Result').value
        self.assertEqual('', result)

    def tearDown(self):
        if AnalysisDataService.doesExist('ws1'):
            DeleteWorkspace('ws1')
        if AnalysisDataService.doesExist('ws2'):
            DeleteWorkspace('ws2')

if __name__ == "__main__":
    unittest.main()
