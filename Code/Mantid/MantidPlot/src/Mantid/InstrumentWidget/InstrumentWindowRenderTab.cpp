#include "InstrumentWindowRenderTab.h"

#include <QMenu>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QComboBox>
#include <QCheckBox>
#include <QFileDialog>
#include <QFileInfo>
#include <QSettings>
#include <QAction>
#include <qwt_scale_widget.h>
#include <qwt_scale_engine.h>

#include "MantidKernel/ConfigService.h"
#include "InstrumentWindow.h"
#include "BinDialog.h"
#include "ColorMapWidget.h"


InstrumentWindowRenderTab::InstrumentWindowRenderTab(InstrumentWindow* instrWindow):
QFrame(instrWindow),m_instrWindow(instrWindow)
{
  m_InstrumentDisplay = m_instrWindow->getInstrumentDisplay();
  QVBoxLayout* renderControlsLayout=new QVBoxLayout(this);

  // Render Mode control
  QComboBox* renderMode = new QComboBox(this);
  renderMode->setToolTip("Set render mode");
  QStringList modeList;
  modeList << "Full 3D" << "Cylindrical X"  << "Cylindrical Y" << "Cylindrical Z" << "Spherical X" << "Spherical Y" << "Spherical Z";
  renderMode->insertItems(0,modeList);
  connect(renderMode,SIGNAL(currentIndexChanged(int)),m_instrWindow,SLOT(setSurfaceType(int)));
  connect(renderMode, SIGNAL(currentIndexChanged(int)), this, SLOT(showResetView(int)));

  // Save image control
  mSaveImage = new QPushButton(tr("Save image"));
  connect(mSaveImage, SIGNAL(clicked()), m_instrWindow, SLOT(saveImage()));

  // Setup Display Setting menu
  QPushButton* displaySettings = new QPushButton("Display Settings",this);
  QMenu* displaySettingsMenu = new QMenu(this);
  m_colorMap = new QAction("Color Map",this);
  connect(m_colorMap,SIGNAL(triggered()),this,SLOT(changeColormap()));
  m_backgroundColor = new QAction("Background Colour",this);
  connect(m_backgroundColor,SIGNAL(triggered()),m_instrWindow,SLOT(pickBackgroundColor()));
  m_lighting = new QAction("Lighting",this);
  m_lighting->setCheckable(true);
  m_lighting->setChecked(false);
  //connect(m_lighting,SIGNAL(toggled(bool)),mInstrumentDisplay,SLOT(enableLighting(bool)));
  m_displayAxes = new QAction("Display Axes",this);
  m_displayAxes->setCheckable(true);
  m_displayAxes->setChecked(true);
  connect(m_displayAxes, SIGNAL(toggled(bool)), this, SLOT(showAxes(bool)));
  m_wireframe = new QAction("Wireframe",this);
  m_wireframe->setCheckable(true);
  m_wireframe->setChecked(false);
  connect(m_wireframe, SIGNAL(toggled(bool)), m_instrWindow, SLOT(setWireframe(bool)));
  displaySettingsMenu->addAction(m_colorMap);
  displaySettingsMenu->addAction(m_backgroundColor);
  displaySettingsMenu->addSeparator();
  displaySettingsMenu->addAction(m_displayAxes);
  displaySettingsMenu->addAction(m_wireframe);
  //displaySettingsMenu->addAction(m_lighting); // enable for testing
  displaySettings->setMenu(displaySettingsMenu);

  QFrame * axisViewFrame = setupAxisFrame();

  // Colormap widget
  m_colorMapWidget = new ColorMapWidget(0,this);
  connect(m_colorMapWidget, SIGNAL(scaleTypeChanged(int)), m_instrWindow, SLOT(changeScaleType(int)));
  connect(m_colorMapWidget,SIGNAL(minValueChanged(double)),m_instrWindow, SLOT(changeColorMapMinValue(double)));
  connect(m_colorMapWidget,SIGNAL(maxValueChanged(double)),m_instrWindow, SLOT(changeColorMapMaxValue(double)));

  // layout
  renderControlsLayout->addWidget(renderMode);
  renderControlsLayout->addWidget(axisViewFrame);
  renderControlsLayout->addWidget(displaySettings);
  renderControlsLayout->addWidget(mSaveImage);
  renderControlsLayout->addWidget(m_colorMapWidget);


}

InstrumentWindowRenderTab::~InstrumentWindowRenderTab()
{
  saveSettings("Mantid/InstrumentWindow");
}

/** Sets up the controls and surrounding layout that allows uses to view the instrument
*  from an axis that they select
*  @return the QFrame that will be inserted on the main instrument view form
*/
QFrame * InstrumentWindowRenderTab::setupAxisFrame()
{
  m_resetViewFrame = new QFrame();
  QHBoxLayout* axisViewLayout = new QHBoxLayout();
  axisViewLayout->addWidget(new QLabel("Axis View:"));

  mAxisCombo = new QComboBox();
  mAxisCombo->addItem("Z+");
  mAxisCombo->addItem("Z-");
  mAxisCombo->addItem("X+");
  mAxisCombo->addItem("X-");
  mAxisCombo->addItem("Y+");
  mAxisCombo->addItem("Y-");

  axisViewLayout->addWidget(mAxisCombo);
  m_resetViewFrame->setLayout(axisViewLayout);

  connect(mAxisCombo,SIGNAL(currentIndexChanged(const QString&)),m_instrWindow,SLOT(setViewDirection(const QString&)));

  loadSettings("Mantid/InstrumentWindow");
  return m_resetViewFrame;
}

/**
 *
 */
void InstrumentWindowRenderTab::setupColorBarScaling(const MantidColorMap& cmap,double minPositive)
{
  m_colorMapWidget->setMinPositiveValue(minPositive);
  m_colorMapWidget->setupColorBarScaling(cmap);
}

/**
 * Change color map button slot. This provides the file dialog box to select colormap or sets it directly a string is provided
 */
void InstrumentWindowRenderTab::changeColormap(const QString &filename)
{
  m_instrWindow->changeColormap(filename);
}

void InstrumentWindowRenderTab::loadSettings(const QString& section)
{
  QSettings settings;
  settings.beginGroup(section);
  int show3daxes = settings.value("3DAxesShown", 1 ).toInt();
  m_instrWindow->set3DAxesState(show3daxes != 0);
  m_displayAxes->blockSignals(true);
  m_displayAxes->setChecked(show3daxes != 0);
  m_displayAxes->blockSignals(false);
  settings.endGroup();
}

void InstrumentWindowRenderTab::saveSettings(const QString& section)
{
  QSettings settings;
  settings.beginGroup(section);
  int val = 0;  if (m_displayAxes->isChecked()) val = 1;
  settings.setValue("3DAxesShown", QVariant(val));
  settings.endGroup();
}

void InstrumentWindowRenderTab::setMinValue(double value, bool apply)
{
  if (!apply) m_colorMapWidget->blockSignals(true);
  m_colorMapWidget->setMinValue(value);
  if (!apply) m_colorMapWidget->blockSignals(false);
}

void InstrumentWindowRenderTab::setMaxValue(double value, bool apply)
{
  if (!apply) m_colorMapWidget->blockSignals(true);
  m_colorMapWidget->setMaxValue(value);
  if (!apply) m_colorMapWidget->blockSignals(false);
}

GraphOptions::ScaleType InstrumentWindowRenderTab::getScaleType()const
{
  return (GraphOptions::ScaleType)m_colorMapWidget->getScaleType();
}

void InstrumentWindowRenderTab::setScaleType(GraphOptions::ScaleType type)
{
  m_colorMapWidget->setScaleType(type);
}

void InstrumentWindowRenderTab::setAxis(const QString& axisNameArg)
{
    QString axisName = axisNameArg.toUpper();
    int axisInd = mAxisCombo->findText(axisName.toUpper());
    if (axisInd < 0) axisInd = 0;
    mAxisCombo->setCurrentIndex(axisInd);
}

bool InstrumentWindowRenderTab::areAxesOn()const
{
  return m_displayAxes->isChecked();
}

/**
  * Show ResetView combo box only with 3D view
  * @param iv Index of a render mode in RenderMode combo box. iv == 0 is 3D view
  */
void InstrumentWindowRenderTab::showResetView(int iv)
{
  m_resetViewFrame->setVisible(iv == 0);
}

void InstrumentWindowRenderTab::showAxes(bool on)
{
  m_instrWindow->set3DAxesState(on);
  m_displayAxes->blockSignals(true);
  m_displayAxes->setChecked(on);
  m_displayAxes->blockSignals(false);
}
