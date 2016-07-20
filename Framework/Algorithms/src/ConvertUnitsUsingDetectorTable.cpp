#include "MantidAlgorithms/ConvertUnitsUsingDetectorTable.h"

#include "MantidDataObjects/EventWorkspace.h"
#include "MantidDataObjects/TableWorkspace.h"
#include "MantidGeometry/IDetector.h"
#include "MantidKernel/ListValidator.h"
#include "MantidKernel/Unit.h"
#include "MantidKernel/UnitFactory.h"

#include <boost/bind.hpp>
#include <boost/function.hpp>
#include <boost/math/special_functions/fpclassify.hpp>

#include <algorithm>
#include <cfloat>
#include <limits>

namespace Mantid {
namespace Algorithms {

using Mantid::Kernel::Direction;
using Mantid::API::WorkspaceProperty;
using namespace Kernel;
using namespace API;
using namespace DataObjects;
using boost::function;
using boost::bind;

// Register the algorithm into the AlgorithmFactory
DECLARE_ALGORITHM(ConvertUnitsUsingDetectorTable)

//----------------------------------------------------------------------------------------------

/// Algorithms name for identification. @see Algorithm::name
const std::string ConvertUnitsUsingDetectorTable::name() const {
  return "ConvertUnitsUsingDetectorTable";
}

/// Algorithm's version for identification. @see Algorithm::version
int ConvertUnitsUsingDetectorTable::version() const { return 1; }

/// Algorithm's category for identification. @see Algorithm::category
const std::string ConvertUnitsUsingDetectorTable::category() const {
  return "Utility\\Development";
}

/// Algorithm's summary for use in the GUI and help. @see Algorithm::summary
const std::string ConvertUnitsUsingDetectorTable::summary() const {
  return "Performs a unit change on the X values of a workspace";
}

//----------------------------------------------------------------------------------------------
/** Initialize the algorithm's properties.
 */
void ConvertUnitsUsingDetectorTable::init() {
  declareProperty(
      make_unique<WorkspaceProperty<>>("InputWorkspace", "", Direction::Input),
      "An input workspace.");
  declareProperty(make_unique<WorkspaceProperty<>>("OutputWorkspace", "",
                                                   Direction::Output),
                  "An output workspace.");
  declareProperty("Target", "", boost::make_shared<StringListValidator>(
                                    UnitFactory::Instance().getKeys()),
                  "The name of the units to convert to (must be one of those "
                  "registered in\n"
                  "the Unit Factory)");
  declareProperty(
      make_unique<WorkspaceProperty<TableWorkspace>>(
          "DetectorParameters", "", Direction::Input, PropertyMode::Optional),
      "Name of a TableWorkspace containing the detector parameters "
      "to use instead of the IDF.");

  declareProperty("AlignBins", false,
                  "If true (default is false), rebins after conversion to "
                  "ensure that all spectra in the output workspace\n"
                  "have identical bin boundaries. This option is not "
                  "recommended (see "
                  "http://www.mantidproject.org/ConvertUnits).");
}

/** This implementation does NOT stores the emode in the provided workspace
*  @param outputWS The workspace
*/
void ConvertUnitsUsingDetectorTable::storeEModeOnWorkspace(
    API::MatrixWorkspace_sptr outputWS) {
  // do nothing here - don't store this value
}

/** Convert the workspace units using TOF as an intermediate step in the
* conversion
* @param fromUnit :: The unit of the input workspace
* @param inputWS :: The input workspace
* @returns A shared pointer to the output workspace
*/
MatrixWorkspace_sptr ConvertUnitsUsingDetectorTable::convertViaTOF(
    Kernel::Unit_const_sptr fromUnit, API::MatrixWorkspace_const_sptr inputWS) {
  using namespace Geometry;

  // Let's see if we are using a TableWorkspace to override parameters
  TableWorkspace_sptr paramWS = getProperty("DetectorParameters");

  // See if we have supplied a DetectorParameters Workspace
  // TODO: Check if paramWS is NULL and if so throw an exception

  //      const std::string l1ColumnLabel("l1");

  // Let's check all the columns exist and are readable
  try {
    auto spectraColumnTmp = paramWS->getColumn("spectra");
    auto l1ColumnTmp = paramWS->getColumn("l1");
    auto l2ColumnTmp = paramWS->getColumn("l2");
    auto twoThetaColumnTmp = paramWS->getColumn("twotheta");
    auto efixedColumnTmp = paramWS->getColumn("efixed");
    auto emodeColumnTmp = paramWS->getColumn("emode");
  } catch (...) {
    throw Exception::InstrumentDefinitionError(
        "DetectorParameter TableWorkspace is not defined correctly.");
  }

  // Now let's take a reference to the vectors.
  const auto &l1Column = paramWS->getColVector<double>("l1");
  const auto &l2Column = paramWS->getColVector<double>("l2");
  const auto &twoThetaColumn = paramWS->getColVector<double>("twotheta");
  const auto &efixedColumn = paramWS->getColVector<double>("efixed");
  const auto &emodeColumn = paramWS->getColVector<int>("emode");
  auto &spectraColumn = paramWS->getColVector<int>("spectra");

  Progress prog(this, 0.2, 1.0, m_numberOfSpectra);
  int64_t numberOfSpectra_i =
      static_cast<int64_t>(m_numberOfSpectra); // cast to make openmp happy

  // Get the unit object for each workspace
  Kernel::Unit_const_sptr outputUnit = m_outputUnit;
  std::vector<double> emptyVec;
  int failedDetectorCount = 0;

  // Perform Sanity Validation before creating workspace
  size_t checkIndex = 0;
  int checkSpecNo = inputWS->getDetector(checkIndex)->getID();
  auto checkSpecIter =
      std::find(spectraColumn.begin(), spectraColumn.end(), checkSpecNo);
  if (checkSpecIter != spectraColumn.end()) {
    size_t detectorRow = std::distance(spectraColumn.begin(), checkSpecIter);
    // copy the X values for the check
    auto checkXValues = inputWS->readX(checkIndex);
    // Convert the input unit to time-of-flight
    auto checkFromUnit = std::unique_ptr<Unit>(fromUnit->clone());
    auto checkOutputUnit = std::unique_ptr<Unit>(outputUnit->clone());
    double checkdelta = 0;
    checkFromUnit->toTOF(checkXValues, emptyVec, l1Column[detectorRow],
                         l2Column[detectorRow], twoThetaColumn[detectorRow],
                         emodeColumn[detectorRow], efixedColumn[detectorRow],
                         checkdelta);
    // Convert from time-of-flight to the desired unit
    checkOutputUnit->fromTOF(checkXValues, emptyVec, l1Column[detectorRow],
                             l2Column[detectorRow], twoThetaColumn[detectorRow],
                             emodeColumn[detectorRow],
                             efixedColumn[detectorRow], checkdelta);
  }

  // create the output workspace
  MatrixWorkspace_sptr outputWS = this->setupOutputWorkspace(inputWS);
  EventWorkspace_sptr eventWS =
      boost::dynamic_pointer_cast<EventWorkspace>(outputWS);
  assert(static_cast<bool>(eventWS) == m_inputEvents); // Sanity check

  // TODO: Check why this parallel stuff breaks
  // Loop over the histograms (detector spectra)
  // PARALLEL_FOR1(outputWS)
  for (int64_t i = 0; i < numberOfSpectra_i; ++i) {

    // Lets find what row this spectrum Number appears in our detector table.

    // PARALLEL_START_INTERUPT_REGION

    std::size_t wsid = i;

    try {

      double deg2rad = M_PI / 180.;

      auto det = outputWS->getDetector(i);
      int specNo = det->getID();

      // int spectraNumber = static_cast<int>(spectraColumn->toDouble(i));
      // wsid = outputWS->getIndexFromSpectrumNumber(spectraNumber);
      g_log.debug() << "###### Spectra #" << specNo
                    << " ==> Workspace ID:" << wsid << '\n';

      // Now we need to find the row that contains this spectrum
      std::vector<int>::iterator specIter;

      specIter = std::find(spectraColumn.begin(), spectraColumn.end(), specNo);
      if (specIter != spectraColumn.end()) {
        size_t detectorRow = std::distance(spectraColumn.begin(), specIter);
        double l1 = l1Column[detectorRow];
        double l2 = l2Column[detectorRow];
        double twoTheta = twoThetaColumn[detectorRow] * deg2rad;
        double efixed = efixedColumn[detectorRow];
        int emode = emodeColumn[detectorRow];

        g_log.debug() << "specNo from detector table = "
                      << spectraColumn[detectorRow] << '\n';

        g_log.debug() << "###### Spectra #" << specNo
                      << " ==> Det Table Row:" << detectorRow << '\n';

        g_log.debug() << "\tL1=" << l1 << ",L2=" << l2 << ",TT=" << twoTheta
                      << ",EF=" << efixed << ",EM=" << emode << '\n';

        // Make local copies of the units. This allows running the loop in
        // parallel
        auto localFromUnit = std::unique_ptr<Unit>(fromUnit->clone());
        auto localOutputUnit = std::unique_ptr<Unit>(outputUnit->clone());
        /// @todo Don't yet consider hold-off (delta)
        const double delta = 0.0;
        // Convert the input unit to time-of-flight
        localFromUnit->toTOF(outputWS->dataX(wsid), emptyVec, l1, l2, twoTheta,
                             emode, efixed, delta);
        // Convert from time-of-flight to the desired unit
        localOutputUnit->fromTOF(outputWS->dataX(wsid), emptyVec, l1, l2,
                                 twoTheta, emode, efixed, delta);
        // EventWorkspace part, modifying the EventLists.
        if (m_inputEvents) {
          eventWS->getSpectrum(wsid)
              .convertUnitsViaTof(localFromUnit.get(), localOutputUnit.get());
        }

      } else {
        // Not found
        g_log.debug() << "Spectrum " << specNo << " not found!\n";
        failedDetectorCount++;
        outputWS->maskWorkspaceIndex(wsid);
      }

    } catch (Exception::NotFoundError &) {
      // Get to here if exception thrown when calculating distance to detector
      failedDetectorCount++;
      // Since you usually (always?) get to here when there's no attached
      // detectors, this call is
      // the same as just zeroing out the data (calling clearData on the
      // spectrum)
      outputWS->maskWorkspaceIndex(i);
    }

    prog.report("Convert to " + m_outputUnit->unitID());
    // PARALLEL_END_INTERUPT_REGION
  } // loop over spectra
  // PARALLEL_CHECK_INTERUPT_REGION

  if (failedDetectorCount != 0) {
    g_log.information() << "Something went wrong for " << failedDetectorCount
                        << " spectra. Masking spectrum.\n";
  }
  if (m_inputEvents)
    eventWS->clearMRU();

  return outputWS;
}

} // namespace Algorithms
} // namespace Mantid
