#include "MantidAPI/AlgorithmManager.h"
#include "MantidAPI/AnalysisDataService.h"
#include "MantidQtAPI/QwtWorkspaceSpectrumData.h"
#include "MantidQtAPI/UserSubWindow.h"
#include "MantidQtCustomInterfaces/Indirect/IndirectBayesTab.h"

using MantidQt::MantidWidgets::RangeSelector;

namespace MantidQt {
namespace CustomInterfaces {

//----------------------------------------------------------------------------------------------
/** Constructor
 */
IndirectBayesTab::IndirectBayesTab(QWidget *parent)
    : IndirectTab(parent), m_propTree(new QtTreePropertyBrowser()) {
  m_propTree->setFactoryForManager(m_dblManager, m_dblEdFac);

  // Connect double maneger signals
  connect(m_dblManager, SIGNAL(valueChanged(QtProperty *, double)), this,
          SLOT(updateProperties(QtProperty *, double)));
}

//----------------------------------------------------------------------------------------------
/** Destructor
 */
IndirectBayesTab::~IndirectBayesTab() {}

/**
 * Emits a signal to run a python script using the method in the parent
 * UserSubWindow
 *
 * @param pyInput :: A string of python code to execute
 */
void IndirectBayesTab::runPythonScript(const QString &pyInput) {
  emit runAsPythonScript(pyInput, true);
}
}
} // namespace MantidQt
