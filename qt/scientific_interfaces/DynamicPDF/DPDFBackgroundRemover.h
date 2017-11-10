#ifndef MANTIDQTCUSTOMINTERFACES_DYNAMICPDF_BACKGROUNDREMOVER_H_
#define MANTIDQTCUSTOMINTERFACES_DYNAMICPDF_BACKGROUNDREMOVER_H_

// Mantid Coding standars <http://www.mantidproject.org/Coding_Standards>
// Mantid Headers from the same project
#include "ui_DPDFBackgroundRemover.h"
// Mantid headers from other projects
#include "DllConfig.h"
#include "MantidQtWidgets/Common/UserSubWindow.h"
// 3rd party library headers
#include <QDialog>
#include <boost/shared_ptr.hpp>

// Class forward declarations
namespace MantidQt {
namespace CustomInterfaces {
namespace DynamicPDF {
class InputDataControl;
class SliceSelector;
class DisplayControl;
class FitControl;
class FourierTrasform;
}
}
}

namespace MantidQt {
namespace CustomInterfaces {
namespace DynamicPDF {
/** An interface to remove the multiphonon background from a
   S(Q,E) structure factor.

  @date 2016-03-11

  Copyright &copy; 2012 ISIS Rutherford Appleton Laboratory, NScD Oak Ridge
 National Laboratory & European Spallation Source

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
class MANTIDQT_DYNAMICPDF_DLL BackgroundRemover
    : public MantidQt::API::UserSubWindow {
  Q_OBJECT

public:
  /// The name of the interface as registered into the factory
  static std::string name() { return "Dynamic PDF Background Remover"; }
  // This interface's categories.
  static QString categoryInfo() { return "DynamicPDF"; }
  BackgroundRemover(QWidget *parent = nullptr);
  ~BackgroundRemover() override;

private slots:
  void showHelp();
  void summonSliceSelector();

private:
  void initLayout() override;
  /// The form generated by Qt Designer
  Ui::BackgroundRemover m_uiForm;
  /// GUI to load slices and select slice for fitting
  std::unique_ptr<SliceSelector> m_sliceSelector;
  /// Manage data of the loaded slice
  std::unique_ptr<InputDataControl> m_inputDataControl;
  /// Format the curves to be displayed
  std::unique_ptr<DisplayControl> m_displayControl;
  /// Managing the model and browser
  FitControl *m_fitControl;
  FourierTransform *m_fourierTransform;
};
}
}
}

#endif // MANTIDQTCUSTOMINTERFACES_DYNAMICPDF_BACKGROUNDREMOVER_H_
