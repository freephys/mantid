#pylint: disable=invalid-name,attribute-defined-outside-init
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jan  5 14:58:49 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from MplFigureCanvas import Qt4MplCanvas


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1332, 1259)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_logname_2 = QtGui.QLabel(self.centralwidget)
        self.label_logname_2.setMinimumSize(QtCore.QSize(40, 0))
        self.label_logname_2.setObjectName(_fromUtf8("label_logname_2"))
        self.horizontalLayout.addWidget(self.label_logname_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_browse = QtGui.QPushButton(self.centralwidget)
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.horizontalLayout.addWidget(self.pushButton_browse)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_load = QtGui.QPushButton(self.centralwidget)
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.horizontalLayout.addWidget(self.pushButton_load)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_refreshWS = QtGui.QPushButton(self.centralwidget)
        self.pushButton_refreshWS.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_refreshWS.setObjectName(_fromUtf8("pushButton_refreshWS"))
        self.horizontalLayout_2.addWidget(self.pushButton_refreshWS)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_logname = QtGui.QLabel(self.centralwidget)
        self.label_logname.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_logname.setObjectName(_fromUtf8("label_logname"))
        self.horizontalLayout_3.addWidget(self.label_logname)
        self.label_lognamevalue = QtGui.QLabel(self.centralwidget)
        self.label_lognamevalue.setObjectName(_fromUtf8("label_lognamevalue"))
        self.horizontalLayout_3.addWidget(self.label_lognamevalue)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

        # Replace 'self.graphicsView = QtGui.QtGraphicsView' with the following
        self.graphicsView = Qt4MplCanvas(self.centralwidget)
        self.mainplot = self.graphicsView.getPlot()
        self.graphicsView.setMinimumSize(QtCore.QSize(160, 160))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout_4.addWidget(self.graphicsView)

        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalSlider = QtGui.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.verticalLayout.addWidget(self.verticalSlider)
        self.verticalSlider_2 = QtGui.QSlider(self.centralwidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setTickPosition(QtGui.QSlider.TicksBelow)
        self.verticalSlider_2.setObjectName(_fromUtf8("verticalSlider_2"))
        self.verticalLayout.addWidget(self.verticalSlider_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.horizontalSlider_2 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.horizontalLayout_5.addWidget(self.horizontalSlider_2)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem10)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.pushButton_setT0 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setT0.setObjectName(_fromUtf8("pushButton_setT0"))
        self.horizontalLayout_6.addWidget(self.pushButton_setT0)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_6.addWidget(self.lineEdit_4)
        self.pushButton_setTf = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setTf.setObjectName(_fromUtf8("pushButton_setTf"))
        self.horizontalLayout_6.addWidget(self.pushButton_setTf)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_outwsname = QtGui.QLabel(self.centralwidget)
        self.label_outwsname.setObjectName(_fromUtf8("label_outwsname"))
        self.horizontalLayout_7.addWidget(self.label_outwsname)
        self.lineEdit_outwsname = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_outwsname.setObjectName(_fromUtf8("lineEdit_outwsname"))
        self.horizontalLayout_7.addWidget(self.lineEdit_outwsname)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_title = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_title.setObjectName(_fromUtf8("lineEdit_title"))
        self.horizontalLayout_7.addWidget(self.lineEdit_title)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.filterTab = QtGui.QTabWidget(self.centralwidget)
        self.filterTab.setMinimumSize(QtCore.QSize(0, 100))
        self.filterTab.setObjectName(_fromUtf8("filterTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1288, 383))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setMaximumSize(QtCore.QSize(160, 40))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        self.comboBox_2 = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_8.addWidget(self.comboBox_2)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_8.addWidget(self.pushButton_4)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_mean = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_mean.setMaximumSize(QtCore.QSize(160, 40))
        self.label_mean.setObjectName(_fromUtf8("label_mean"))
        self.horizontalLayout_9.addWidget(self.label_mean)
        self.label_meanvalue = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_meanvalue.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_meanvalue.setObjectName(_fromUtf8("label_meanvalue"))
        self.horizontalLayout_9.addWidget(self.label_meanvalue)
        self.label_avg = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_avg.setMaximumSize(QtCore.QSize(160, 40))
        self.label_avg.setObjectName(_fromUtf8("label_avg"))
        self.horizontalLayout_9.addWidget(self.label_avg)
        self.label_timeAvgValue = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_timeAvgValue.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_timeAvgValue.setObjectName(_fromUtf8("label_timeAvgValue"))
        self.horizontalLayout_9.addWidget(self.label_timeAvgValue)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_freq = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_freq.setMaximumSize(QtCore.QSize(160, 40))
        self.label_freq.setObjectName(_fromUtf8("label_freq"))
        self.horizontalLayout_10.addWidget(self.label_freq)
        self.label_freqValue = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_freqValue.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_freqValue.setObjectName(_fromUtf8("label_freqValue"))
        self.horizontalLayout_10.addWidget(self.label_freqValue)
        self.label_logsize = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_logsize.setMaximumSize(QtCore.QSize(160, 40))
        self.label_logsize.setObjectName(_fromUtf8("label_logsize"))
        self.horizontalLayout_10.addWidget(self.label_logsize)
        self.label_logsizevalue = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_logsizevalue.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_logsizevalue.setObjectName(_fromUtf8("label_logsizevalue"))
        self.horizontalLayout_10.addWidget(self.label_logsizevalue)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_11.addWidget(self.label_8)
        self.lineEdit_5 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_11.addWidget(self.lineEdit_5)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem16)
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_11.addWidget(self.label_9)
        self.lineEdit_6 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_11.addWidget(self.lineEdit_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_10 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_12.addWidget(self.label_10)
        self.lineEdit_7 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.horizontalLayout_12.addWidget(self.lineEdit_7)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem17)
        self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.comboBox_4 = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.horizontalLayout_12.addWidget(self.comboBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_19 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_13.addWidget(self.label_19)
        self.lineEdit_8 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.horizontalLayout_13.addWidget(self.lineEdit_8)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem18)
        self.label_21 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_13.addWidget(self.label_21)
        self.comboBox_5 = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.horizontalLayout_13.addWidget(self.comboBox_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_20 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_14.addWidget(self.label_20)
        self.lineEdit_9 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.horizontalLayout_14.addWidget(self.lineEdit_9)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem19)
        self.pushButton_filterLog = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_filterLog.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton_filterLog.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_filterLog.setObjectName(_fromUtf8("pushButton_filterLog"))
        self.horizontalLayout_14.addWidget(self.pushButton_filterLog)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem20)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.filterTab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_15.addWidget(self.label_6)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem21)
        self.lineEdit_timeInterval = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_timeInterval.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_timeInterval.setObjectName(_fromUtf8("lineEdit_timeInterval"))
        self.horizontalLayout_15.addWidget(self.lineEdit_timeInterval)
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem22)
        self.pushButton_filterTime = QtGui.QPushButton(self.tab_2)
        self.pushButton_filterTime.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton_filterTime.setObjectName(_fromUtf8("pushButton_filterTime"))
        self.horizontalLayout_15.addWidget(self.pushButton_filterTime)
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem23)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.filterTab.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1288, 383))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_16.addWidget(self.label_12)
        self.comboBox_tofCorr = QtGui.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_tofCorr.setObjectName(_fromUtf8("comboBox_tofCorr"))
        self.comboBox_tofCorr.addItem(_fromUtf8(""))
        self.comboBox_tofCorr.addItem(_fromUtf8(""))
        self.comboBox_tofCorr.addItem(_fromUtf8(""))
        self.comboBox_tofCorr.addItem(_fromUtf8(""))
        self.comboBox_tofCorr.addItem(_fromUtf8(""))
        self.horizontalLayout_16.addWidget(self.comboBox_tofCorr)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem24)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_Ei = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_Ei.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_Ei.setObjectName(_fromUtf8("label_Ei"))
        self.horizontalLayout_17.addWidget(self.label_Ei)
        self.lineEdit_Ei = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_Ei.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_Ei.setObjectName(_fromUtf8("lineEdit_Ei"))
        self.horizontalLayout_17.addWidget(self.lineEdit_Ei)
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem25)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_Ei_2 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_Ei_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_Ei_2.setObjectName(_fromUtf8("label_Ei_2"))
        self.horizontalLayout_18.addWidget(self.label_Ei_2)
        self.comboBox_corrWS = QtGui.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_corrWS.setObjectName(_fromUtf8("comboBox_corrWS"))
        self.horizontalLayout_18.addWidget(self.comboBox_corrWS)
        self.pushButton_refreshCorrWSList = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_refreshCorrWSList.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_refreshCorrWSList.setObjectName(_fromUtf8("pushButton_refreshCorrWSList"))
        self.horizontalLayout_18.addWidget(self.pushButton_refreshCorrWSList)
        spacerItem26 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem26)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.checkBox_fastLog = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.checkBox_fastLog.setFont(font)
        self.checkBox_fastLog.setObjectName(_fromUtf8("checkBox_fastLog"))
        self.horizontalLayout_19.addWidget(self.checkBox_fastLog)
        self.checkBox_doParallel = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_doParallel.setFont(font)
        self.checkBox_doParallel.setObjectName(_fromUtf8("checkBox_doParallel"))
        self.horizontalLayout_19.addWidget(self.checkBox_doParallel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_20.addWidget(self.label_13)
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem27)
        self.comboBox_skipSpectrum = QtGui.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_skipSpectrum.setMaximumSize(QtCore.QSize(600, 16777215))
        self.comboBox_skipSpectrum.setObjectName(_fromUtf8("comboBox_skipSpectrum"))
        self.comboBox_skipSpectrum.addItem(_fromUtf8(""))
        self.comboBox_skipSpectrum.addItem(_fromUtf8(""))
        self.horizontalLayout_20.addWidget(self.comboBox_skipSpectrum)
        spacerItem28 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem28)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.checkBox_filterByPulse = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_filterByPulse.setObjectName(_fromUtf8("checkBox_filterByPulse"))
        self.horizontalLayout_21.addWidget(self.checkBox_filterByPulse)
        self.checkBox_from1 = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_from1.setObjectName(_fromUtf8("checkBox_from1"))
        self.horizontalLayout_21.addWidget(self.checkBox_from1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.checkBox_groupWS = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_groupWS.setObjectName(_fromUtf8("checkBox_groupWS"))
        self.horizontalLayout_22.addWidget(self.checkBox_groupWS)
        self.checkBox_splitLog = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_splitLog.setObjectName(_fromUtf8("checkBox_splitLog"))
        self.horizontalLayout_22.addWidget(self.checkBox_splitLog)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.filterTab.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.filterTab)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1332, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.filterTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_logname_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>The name of the NeXus file or the run number to load</p></body></html>", None))
        self.label_logname_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Label for file name or run number</p></body></html>", None))
        self.label_logname_2.setText(_translate("MainWindow", "File / Run ", None))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>The name of the NeXus file or the run number to load. </p><p><br/></p><p>Run number should be InstrumentName_RunNumber (for example, NOM_11788)</p></body></html>", None))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_load.setText(_translate("MainWindow", "Load", None))
        self.pushButton_refreshWS.setText(_translate("MainWindow", "Refresh", None))
        self.pushButton_3.setText(_translate("MainWindow", "Use", None))
        self.label_logname.setText(_translate("MainWindow", "Log Name", None))
        self.label_lognamevalue.setText(_translate("MainWindow", "?", None))
        self.label_3.setText(_translate("MainWindow", "Starting Time", None))
        self.pushButton_setT0.setText(_translate("MainWindow", "Set", None))
        self.label_4.setText(_translate("MainWindow", "Stopping Time", None))
        self.pushButton_setTf.setText(_translate("MainWindow", "Set", None))
        self.label_outwsname.setText(_translate("MainWindow", "Output Name", None))
        self.label_5.setText(_translate("MainWindow", "Splitter Title", None))
        self.label_7.setText(_translate("MainWindow", "Sample Log", None))
        self.pushButton_4.setText(_translate("MainWindow", "Plot", None))
        self.label_mean.setText(_translate("MainWindow", "Mean", None))
        self.label_meanvalue.setText(_translate("MainWindow", "?", None))
        self.label_avg.setText(_translate("MainWindow", "Time Average", None))
        self.label_timeAvgValue.setText(_translate("MainWindow", "?", None))
        self.label_freq.setText(_translate("MainWindow", "Frequency", None))
        self.label_freqValue.setText(_translate("MainWindow", "?", None))
        self.label_logsize.setText(_translate("MainWindow", "Log Size", None))
        self.label_logsizevalue.setText(_translate("MainWindow", "?", None))
        self.label_8.setText(_translate("MainWindow", "Minimum Value", None))
        self.label_9.setText(_translate("MainWindow", "Maximum Value", None))
        self.label_10.setText(_translate("MainWindow", "Log Step Size", None))
        self.label_11.setText(_translate("MainWindow", "Value Change Direction", None))
        self.label_19.setText(_translate("MainWindow", "Log Value Tolerance", None))
        self.label_21.setText(_translate("MainWindow", "Log Boundary", None))
        self.label_20.setText(_translate("MainWindow", "Time Tolerance", None))
        self.pushButton_filterLog.setText(_translate("MainWindow", "Filter", None))
        self.filterTab.setTabText(self.filterTab.indexOf(self.tab), _translate("MainWindow", "Filter By Log", None))
        self.label_6.setText(_translate("MainWindow", "Time Interval", None))
        self.pushButton_filterTime.setText(_translate("MainWindow", "Filter", None))
        self.filterTab.setTabText(self.filterTab.indexOf(self.tab_2), _translate("MainWindow", "Filter By Time", None))
        self.label_12.setText(_translate("MainWindow", "TOF Correction To Sample", None))
        self.comboBox_tofCorr.setItemText(0, _translate("MainWindow", "None", None))
        self.comboBox_tofCorr.setItemText(1, _translate("MainWindow", "Elastic", None))
        self.comboBox_tofCorr.setItemText(2, _translate("MainWindow", "Direct", None))
        self.comboBox_tofCorr.setItemText(3, _translate("MainWindow", "Indirect", None))
        self.comboBox_tofCorr.setItemText(4, _translate("MainWindow", "Customized", None))
        self.label_Ei.setText(_translate("MainWindow", "Incident Energy", None))
        self.label_Ei_2.setText(_translate("MainWindow", "TOF Correction Workspace", None))
        self.pushButton_refreshCorrWSList.setText(_translate("MainWindow", "Refresh", None))
        self.checkBox_fastLog.setText(_translate("MainWindow", "Fast Log", None))
        self.checkBox_doParallel.setText(_translate("MainWindow", "Generate Filter In Parallel", None))
        self.label_13.setText(_translate("MainWindow", "Spectrum without Detector", None))
        self.comboBox_skipSpectrum.setItemText(0, _translate("MainWindow", "Skip", None))
        self.comboBox_skipSpectrum.setItemText(1, _translate("MainWindow", "Skip only if TOF correction", None))
        self.checkBox_filterByPulse.setText(_translate("MainWindow", "Filter By Pulse Time", None))
        self.checkBox_from1.setText(_translate("MainWindow", "Output Workspace Indexed From 1", None))
        self.checkBox_groupWS.setText(_translate("MainWindow", "Group Output Workspace", None))
        self.checkBox_splitLog.setText(_translate("MainWindow", "Split Sample Logs", None))
        self.filterTab.setTabText(self.filterTab.indexOf(self.tab_3), _translate("MainWindow", "Advanced Setup", None))

