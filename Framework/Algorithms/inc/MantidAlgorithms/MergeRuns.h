#ifndef MANTID_ALGORITHMS_MERGERUNS_H_
#define MANTID_ALGORITHMS_MERGERUNS_H_

#include <MantidAPI/MatrixWorkspace.h>
#include "MantidAPI/MultiPeriodGroupAlgorithm.h"
#include "MantidAPI/WorkspaceHistory.h"
#include "MantidDataObjects/EventWorkspace.h"
#include "MantidGeometry/Instrument/DetectorInfo.h"
#include "MantidKernel/System.h"

namespace Mantid {
namespace API {
class WorkspaceGroup;
}
namespace HistogramData {
class HistogramX;
}
namespace Algorithms {
/** Combines the data contained in an arbitrary number of input workspaces.
    If the input workspaces do not have common binning, the bins in the output
   workspace
    will cover the entire range of all the input workspaces, with the largest
   bin widths
    used in areas of overlap.
    The input workspaces must contain histogram data with the same number of
   spectra,
    units and instrument name in order for the algorithm to succeed.
    Other than this it is currently left to the user to ensure that the
   combination of the
    workspaces is a valid operation.

    Required Properties:
    <UL>
    <LI> InputWorkspaces  - The names of the input workspace as a comma
   separated list. </LI>
    <LI> OutputWorkspace - The name of the output workspace which will contain
   the combined inputs. </LI>
    </UL>

    @author Russell Taylor, Tessella Support Services plc
    @date 22/09/2008

    Copyright &copy; 2008-9 ISIS Rutherford Appleton Laboratory, NScD Oak Ridge
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

class DLLExport MergeRuns : public API::MultiPeriodGroupAlgorithm {
public:
  /// Algorithm's name for identification overriding a virtual method
  const std::string name() const override { return "MergeRuns"; }
  /// Summary of algorithms purpose
  const std::string summary() const override {
    return "Combines the data contained in an arbitrary number of input "
           "workspaces.";
  }

  /// Algorithm's version for identification overriding a virtual method
  int version() const override { return 1; }
  /// Algorithm's category for identification overriding a virtual method
  const std::string category() const override { return "Transforms\\Merging"; }
  // Overriden MultiPeriodGroupAlgorithm method.
  bool useCustomInputPropertyName() const override;

protected:
  /// Overriden fillHistory method to correctly store history from merged
  /// workspaces
  void fillHistory() override;

private:
  // Overridden Algorithm methods
  void init() override;
  void exec() override;
  void execEvent();
  void buildAdditionTables();
  // Overriden MultiPeriodGroupAlgorithm method.
  std::string fetchInputPropertyName() const override;

  /// An addition table is a list of pairs: First int = workspace index in the
  /// EW being added, Second int = workspace index to which it will be added in
  /// the OUTPUT EW. -1 if it should add a new entry at the end.
  typedef std::vector<std::pair<int, int>> AdditionTable;
  /// Copy the history from the input workspaces to the output workspaces
  template <typename Container>
  void copyHistoryFromInputWorkspaces(const Container &workspaces) {
    API::Workspace_sptr outWS = this->getProperty("OutputWorkspace");

    // this is not a child algorithm. Add the history algorithm to the
    // WorkspaceHistory object.
    if (!isChild()) {
      // Loop over the input workspaces, making the call that copies their
      // history to the output ones
      // (Protection against copy to self is in
      // WorkspaceHistory::copyAlgorithmHistory)
      for (auto inWS = workspaces.begin(); inWS != workspaces.end(); ++inWS) {
        outWS->history().addHistory((*inWS)->getHistory());
      }
      // Add the history for the current algorithm to all the output workspaces
      outWS->history().addHistory(m_history);
    }
    // this is a child algorithm, but we still want to keep the history.
    else if (isRecordingHistoryForChild() && m_parentHistory) {
      m_parentHistory->addChildHistory(m_history);
    }
  }

  // Methods called by exec()
  using Mantid::API::Algorithm::validateInputs;
  bool validateInputsForEventWorkspaces(
      const std::vector<std::string> &inputWorkspaces);
  void calculateRebinParams(const API::MatrixWorkspace_const_sptr &ws1,
                            const API::MatrixWorkspace_const_sptr &ws2,
                            std::vector<double> &params) const;
  void noOverlapParams(const HistogramData::HistogramX &X1,
                       const HistogramData::HistogramX &X2,
                       std::vector<double> &params) const;
  void intersectionParams(const HistogramData::HistogramX &X1, int64_t &i,
                          const HistogramData::HistogramX &X2,
                          std::vector<double> &params) const;
  void inclusionParams(const HistogramData::HistogramX &X1, int64_t &i,
                       const HistogramData::HistogramX &X2,
                       std::vector<double> &params) const;
  API::MatrixWorkspace_sptr
  rebinInput(const API::MatrixWorkspace_sptr &workspace,
             const std::vector<double> &params);
  API::MatrixWorkspace_sptr
  buildScanningOutputWorkspace(const API::MatrixWorkspace_sptr &outWS,
                               const API::MatrixWorkspace_sptr &addee);
  /// Progress reporting
  std::unique_ptr<API::Progress> m_progress;

  /// List of input EVENT workspaces
  std::vector<Mantid::DataObjects::EventWorkspace_sptr> m_inEventWS;
  /// List of input matrix workspace
  std::list<API::MatrixWorkspace_sptr> m_inMatrixWS;
  /// Addition tables for event workspaces
  std::vector<AdditionTable> m_tables;
  /// Total number of histograms in the output workspace
  size_t m_outputSize = 0;

  std::vector<SpectrumDefinition>
  buildScanIntervals(const std::vector<SpectrumDefinition> &addeeSpecDefs,
                     const Geometry::DetectorInfo &addeeDetInfo,
                     const Geometry::DetectorInfo &outDetInfo,
                     const Geometry::DetectorInfo &newOutDetInfo);
};

} // namespace Algorithm
} // namespace Mantid

#endif /* MANTID_ALGORITHMS_MERGERUNS_H_ */
