#ifndef MANTIDQT_MANTIDWIDGETS_PROJECTSAVEMODEL_H
#define MANTIDQT_MANTIDWIDGETS_PROJECTSAVEMODEL_H

#include "MantidAPI/Workspace.h"
#include "MantidQtAPI/IProjectSerialisable.h"
#include "MantidQtAPI/pixmaps.h"

#include "WidgetDllOption.h"
#include <unordered_map>
#include <vector>

namespace MantidQt {
namespace MantidWidgets {

// POD structs to pass information to the view
//==============================================================================

struct WorkspaceInfo {
  std::string name;
  std::string type;
  std::string size;
  std::string icon_id;
  size_t numWindows;
  std::vector<WorkspaceInfo> subWorkspaces;

  bool operator==(const WorkspaceInfo &b) const { return name == b.name; }
};

struct WindowInfo {
  std::string name;
  std::string type;
  std::string icon_id;

  bool operator==(const WindowInfo &b) const { return name == b.name; }
};

// Model definition
//==============================================================================

class EXPORT_OPT_MANTIDQT_MANTIDWIDGETS ProjectSaveModel {
public:
  /// Construct a new model instance with vector of window handles
  ProjectSaveModel(std::vector<MantidQt::API::IProjectSerialisable *> windows);

  /// Check if a workspace has any windows attached to it
  bool hasWindows(const std::string &ws) const;
  /// Get all window names for a collection of workspace names
  std::vector<std::string>
  getWindowNames(const std::vector<std::string> &wsNames) const;
  /// Get all workspace names
  std::vector<std::string> getWorkspaceNames() const;
  /// Get all window information for a collection of workspaces
  std::vector<WindowInfo>
  getWindowInformation(const std::vector<std::string> &wsNames) const;
  /// Get all workspace information
  std::vector<WorkspaceInfo> getWorkspaceInformation() const;
  /// Get all window handles for this workspace
  std::vector<MantidQt::API::IProjectSerialisable *>
  getWindows(const std::string &wsName) const;
  /// Get all window handles for a collection of workspace names
  std::vector<MantidQt::API::IProjectSerialisable *>
  getUniqueWindows(const std::vector<std::string> &wsNames) const;
  /// Get all workspaces from the ADS
  std::vector<Mantid::API::Workspace_sptr> getWorkspaces() const;

private:
  /// Create a workspace info object for this workspace
  WorkspaceInfo
  makeWorkspaceInfoObject(Mantid::API::Workspace_const_sptr ws) const;

  // Instance variables

  /// Map to hold which windows are associated with a workspace
  std::unordered_map<std::string,
                     std::vector<MantidQt::API::IProjectSerialisable *>>
      m_workspaceWindows;
};

} // CustomInterfaces
} // MantidQt

#endif // MANTIDQT_MANTIDWIDGETS_PROJECTSAVEMODEL_H