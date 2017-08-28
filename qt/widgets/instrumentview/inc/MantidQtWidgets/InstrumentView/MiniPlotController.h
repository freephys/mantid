#ifndef MANTIDQT_WIDGETS_INSTRUMENTVIEW_MINIPLOTCONTROLLER_H
#define MANTIDQT_WIDGETS_INSTRUMENTVIEW_MINIPLOTCONTROLLER_H
/*
 Copyright &copy; 2017 ISIS Rutherford Appleton Laboratory, NScD Oak Ridge
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
*/
#include <QObject>

class QAction;
class QActionGroup;
class QContextMenuEvent;
class QSettings;
class QSignalMapper;

namespace Mantid {
namespace Kernel {
class V3D;
}
namespace Geometry {
class ICompAssembly;
}
}

namespace MantidQt {
namespace MantidWidgets {
class InstrumentActor;
class InstrumentWidget;
class MiniPlot;
class MiniPlotCurveData;

/**
 * A controller class that contains logic to display the miniplot
 */
class MiniPlotController : public QObject {
  Q_OBJECT

public:
  enum class PlotType { Single = 0, DetectorSum, TubeSum, TubeIntegral };
  enum class TubeXUnits : int {
    DETECTOR_ID = 0,
    LENGTH,
    PHI,
    OUT_OF_PLANE_ANGLE,
    NUMBER_OF_UNITS
  };

  MiniPlotController(InstrumentWidget *instrWidget, MiniPlot *miniplot);
  void loadSettings(const QSettings &settings);
  void saveSettings(QSettings &settings) const;
  void setEnabled(bool on) { m_enabled = on; }
  void setPlotData(size_t pickID);
  void setPlotData(QList<int> detIDs);
  void setPlotType(PlotType type);
  void setTubeXUnits(TubeXUnits units) { m_tubeXUnits = units; }
  void updatePlot();
  void clear();
  void savePlotToWorkspace();

  PlotType getPlotType() { return m_plotType; }
  TubeXUnits getTubeXUnits() { return m_tubeXUnits; }
  QString getTubeXUnitsName() const;
  QString getTubeXUnitsUnits() const;
  QString getPlotCaption() const;

public slots:
  void showContextMenu(QContextMenuEvent *evt);

signals:
  void plotTypeChanged(QString title);

private slots:
  void sumDetectors();
  void integrateTimeBins();
  void setYScaleLinear();
  void setYScaleLog();
  void setTubeXUnits(int unit);
  void removeCurve(const QString & label);
  void addPeak(double x, double y);

private:
  void initActions();

  void plotSingle(int detid);
  void plotTube(int detid);
  void plotTubeSums(int detid, const InstrumentActor &instrumentActor,
                    const Mantid::Geometry::ICompAssembly &assembly);
  void plotTubeIntegrals(int detid, const InstrumentActor &instrumentActor,
                         const Mantid::Geometry::ICompAssembly &assembly);
  MiniPlotCurveData prepareDataForSinglePlot(int detid,
                                             bool includeErrors = false);
  MiniPlotCurveData
  prepareDataForSumsPlot(int detid, const InstrumentActor &instrumentActor,
                         const Mantid::Geometry::ICompAssembly &assembly);
  MiniPlotCurveData
  prepareDataForIntegralsPlot(int detid, const InstrumentActor &instrumentActor,
                              const Mantid::Geometry::ICompAssembly &assembly);
  static double getOutOfPlaneAngle(const Mantid::Kernel::V3D &pos,
                                   const Mantid::Kernel::V3D &origin,
                                   const Mantid::Kernel::V3D &normal);

  InstrumentWidget *m_instrWidget;
  MiniPlot *m_miniplot;

  PlotType m_plotType;
  bool m_enabled;
  /// quantity the time bin integrals to be plotted against
  TubeXUnits m_tubeXUnits;
  int m_currentDetID;

  // actions
  QAction *m_sumDetectors;
  QAction *m_integrateTimeBins;
  QActionGroup *m_summationType;
  QAction *m_linearY;
  QAction *m_logY;
  QActionGroup *m_yScaleActions;
  QAction *m_detidUnits, *m_lengthUnits, *m_phiUnits, *m_outOfPlaneAngleUnits;
  QActionGroup *m_unitsGroup;
  QSignalMapper *m_unitsMapper;
};
}
}

#endif // MANTIDQT_WIDGETS_INSTRUMENTVIEW_MINIPLOTCONTROLLER_H