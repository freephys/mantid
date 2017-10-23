#include "MantidQtWidgets/Common/DataProcessorUI/ProcessingAlgorithm.h"
#include <string>

namespace MantidQt {
namespace MantidWidgets {
namespace DataProcessor {

/** Constructor
* @param name : The name of this algorithm
* @param prefix : The list of prefixes that will be used for the output
* workspaces' names
* @param blacklist : The list of properties we do not want to show
*/
ProcessingAlgorithm::ProcessingAlgorithm(const QString &name,
                                         std::vector<QString> prefix,
                                         std::vector<QString> suffix,
                                         const std::set<QString> &blacklist)
    : ProcessingAlgorithmBase(name, blacklist), m_prefix(std::move(prefix)),
      m_suffix(std::move(suffix)) {

  m_inputProperties = getInputWsProperties();
  if (m_inputProperties.empty())
    throw std::invalid_argument("Invalid Processing algorithm. A valid "
                                "algorithm must have at least one input "
                                "workpspace property");

  m_outputProperties = getOutputWsProperties();
  if (m_outputProperties.empty())
    throw std::invalid_argument("Invalid processing algorithm. A valid "
                                "algorithm must have at least one output "
                                "workspace property");

  // The number of prefixes given should match the number of output
  // workspaces
  if (m_outputProperties.size() != m_prefix.size()) {
    throw std::invalid_argument(
        "Invalid ProcessingAlgorithm. The number of prefixes ("
        + std::to_string(m_prefix.size()) + ") given must "
        "match the number of output ws properties (" + std::to_string(m_outputProperties.size()) +
        ") defined for this algorithm");
  }
}

/** Delegating constructor
* @param name : The name of this algorithm
* @param prefix : The list of prefixes that will be used for the output
* workspaces' names, as a string
* @param blacklist : The list of properties we do not want to show, as a string
*/
ProcessingAlgorithm::ProcessingAlgorithm(const QString &name,
                                         const QString &prefix,
                                         const QString &suffix,
                                         const QString &blacklist)
    : ProcessingAlgorithm(name, convertStringToVector(prefix),
                          convertStringToVector(suffix),
                          convertStringToSet(blacklist)) {}

/**
 * Constructor
*/
ProcessingAlgorithm::ProcessingAlgorithm()
    : m_prefix(), m_suffix(), m_inputProperties(), m_outputProperties() {}

// Destructor
ProcessingAlgorithm::~ProcessingAlgorithm() {}

// Returns the number of output properties
size_t ProcessingAlgorithm::numberOfOutputProperties() const {
  return m_outputProperties.size();
}

/** Returns the suffix that will be added to the name of this output ws property
 *@param index : The property index
 */
QString ProcessingAlgorithm::suffix(size_t index) const {
  return m_suffix[index];
}

/** Returns the prefix that will be added to the name of this output ws property
 *@param index : The property index
 */
QString ProcessingAlgorithm::prefix(size_t index) const {
  return m_prefix[index];
}

/** Returns the name of an input property specified by its index
 *@param index : The property index
 */
QString ProcessingAlgorithm::inputPropertyName(size_t index) const {
  return m_inputProperties[index];
}

/** Returns the name of an output ws property specified by its index
 *@param index : The property index
 */
QString ProcessingAlgorithm::outputPropertyName(size_t index) const {
  return m_outputProperties[index];
}
}
}
}
