#include "MantidQtMantidWidgets/MuonSequentialFitDialog.h"
#include "MantidAPI/AnalysisDataService.h" 

namespace MantidQt
{
namespace MantidWidgets
{
  using namespace Mantid::Kernel;
  using namespace Mantid::API;

  Logger& MuonSequentialFitDialog::g_log(Logger::get("MuonSequentialFitDialog"));

  /** 
   * Constructor
   */
  MuonSequentialFitDialog::MuonSequentialFitDialog(QWidget* parent) :
    QDialog(parent) 
  {
    ui.setupUi(this);

    // TODO: set initial values 

    // After initial values are set, update depending elements accordingly. We don't rely on
    // slot/signal update, as element might be left with default values which means these will
    // never be called on initialication.
    updateLabelError( ui.labelInput->text() );
    updateStartButton();

    connect( ui.labelInput, SIGNAL( textChanged(const QString&) ), 
      this, SLOT( updateLabelError(const QString&) ) );

    connect( ui.labelInput, SIGNAL( textChanged(const QString&) ), 
      this, SLOT( updateStartButton() ) );
    connect( ui.runs, SIGNAL( fileFindingFinished() ), 
      this, SLOT( updateStartButton() ) );
  }

  /**
   * Checks if specified name is valid as a name for label. 
   * @param label :: The name to check
   * @return Empty string if valid, otherwise a string describing why is invalid
   */
  std::string MuonSequentialFitDialog::isValidLabel(const std::string& label)
  {
    if ( label.empty() )
      return "Can not be empty";
    else
      return AnalysisDataService::Instance().isValid(label);
  }

  /**
   * Updates visibility/tooltip of label error asterisk.
   * @param label :: New label as specified by user 
   */
  void MuonSequentialFitDialog::updateLabelError(const QString& label)
  {
    std::string error = isValidLabel( label.toStdString() );

    ui.labelError->setVisible( ! error.empty() ); 
    ui.labelError->setToolTip( QString::fromStdString(error) );
  }

  /**
   * Check if all the input field are valid.
   * @return True if everything valid, false otherwise
   */
  bool MuonSequentialFitDialog::isInputValid()
  {
    if ( ! ui.runs->isValid() )
      return false;  

    std::string label = ui.labelInput->text().toStdString();
    if ( ! isValidLabel(label).empty() )
      return false;

    return true;
  }

  /**
   * Enables/disables start button depending on wether we are allowed to start.
   */
  void MuonSequentialFitDialog::updateStartButton()
  {
    ui.controlButton->setEnabled( isInputValid() );
  }

  /**
   * Destructor
   */
  MuonSequentialFitDialog::~MuonSequentialFitDialog()
  {}

} // namespace MantidWidgets
} // namespace Mantid
