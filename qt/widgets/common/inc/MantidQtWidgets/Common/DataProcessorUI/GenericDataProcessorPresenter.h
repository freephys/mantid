#ifndef MANTIDQTMANTIDWIDGETS_GENERICDATAPROCESSORPRESENTER_H
#define MANTIDQTMANTIDWIDGETS_GENERICDATAPROCESSORPRESENTER_H
#include "MantidAPI/IAlgorithm_fwd.h"
#include "MantidAPI/ITableWorkspace_fwd.h"
#include "MantidQtWidgets/Common/DataProcessorUI/Command.h"
#include "MantidQtWidgets/Common/DataProcessorUI/DataProcessorMainPresenter.h"
#include "MantidQtWidgets/Common/DataProcessorUI/DataProcessorPresenter.h"
#include "MantidQtWidgets/Common/DataProcessorUI/GenericDataProcessorPresenterThread.h"
#include "MantidQtWidgets/Common/DataProcessorUI/OneLevelTreeManager.h"
#include "MantidQtWidgets/Common/DataProcessorUI/OptionsMap.h"
#include "MantidQtWidgets/Common/DataProcessorUI/PostprocessingAlgorithm.h"
#include "MantidQtWidgets/Common/DataProcessorUI/PostprocessingStep.h"
#include "MantidQtWidgets/Common/DataProcessorUI/PreprocessMap.h"
#include "MantidQtWidgets/Common/DataProcessorUI/PreprocessingAlgorithm.h"
#include "MantidQtWidgets/Common/DataProcessorUI/ProcessingAlgorithm.h"
#include "MantidQtWidgets/Common/DataProcessorUI/TreeData.h"
#include "MantidQtWidgets/Common/DataProcessorUI/TwoLevelTreeManager.h"
#include "MantidQtWidgets/Common/DataProcessorUI/WhiteList.h"
#include "MantidQtWidgets/Common/DllOption.h"
#include "MantidQtWidgets/Common/ParseKeyValueString.h"
#include "MantidQtWidgets/Common/ProgressPresenter.h"
#include "MantidQtWidgets/Common/WorkspaceObserver.h"
#include <boost/optional.hpp>

#include <QSet>
#include <map>
#include <queue>

#include "MantidAPI/AnalysisDataService.h"
#include <QObject>

namespace MantidQt {
namespace MantidWidgets {
class ProgressableView;
namespace DataProcessor {
// Forward decs
class DataProcessorView;
class TreeManager;
class GenericDataProcessorPresenterThread;

using RowItem = std::pair<int, RowData>;
using RowQueue = std::queue<RowItem>;
using GroupQueue = std::queue<std::pair<int, RowQueue>>;

/** @class GenericDataProcessorPresenter

GenericDataProcessorPresenter is a presenter class for the Data Processor
Interface. It handles any interface functionality and model manipulation.

Copyright &copy; 2011-16 ISIS Rutherford Appleton Laboratory, NScD Oak Ridge
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

File change history is stored at: <https://github.com/mantidproject/mantid>.
Code Documentation is available at: <http://doxygen.mantidproject.org>
*/
struct PreprocessingAttributes {
  PreprocessingAttributes(const ColumnOptionsMap &options)
      : m_options(options) {}
  PreprocessingAttributes(const ColumnOptionsMap &options,
                          std::map<QString, PreprocessingAlgorithm> map)
      : m_options(options), m_map(map) {}
  ColumnOptionsMap m_options;
  std::map<QString, PreprocessingAlgorithm> m_map;

  bool hasPreprocessing(const QString &columnName) const {
    return m_map.count(columnName) > 0;
  }

  bool hasOptions(const QString &columnName) const {
    return m_options.count(columnName) > 0;
  }

  // IAlgorithm_sptr createAlgorithmFor(const QString& columnName) const {
  //     assert(hasPreprocessing(columnName));
  //     const auto& preprocessor = m_map[columnName];
  //
  // }
};

class EXPORT_OPT_MANTIDQT_COMMON GenericDataProcessorPresenter
    : public QObject,
      public DataProcessorPresenter,
      public MantidQt::API::WorkspaceObserver {
  // Q_OBJECT for 'connect' with thread/worker
  Q_OBJECT

  friend class GenericDataProcessorPresenterRowReducerWorker;
  friend class GenericDataProcessorPresenterGroupReducerWorker;

public:
  // Constructor: pre-processing and post-processing
  GenericDataProcessorPresenter(
      WhiteList whitelist,
      std::map<QString, PreprocessingAlgorithm> preprocessMap,
      ProcessingAlgorithm processor, PostprocessingAlgorithm postprocessor,
      int group,
      std::map<QString, QString> postprocessMap = std::map<QString, QString>(),
      QString loader = "Load");
  // Constructor: no pre-processing, post-processing
  GenericDataProcessorPresenter(WhiteList whitelist,
                                ProcessingAlgorithm processor,
                                PostprocessingAlgorithm postprocessor,
                                int group);
  // Constructor: pre-processing, no post-processing
  GenericDataProcessorPresenter(
      WhiteList whitelist,
      std::map<QString, PreprocessingAlgorithm> preprocessMap,
      ProcessingAlgorithm processor, int group);
  // Constructor: no pre-processing, no post-processing
  GenericDataProcessorPresenter(WhiteList whitelist,
                                ProcessingAlgorithm processor, int group);
  // Constructor: only whitelist
  GenericDataProcessorPresenter(WhiteList whitelist, int group);
  // Delegating constructor: pre-processing, no post-processing
  GenericDataProcessorPresenter(WhiteList whitelist,
                                PreprocessMap preprocessMap,
                                ProcessingAlgorithm processor, int group);
  // Delegating Constructor: pre-processing and post-processing
  GenericDataProcessorPresenter(WhiteList whitelist,
                                PreprocessMap preprocessMap,
                                ProcessingAlgorithm processor,
                                PostprocessingAlgorithm postprocessor,
                                int group);
  virtual ~GenericDataProcessorPresenter() override;
  void notify(DataProcessorPresenter::Flag flag) override;
  const std::map<QString, QVariant> &options() const override;
  void setOptions(const std::map<QString, QVariant> &options) override;
  void transfer(const std::vector<std::map<QString, QString>> &runs) override;
  void setInstrumentList(const QStringList &instruments,
                         const QString &defaultInstrument) override;
  std::vector<std::unique_ptr<Command>> publishCommands() override;
  void acceptViews(DataProcessorView *tableView,
                   ProgressableView *progressView) override;
  void accept(DataProcessorMainPresenter *mainPresenter) override;
  void setModel(QString const &name) override;
  bool hasPostprocessing() const;

  void settingsChanged() override;

  // The following methods are public only for testing purposes
  // Get the whitelist
  WhiteList getWhiteList() const { return m_whitelist; };
  // Get the name of the reduced workspace for a given row
  QString getReducedWorkspaceName(const QStringList &data,
                                  const QString &prefix = "") const;

  ParentItems selectedParents() const override;
  ChildItems selectedChildren() const override;
  bool askUserYesNo(const QString &prompt, const QString &title) const override;
  void giveUserWarning(const QString &prompt,
                       const QString &title) const override;
  bool isProcessing() const override;
  void setForcedReProcessing(bool forceReProcessing) override;

  void skipProcessing() override;

protected:
  template <typename T> using QOrderedSet = QMap<T, std::nullptr_t>;
  // The table view we're managing
  DataProcessorView *m_view;
  // The progress view
  ProgressableView *m_progressView;
  // A workspace receiver we want to notify
  DataProcessorMainPresenter *m_mainPresenter;
  // The tree manager, a proxy class to retrieve data from the model
  std::unique_ptr<TreeManager> m_manager;
  // Loader
  QString m_loader;
  // The list of selected items to reduce
  TreeData m_selectedData;

  boost::optional<PostprocessingStep> m_postprocessing;

  // Pre-processing options
  PreprocessingAttributes m_preprocessing;
  // Data processor options
  OptionsMap m_processingOptions;
  void updateProcessedStatus(const std::pair<int, GroupData> &group);
  // Post-process some rows
  void postProcessGroup(const GroupData &data);
  // Preprocess the given column value if applicable
  void preprocessColumnValue(const QString &columnName, QString &columnValue,
                             RowData *data);
  // Preprocess all option values where applicable
  void preprocessOptionValues(OptionsMap &options, RowData *data);
  // Update the model with results from the algorithm
  void updateModelFromAlgorithm(Mantid::API::IAlgorithm_sptr alg,
                                RowData *data);
  // Create and execute the algorithm with the given properties
  Mantid::API::IAlgorithm_sptr createAndRunAlgorithm(const OptionsMap &options);
  // Reduce a row
  void reduceRow(RowData *data);
  // Finds a run in the AnalysisDataService
  QString findRunInADS(const QString &run, const QString &prefix,
                       bool &runFound);
  // Sets whether to prompt user when getting selected runs
  void setPromptUser(bool allowPrompt);

  // Process selected rows
  virtual void process();
  // Plotting
  virtual void plotRow();
  virtual void plotGroup();
  void plotWorkspaces(const QOrderedSet<QString> &workspaces);
  // Get the name of a post-processed workspace
  QString getPostprocessedWorkspaceName(const GroupData &groupData);
  bool rowOutputExists(RowItem const &row) const;
  // Refl GUI Group.
  int m_group;
protected slots:
  void reductionError(QString ex);
  void threadFinished(const int exitCode);
  void issueNotFoundWarning(QString const &granule,
                            QSet<QString> const &missingWorkspaces);

private:
  void applyDefaultOptions(std::map<QString, QVariant> &options);
  void setPropertiesFromKeyValueString(Mantid::API::IAlgorithm_sptr alg,
                                       const std::string &hiddenOptions,
                                       const std::string &columnName);
  Mantid::API::IAlgorithm_sptr createProcessingAlgorithm() const;
  // the name of the workspace/table/model in the ADS, blank if unsaved
  QString m_wsName;
  // The whitelist
  WhiteList m_whitelist;
  // The data processor algorithm
  ProcessingAlgorithm m_processor;

  // The current queue of groups to be reduced
  GroupQueue m_group_queue;
  // The current group we are reducing row data for
  GroupData m_groupData;
  // The current row item being reduced
  RowItem m_rowItem;
  // The progress reporter
  ProgressPresenter *m_progressReporter;
  // A boolean indicating whether to prompt the user when getting selected runs
  bool m_promptUser;
  // stores whether or not the table has changed since it was last saved
  bool m_tableDirty;
  // stores the user options for the presenter
  std::map<QString, QVariant> m_options;
  // Thread to run reducer worker in
  std::unique_ptr<GenericDataProcessorPresenterThread> m_workerThread;
  // A boolean that can be set to pause reduction of the current item
  bool m_pauseReduction;
  // A boolean indicating whether data reduction is confirmed paused
  bool m_reductionPaused;
  // Enumeration of the reduction actions that can be taken
  enum class ReductionFlag { ReduceRowFlag, ReduceGroupFlag, StopReduceFlag };
  // A flag of the next action due to be carried out
  ReductionFlag m_nextActionFlag;
  // load a run into the ADS, or re-use one in the ADS if possible
  Mantid::API::Workspace_sptr
  getRun(const QString &run, const QString &instrument, const QString &prefix);
  // Loads a run from disk
  QString loadRun(const QString &run, const QString &instrument,
                  const QString &prefix, const QString &loader, bool &runFound);
  // prepare a run or list of runs for processing
  Mantid::API::Workspace_sptr
  prepareRunWorkspace(const QString &run, const PreprocessingAlgorithm &alg,
                      const OptionsMap &optionsMap);
  // add row(s) to the model
  void appendRow();
  // add group(s) to the model
  void appendGroup();
  // delete row(s) from the model
  void deleteRow();
  // delete group(s) from the model
  void deleteGroup();
  // clear selected row(s) in the model
  void clearSelected();
  // copy selected rows to clipboard
  void copySelected();
  // copy selected rows to clipboard and then delete them
  void cutSelected();
  // paste clipboard into selected rows
  void pasteSelected();
  // group selected rows together
  void groupRows();
  // expand selection to group
  void expandSelection();
  // expand all groups
  void expandAll();
  // close all groups
  void collapseAll();
  // select all rows / groups
  void selectAll();
  // table io methods
  void newTable();
  void openTable();
  void saveTable();
  void saveTableAs();
  void importTable();
  void exportTable();

  // options
  void showOptionsDialog();
  void initOptions();

  // actions/commands
  void addCommands();

  // decide between processing next row or group
  void doNextAction();

  // process next row/group
  void nextRow();
  void nextGroup();

  // start thread for performing reduction on current row/group asynchronously
  virtual void startAsyncRowReduceThread(RowItem *rowItem, int groupIndex);
  virtual void startAsyncGroupReduceThread(GroupData &groupData,
                                           int groupIndex);

  // end reduction
  void endReduction();

  // pause/resume reduction
  void pause();
  void resume();
  void updateWidgetEnabledState(const bool isProcessing) const;

  // Check if run has been processed
  bool isProcessed(int position) const;
  bool isProcessed(int position, int parent) const;
  bool m_forceProcessing = false;
  bool m_skipProcessing = false;

  // List of workspaces the user can open
  QSet<QString> m_workspaceList;

  void addHandle(const std::string &name,
                 Mantid::API::Workspace_sptr workspace) override;
  void postDeleteHandle(const std::string &name) override;
  void clearADSHandle() override;
  void renameHandle(const std::string &oldName,
                    const std::string &newName) override;
  void afterReplaceHandle(const std::string &name,
                          Mantid::API::Workspace_sptr workspace) override;
  void saveNotebook(const TreeData &data);
  std::vector<std::unique_ptr<Command>> getTableList();

  // set/get values in the table
  void setCell(int row, int column, int parentRow, int parentColumn,
               const std::string &value) override;
  std::string getCell(int row, int column, int parentRow,
                      int parentColumn) override;
  int getNumberOfRows() override;
  void clearTable() override;
};
}
}
}
#endif /*MANTIDQTMANTIDWIDGETS_GENERICDATAPROCESSORPRESENTER_H*/
