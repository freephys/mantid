#ifndef MANTIDQTCUSTOMINTERFACES_ENGGDIFFRACTION_IENGGDIFFFITTINGVIEWQTWIDGET_H_
#define MANTIDQTCUSTOMINTERFACES_ENGGDIFFRACTION_IENGGDIFFFITTINGVIEWQTWIDGET_H_

#include "MantidAPI/IPeakFunction.h"
#include "MantidQtCustomInterfaces/DllConfig.h"
#include "MantidQtCustomInterfaces/EnggDiffraction/IEnggDiffFittingPresenter.h"
#include "MantidQtCustomInterfaces/EnggDiffraction/IEnggDiffFittingView.h"

#include "ui_EnggDiffractionQtTabFitting.h"

#include <boost/scoped_ptr.hpp>

// Qt classes forward declarations
class QMessageBox;
class QMutex;

class QwtPlotCurve;
class QwtPlotZoomer;

namespace MantidQt {

namespace MantidWidgets {
class PeakPicker;
}

namespace CustomInterfaces {

/**
Qt-based view of the Engineering Diffraction (EnggDiff) fitting
widget/tab. Provides a concrete view that is Qt-based and is probably
the only one that will be implemented in a foreseeable horizon. The
interface of this class is given by IEnggDiffFittingView so that it
fits in the MVP (Model-View-Presenter) design of this GUI.

Copyright &copy; 2016 ISIS Rutherford Appleton Laboratory, NScD
Oak Ridge National Laboratory & European Spallation Source

This file is part of Mantid.

Mantid is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

Mantid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

File change history is stored at: <https://github.com/mantidproject/mantid>
Code Documentation is available at: <http://doxygen.mantidproject.org>
*/
class MANTIDQT_CUSTOMINTERFACES_DLL EnggDiffFittingViewQtWidget
    : public QWidget,
      public IEnggDiffFittingView {
  Q_OBJECT

public:
  EnggDiffFittingViewQtWidget(
      QWidget *parent, boost::shared_ptr<IEnggDiffractionUserMsg> mainMsg);
  ~EnggDiffFittingViewQtWidget() override;

  void showStatus(const std::string &sts) override;

  void userWarning(const std::string &warn,
                   const std::string &description) override;

  void userError(const std::string &err,
                 const std::string &description) override;

  void enableCalibrateFocusFitUserActions(bool enable) override;

  void enable(bool enable);

  void setFittingRunNo(const std::string &path) override;

  std::string getFittingRunNo() const override;

  void clearFittingComboBox() const override;

  void enableFittingComboBox(bool enable) const override;

  int getFittingComboIdx(std::string bank) const override;

  void clearFittingListWidget() const override;

  void enableFittingListWidget(bool enable) const override;

  int getFittingListWidgetCurrentRow() const override;

  void setFittingListWidgetCurrentRow(int idx) const override;

  std::string fittingPeaksData() const override;

  void setPeakList(const std::string &peakList) const override;

  std::vector<std::string>
  splitFittingDirectory(std::string &selectedfPath) override;

  void setBankEmit() override;

  std::string getFocusDir() override;

  void setDataVector(std::vector<boost::shared_ptr<QwtData>> &data,
                     bool focused, bool plotSinglePeaks) override;

  void addBankItem(std::string bankID) override;

  void addRunNoItem(std::string runNo) override;

  std::vector<std::string> getFittingRunNumVec() override;

  void setFittingRunNumVec(std::vector<std::string> assignVec) override;

  bool getFittingMultiRunMode() override;

  void setFittingMultiRunMode(bool mode) override;

  std::string fittingRunNoFactory(std::string bank, std::string fileName,
                                  std::string &bankDir, std::string fileDir);

  std::string readPeaksFile(std::string fileDir);

  void dataCurvesFactory(std::vector<boost::shared_ptr<QwtData>> &data,
                         std::vector<QwtPlotCurve *> &dataVector, bool focused);

  void setPeakPickerEnabled(bool enabled);

  void setPeakPicker(const Mantid::API::IPeakFunction_const_sptr &peak);

  double getPeakCentre() const;

  void fittingWriteFile(const std::string &fileDir);

  void setZoomTool(bool enabled);

  void resetView();

protected:
  void initLayout();

signals:
  void getBanks();
  void setBank();

private slots:
  // enables the text field when appropriate bank name is selected
  void enableSpecNos();

  // slot of the fitting peaks per part of the interface
  void browseFitFocusedRun();
  void resetFittingMultiMode();
  void setBankIdComboBox(int idx) override;
  void browsePeaksToFit();
  void setPeakPick();
  void addPeakToList();
  void savePeakList();
  void clearPeakList();
  void fitClicked();
  void FittingRunNo();
  void plotSeparateWindow();
  void setBankDir(int idx);
  void listViewFittingRun();

private:
  /// Setup the interface (tab UI)
  void doSetup();

  /// Load saved/default interface settings
  void readSettings();
  /// save settings (before closing)
  void saveSettings() const override;

  Ui::EnggDiffractionQtTabFitting m_ui;

  /// converts QList to a vector
  std::vector<std::string> qListToVector(QStringList list,
                                         bool validator) const;

  // path/name for the persistent settings group of this interface
  static const std::string g_settingsGroup;

  static const std::string g_peaksListExt;

  /// indentifier for fitting multi-run or single run input
  static bool m_fittingMutliRunMode;

  // vector holding directory of focused bank file
  static std::vector<std::string> m_fitting_runno_dir_vec;

  /// Loaded focused workspace
  std::vector<QwtPlotCurve *> m_focusedDataVector;

  /// Loaded data curves
  std::vector<QwtPlotCurve *> m_fittedDataVector;

  /// Peak picker tool for fitting - only one on the plot at any given moment
  MantidWidgets::PeakPicker *m_peakPicker = nullptr;

  /// zoom-in/zoom-out tool for fitting
  QwtPlotZoomer *m_zoomTool = nullptr;

  // user messages interface provided by a main view/widget
  boost::shared_ptr<IEnggDiffractionUserMsg> m_mainMsgProvider;

  /// presenter as in the model-view-presenter
  boost::scoped_ptr<IEnggDiffFittingPresenter> m_presenter;
};

} // namespace CustomInterfaces
} // namespace MantidQt

#endif // MANTIDQTCUSTOMINTERFACES_ENGGDIFFRACTION_IENGGDIFFFITTINGVIEWQTWIDGET_H_