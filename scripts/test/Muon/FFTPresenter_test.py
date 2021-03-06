import sys

from Muon import load_utils
from Muon import fft_presenter
from Muon import fft_view
from Muon import fft_model
from Muon import thread_model

import unittest

if sys.version_info.major ==  3:
   from unittest import mock
else:
   import mock


class FFTPresenterTest(unittest.TestCase):
   def setUp(self):
       self.load = mock.create_autospec(load_utils.LoadUtils,spec_set=True)
       self.load.getCurrentWS = mock.Mock(return_value=["TEST00000001",["fwd","bkwd"]])
       self.load.getRunName = mock.MagicMock(return_value="MUSR00023456")
       self.view = mock.create_autospec(fft_view.FFTView,spec_set=True)
       #signals
       self.view.tableClickSignal = mock.Mock(return_value=[3,1])
       self.view.phaseCheckSignal = mock.Mock(return_value =True)
       #needed for connect in presenter
       self.view.buttonSignal = mock.Mock()
       self.view.changed = mock.MagicMock()
       self.view.changedHideUnTick = mock.MagicMock()
       self.view.initFFTInput = mock.Mock(return_value={"InputWorkspace":"testWS","OutputWorkspace":"muon"})
       self.view.addFFTComplex = mock.Mock(return_value={"InputImWorkspace":"MuonFFT"})
       self.view.addFFTShift = mock.Mock()
       self.view.addRaw = mock.Mock()
       self.view.RePhaseAdvanced = mock.Mock()
       self.view.getFFTRePhase = mock.Mock()
       self.view.getFFTImPhase = mock.Mock()
       self.view.getWS = mock.Mock(return_value="MUSR00023456")
       self.view.getFirstGoodData = mock.Mock(return_value=0.1)
       self.view.getLastGoodData = mock.Mock(return_value=15.)
       self.view.getImBoxRow = mock.Mock(return_value=3)
       self.view.getShiftBoxRow = mock.Mock(return_value=5)
       self.view.isRaw = mock.Mock(return_value=True)
       self.view.isComplex = mock.Mock(return_value=True)
       self.view.isAutoShift = mock.Mock(return_value=True)
       self.view.setPhaseBox = mock.Mock()
       self.view.isNewPhaseTable = mock.Mock(return_value=True)
       self.view.activateButton = mock.Mock()
       self.view.deactivateButton = mock.Mock()
       # setup model
       self.model1 = mock.create_autospec(fft_model.FFTModel,spec_set=False)
       self.model = mock.create_autospec(fft_model.FFTWrapper,spec_set=False)

       #set presenter
       self.presenter = fft_presenter.FFTPresenter(self.view,self.model,self.load)

       # mock thread
       self.thread = mock.create_autospec(thread_model.ThreadModel)
       self.thread.start = mock.Mock()
       self.thread.started = mock.Mock()
       self.thread.finished = mock.Mock()
       self.thread.setInputs = mock.Mock()
       self.thread.loadData = mock.Mock()
       self.presenter.createThread = mock.Mock(return_value=self.thread)

   def sendSignal(self):
       row,col = self.view.tableClickSignal()
       self.presenter.tableClicked(row,col)

   def test_ImBox(self):
       self.sendSignal()
       self.view.tableClickSignal = mock.Mock(return_value=[3,1])
       assert(self.view.changedHideUnTick.call_count == 1)
       assert(self.view.changed.call_count  ==  0)

   def test_shiftBox(self):
       self.view.tableClickSignal = mock.Mock(return_value=[5,1])
       self.sendSignal()
       assert(self.view.changed.call_count == 1)
       assert(self.view.changedHideUnTick.call_count == 0)

   def test_buttonNotRawAndNoIm(self):
       self.view.isAutoShift = mock.Mock(return_value=True)
       self.view.isComplex = mock.Mock(return_value=False)
       self.view.isRaw = mock.Mock(return_value=False)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 0)
       assert(self.view.addFFTShift.call_count == 0)
       assert(self.view.addRaw.call_count == 0)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 0)
       assert(self.view.getLastGoodData.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonNotRawAndIm(self):
       self.view.isAutoShift = mock.Mock(return_value=True)
       self.view.isComplex = mock.Mock(return_value=True)
       self.view.isRaw = mock.Mock(return_value=False)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 1)
       assert(self.view.addFFTShift.call_count == 0)
       assert(self.view.addRaw.call_count == 0)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 0)
       assert(self.view.getLastGoodData.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonRawAndIm(self):
       self.view.isAutoShift = mock.Mock(return_value=True)
       self.view.isComplex = mock.Mock(return_value=True)
       self.view.isRaw = mock.Mock(return_value=True)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 1)
       assert(self.view.addFFTShift.call_count == 0)
       assert(self.view.addRaw.call_count == 3)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 0)
       assert(self.view.getLastGoodData.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonRawAndNoIm(self):
       self.view.isAutoShift = mock.Mock(return_value=True)
       self.view.isComplex = mock.Mock(return_value=False)
       self.view.isRaw = mock.Mock(return_value=True)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 0)
       assert(self.view.addFFTShift.call_count == 0)
       assert(self.view.addRaw.call_count == 2)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 0)
       assert(self.view.getLastGoodData.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonNoShiftNotRawAndNoIm(self):
       self.view.isAutoShift = mock.Mock(return_value=False)
       self.view.isComplex = mock.Mock(return_value=False)
       self.view.isRaw = mock.Mock(return_value=False)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 0)
       assert(self.view.addFFTShift.call_count == 1)
       assert(self.view.addRaw.call_count == 0)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 0)
       assert(self.view.getLastGoodData.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonNoShiftNotRawAndIm(self):
       self.view.isAutoShift = mock.Mock(return_value=False)
       self.view.isComplex = mock.Mock(return_value=True)
       self.view.isRaw = mock.Mock(return_value=False)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 1)
       assert(self.view.addFFTShift.call_count == 1)
       assert(self.view.addRaw.call_count == 0)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 0)
       assert(self.view.getLastGoodData.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonNoShiftRawAndIm(self):
       self.view.isAutoShift = mock.Mock(return_value=False)
       self.view.isComplex = mock.Mock(return_value=True)
       self.view.isRaw = mock.Mock(return_value=True)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 1)
       assert(self.view.addFFTShift.call_count == 1)
       assert(self.view.addRaw.call_count == 3)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 0)
       assert(self.view.getLastGoodData.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonNoShiftRawAndNoIm(self):
       self.view.isAutoShift = mock.Mock(return_value=False)
       self.view.isComplex = mock.Mock(return_value=False)
       self.view.isRaw = mock.Mock(return_value=True)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 0)
       assert(self.view.addFFTShift.call_count == 1)
       assert(self.view.addRaw.call_count == 2)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 0)
       assert(self.view.getLastGoodData.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonPhaseQuad(self):
       self.view.getWS = mock.Mock(return_value="PhaseQuad")
       self.view.isComplex = mock.Mock(return_value=False)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 0)
       assert(self.view.addFFTShift.call_count == 0)
       assert(self.view.addRaw.call_count == 0)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 1)
       assert(self.view.getLastGoodData.call_count == 1)
       assert(self.view.RePhaseAdvanced.call_count == 1)
       assert(self.view.getFFTRePhase.call_count == 1)
       assert(self.view.getFFTImPhase.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonImPhaseQuad(self):
       self.view.getWS = mock.Mock(return_value="PhaseQuad")
       self.view.isComplex = mock.Mock(return_value=True)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 1)
       assert(self.view.addFFTShift.call_count == 0)
       assert(self.view.addRaw.call_count == 0)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 1)
       assert(self.view.getLastGoodData.call_count == 1)
       assert(self.view.RePhaseAdvanced.call_count == 1)
       assert(self.view.getFFTRePhase.call_count == 1)
       assert(self.view.getFFTImPhase.call_count == 1)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonPhaseQuadNoTable(self):
       self.view.getWS = mock.Mock(return_value="PhaseQuad")
       self.view.isComplex = mock.Mock(return_value=False)
       self.view.isNewPhaseTable = mock.Mock(return_value=False)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 0)
       assert(self.view.addFFTShift.call_count == 0)
       assert(self.view.addRaw.call_count == 0)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 1)
       assert(self.view.getLastGoodData.call_count == 1)
       assert(self.view.RePhaseAdvanced.call_count == 1)
       assert(self.view.getFFTRePhase.call_count == 1)
       assert(self.view.getFFTImPhase.call_count == 0)
       assert(self.presenter.thread.start.call_count == 1)

   def test_buttonImPhaseQuadNoTable(self):
       self.view.getWS = mock.Mock(return_value="PhaseQuad")
       self.view.isNewPhaseTable = mock.Mock(return_value=False)
       self.view.isComplex = mock.Mock(return_value=True)
       self.presenter.handleButton()
       assert(self.view.initFFTInput.call_count == 1)
       assert(self.view.addFFTComplex.call_count == 1)
       assert(self.view.addFFTShift.call_count == 0)
       assert(self.view.addRaw.call_count == 0)
       assert(self.view.setPhaseBox.call_count == 1)
       assert(self.view.getFirstGoodData.call_count == 1)
       assert(self.view.getLastGoodData.call_count == 1)
       assert(self.view.RePhaseAdvanced.call_count == 1)
       assert(self.view.getFFTRePhase.call_count == 1)
       assert(self.view.getFFTImPhase.call_count == 1)
       assert(self.presenter.thread.start.call_count == 1)

   def test_activateButton(self):
       self.presenter.activate()
       assert(self.view.activateButton.call_count == 1)

   def test_deactivateButton(self):
       self.presenter.deactivate()
       assert(self.view.deactivateButton.call_count == 1)


if __name__ ==  '__main__':
   unittest.main()
