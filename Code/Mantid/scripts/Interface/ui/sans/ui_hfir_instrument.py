# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sans/hfir_instrument.ui'
#
# Created: Wed Aug 31 10:50:50 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1026, 1152)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setFrameShape(QtGui.QFrame.NoFrame)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(Frame)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1026, 1152))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.instr_name_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instr_name_label.sizePolicy().hasHeightForWidth())
        self.instr_name_label.setSizePolicy(sizePolicy)
        self.instr_name_label.setMinimumSize(QtCore.QSize(100, 30))
        self.instr_name_label.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.instr_name_label.setFont(font)
        self.instr_name_label.setObjectName("instr_name_label")
        self.verticalLayout_4.addWidget(self.instr_name_label)
        self.reduction_options_group = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.reduction_options_group.setObjectName("reduction_options_group")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.reduction_options_group)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtGui.QLabel(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("font: italic 10pt \"Bitstream Charter\";")
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.normalization_none_radio = QtGui.QRadioButton(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.normalization_none_radio.sizePolicy().hasHeightForWidth())
        self.normalization_none_radio.setSizePolicy(sizePolicy)
        self.normalization_none_radio.setMinimumSize(QtCore.QSize(100, 0))
        self.normalization_none_radio.setMaximumSize(QtCore.QSize(100, 16777215))
        self.normalization_none_radio.setObjectName("normalization_none_radio")
        self.horizontalLayout_5.addWidget(self.normalization_none_radio)
        self.normalization_time_radio = QtGui.QRadioButton(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.normalization_time_radio.sizePolicy().hasHeightForWidth())
        self.normalization_time_radio.setSizePolicy(sizePolicy)
        self.normalization_time_radio.setMinimumSize(QtCore.QSize(100, 0))
        self.normalization_time_radio.setMaximumSize(QtCore.QSize(100, 16777215))
        self.normalization_time_radio.setObjectName("normalization_time_radio")
        self.horizontalLayout_5.addWidget(self.normalization_time_radio)
        self.normalization_monitor_radio = QtGui.QRadioButton(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.normalization_monitor_radio.sizePolicy().hasHeightForWidth())
        self.normalization_monitor_radio.setSizePolicy(sizePolicy)
        self.normalization_monitor_radio.setMinimumSize(QtCore.QSize(100, 0))
        self.normalization_monitor_radio.setMaximumSize(QtCore.QSize(100, 16777215))
        self.normalization_monitor_radio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.normalization_monitor_radio.setObjectName("normalization_monitor_radio")
        self.horizontalLayout_5.addWidget(self.normalization_monitor_radio)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.att_scale_factor_label = QtGui.QLabel(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.att_scale_factor_label.sizePolicy().hasHeightForWidth())
        self.att_scale_factor_label.setSizePolicy(sizePolicy)
        self.att_scale_factor_label.setMinimumSize(QtCore.QSize(150, 0))
        self.att_scale_factor_label.setMaximumSize(QtCore.QSize(16777215, 150))
        self.att_scale_factor_label.setObjectName("att_scale_factor_label")
        self.horizontalLayout_4.addWidget(self.att_scale_factor_label)
        self.scale_edit = QtGui.QLineEdit(self.reduction_options_group)
        self.scale_edit.setMinimumSize(QtCore.QSize(80, 0))
        self.scale_edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.scale_edit.setObjectName("scale_edit")
        self.horizontalLayout_4.addWidget(self.scale_edit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scale_chk = QtGui.QCheckBox(self.reduction_options_group)
        self.scale_chk.setObjectName("scale_chk")
        self.horizontalLayout_6.addWidget(self.scale_chk)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.direct_beam_label = QtGui.QLabel(self.reduction_options_group)
        self.direct_beam_label.setMinimumSize(QtCore.QSize(120, 0))
        self.direct_beam_label.setMaximumSize(QtCore.QSize(120, 16777215))
        self.direct_beam_label.setObjectName("direct_beam_label")
        self.horizontalLayout_10.addWidget(self.direct_beam_label)
        self.scale_data_edit = QtGui.QLineEdit(self.reduction_options_group)
        self.scale_data_edit.setMinimumSize(QtCore.QSize(300, 0))
        self.scale_data_edit.setObjectName("scale_data_edit")
        self.horizontalLayout_10.addWidget(self.scale_data_edit)
        self.scale_data_browse_button = QtGui.QPushButton(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_data_browse_button.sizePolicy().hasHeightForWidth())
        self.scale_data_browse_button.setSizePolicy(sizePolicy)
        self.scale_data_browse_button.setObjectName("scale_data_browse_button")
        self.horizontalLayout_10.addWidget(self.scale_data_browse_button)
        self.scale_data_plot_button = QtGui.QPushButton(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_data_plot_button.sizePolicy().hasHeightForWidth())
        self.scale_data_plot_button.setSizePolicy(sizePolicy)
        self.scale_data_plot_button.setObjectName("scale_data_plot_button")
        self.horizontalLayout_10.addWidget(self.scale_data_plot_button)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem4 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.beamstop_chk = QtGui.QCheckBox(self.reduction_options_group)
        self.beamstop_chk.setObjectName("beamstop_chk")
        self.horizontalLayout_11.addWidget(self.beamstop_chk)
        self.scale_beam_radius_edit = QtGui.QLineEdit(self.reduction_options_group)
        self.scale_beam_radius_edit.setMinimumSize(QtCore.QSize(80, 0))
        self.scale_beam_radius_edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.scale_beam_radius_edit.setObjectName("scale_beam_radius_edit")
        self.horizontalLayout_11.addWidget(self.scale_beam_radius_edit)
        spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.att_trans_label = QtGui.QLabel(self.reduction_options_group)
        self.att_trans_label.setObjectName("att_trans_label")
        self.horizontalLayout_11.addWidget(self.att_trans_label)
        self.scale_att_trans_edit = QtGui.QLineEdit(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_att_trans_edit.sizePolicy().hasHeightForWidth())
        self.scale_att_trans_edit.setSizePolicy(sizePolicy)
        self.scale_att_trans_edit.setMinimumSize(QtCore.QSize(80, 0))
        self.scale_att_trans_edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.scale_att_trans_edit.setObjectName("scale_att_trans_edit")
        self.horizontalLayout_11.addWidget(self.scale_att_trans_edit)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.dark_current_check = QtGui.QCheckBox(self.reduction_options_group)
        self.dark_current_check.setMinimumSize(QtCore.QSize(150, 0))
        self.dark_current_check.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dark_current_check.setObjectName("dark_current_check")
        self.horizontalLayout_7.addWidget(self.dark_current_check)
        self.dark_file_edit = QtGui.QLineEdit(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dark_file_edit.sizePolicy().hasHeightForWidth())
        self.dark_file_edit.setSizePolicy(sizePolicy)
        self.dark_file_edit.setMinimumSize(QtCore.QSize(300, 0))
        self.dark_file_edit.setBaseSize(QtCore.QSize(0, 0))
        self.dark_file_edit.setObjectName("dark_file_edit")
        self.horizontalLayout_7.addWidget(self.dark_file_edit)
        self.dark_browse_button = QtGui.QPushButton(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dark_browse_button.sizePolicy().hasHeightForWidth())
        self.dark_browse_button.setSizePolicy(sizePolicy)
        self.dark_browse_button.setObjectName("dark_browse_button")
        self.horizontalLayout_7.addWidget(self.dark_browse_button)
        self.dark_plot_button = QtGui.QPushButton(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dark_plot_button.sizePolicy().hasHeightForWidth())
        self.dark_plot_button.setSizePolicy(sizePolicy)
        self.dark_plot_button.setMinimumSize(QtCore.QSize(0, 0))
        self.dark_plot_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dark_plot_button.setObjectName("dark_plot_button")
        self.horizontalLayout_7.addWidget(self.dark_plot_button)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.solid_angle_chk = QtGui.QCheckBox(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.solid_angle_chk.sizePolicy().hasHeightForWidth())
        self.solid_angle_chk.setSizePolicy(sizePolicy)
        self.solid_angle_chk.setObjectName("solid_angle_chk")
        self.horizontalLayout_8.addWidget(self.solid_angle_chk)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtGui.QLabel(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.n_q_bins_edit = QtGui.QLineEdit(self.reduction_options_group)
        self.n_q_bins_edit.setMinimumSize(QtCore.QSize(80, 0))
        self.n_q_bins_edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.n_q_bins_edit.setObjectName("n_q_bins_edit")
        self.horizontalLayout_9.addWidget(self.n_q_bins_edit)
        self.label_3 = QtGui.QLabel(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.n_sub_pix_edit = QtGui.QLineEdit(self.reduction_options_group)
        self.n_sub_pix_edit.setMinimumSize(QtCore.QSize(80, 0))
        self.n_sub_pix_edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.n_sub_pix_edit.setObjectName("n_sub_pix_edit")
        self.horizontalLayout_9.addWidget(self.n_sub_pix_edit)
        self.log_binning_radio = QtGui.QCheckBox(self.reduction_options_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_binning_radio.sizePolicy().hasHeightForWidth())
        self.log_binning_radio.setSizePolicy(sizePolicy)
        self.log_binning_radio.setMinimumSize(QtCore.QSize(120, 0))
        self.log_binning_radio.setMaximumSize(QtCore.QSize(120, 16777215))
        self.log_binning_radio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.log_binning_radio.setObjectName("log_binning_radio")
        self.horizontalLayout_9.addWidget(self.log_binning_radio)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addWidget(self.reduction_options_group)
        self.geometry_options_groupbox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geometry_options_groupbox.sizePolicy().hasHeightForWidth())
        self.geometry_options_groupbox.setSizePolicy(sizePolicy)
        self.geometry_options_groupbox.setMinimumSize(QtCore.QSize(0, 0))
        self.geometry_options_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.geometry_options_groupbox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.geometry_options_groupbox.setObjectName("geometry_options_groupbox")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.geometry_options_groupbox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mask_template_horiz_layout = QtGui.QHBoxLayout()
        self.mask_template_horiz_layout.setSpacing(0)
        self.mask_template_horiz_layout.setObjectName("mask_template_horiz_layout")
        self.experiment_parameter_help = QtGui.QLabel(self.geometry_options_groupbox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.experiment_parameter_help.sizePolicy().hasHeightForWidth())
        self.experiment_parameter_help.setSizePolicy(sizePolicy)
        self.experiment_parameter_help.setMinimumSize(QtCore.QSize(150, 0))
        self.experiment_parameter_help.setStyleSheet("font: italic 10pt \"Bitstream Charter\";")
        self.experiment_parameter_help.setObjectName("experiment_parameter_help")
        self.mask_template_horiz_layout.addWidget(self.experiment_parameter_help)
        self.verticalLayout_5.addLayout(self.mask_template_horiz_layout)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setObjectName("formLayout_3")
        self.detector_offset_chk = QtGui.QCheckBox(self.geometry_options_groupbox)
        self.detector_offset_chk.setWhatsThis("")
        self.detector_offset_chk.setObjectName("detector_offset_chk")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.detector_offset_chk)
        self.detector_offset_edit = QtGui.QLineEdit(self.geometry_options_groupbox)
        self.detector_offset_edit.setMinimumSize(QtCore.QSize(80, 0))
        self.detector_offset_edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.detector_offset_edit.setObjectName("detector_offset_edit")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.detector_offset_edit)
        self.sample_dist_chk = QtGui.QCheckBox(self.geometry_options_groupbox)
        self.sample_dist_chk.setObjectName("sample_dist_chk")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.sample_dist_chk)
        self.sample_dist_edit = QtGui.QLineEdit(self.geometry_options_groupbox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_dist_edit.sizePolicy().hasHeightForWidth())
        self.sample_dist_edit.setSizePolicy(sizePolicy)
        self.sample_dist_edit.setMinimumSize(QtCore.QSize(80, 0))
        self.sample_dist_edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.sample_dist_edit.setObjectName("sample_dist_edit")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.sample_dist_edit)
        self.wavelength_chk = QtGui.QCheckBox(self.geometry_options_groupbox)
        self.wavelength_chk.setObjectName("wavelength_chk")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.wavelength_chk)
        self.wavelength_edit = QtGui.QLineEdit(self.geometry_options_groupbox)
        self.wavelength_edit.setMinimumSize(QtCore.QSize(80, 0))
        self.wavelength_edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.wavelength_edit.setObjectName("wavelength_edit")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.wavelength_edit)
        self.label_10 = QtGui.QLabel(self.geometry_options_groupbox)
        self.label_10.setIndent(23)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.wavelength_spread_edit = QtGui.QLineEdit(self.geometry_options_groupbox)
        self.wavelength_spread_edit.setMinimumSize(QtCore.QSize(80, 0))
        self.wavelength_spread_edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.wavelength_spread_edit.setObjectName("wavelength_spread_edit")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.wavelength_spread_edit)
        self.verticalLayout_5.addLayout(self.formLayout_3)
        self.verticalLayout_4.addWidget(self.geometry_options_groupbox)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mask_check = QtGui.QCheckBox(self.groupBox)
        self.mask_check.setMinimumSize(QtCore.QSize(150, 0))
        self.mask_check.setObjectName("mask_check")
        self.horizontalLayout.addWidget(self.mask_check)
        self.mask_edit = QtGui.QLineEdit(self.groupBox)
        self.mask_edit.setMinimumSize(QtCore.QSize(300, 0))
        self.mask_edit.setObjectName("mask_edit")
        self.horizontalLayout.addWidget(self.mask_edit)
        self.mask_browse_button = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mask_browse_button.sizePolicy().hasHeightForWidth())
        self.mask_browse_button.setSizePolicy(sizePolicy)
        self.mask_browse_button.setObjectName("mask_browse_button")
        self.horizontalLayout.addWidget(self.mask_browse_button)
        self.mask_plot_button = QtGui.QPushButton(self.groupBox)
        self.mask_plot_button.setObjectName("mask_plot_button")
        self.horizontalLayout.addWidget(self.mask_plot_button)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.instr_name_label.setText(QtGui.QApplication.translate("Frame", "BIOSANS", None, QtGui.QApplication.UnicodeUTF8))
        self.reduction_options_group.setTitle(QtGui.QApplication.translate("Frame", "Reduction Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bitstream Charter\'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For more information, go to <a style=\"text-decoration: none\" href=\"http://www.mantidproject.org/Reduction_for_HFIR_SANS\"><span style=\" color:#5555ff;\">http://www.mantidproject.org/Reduction_for_HFIR_SANS</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Frame", "Normalization", None, QtGui.QApplication.UnicodeUTF8))
        self.normalization_none_radio.setToolTip(QtGui.QApplication.translate("Frame", "Select to skip data normalization.", None, QtGui.QApplication.UnicodeUTF8))
        self.normalization_none_radio.setText(QtGui.QApplication.translate("Frame", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.normalization_time_radio.setToolTip(QtGui.QApplication.translate("Frame", "Select to normalize the data to the data collection time.", None, QtGui.QApplication.UnicodeUTF8))
        self.normalization_time_radio.setText(QtGui.QApplication.translate("Frame", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.normalization_monitor_radio.setToolTip(QtGui.QApplication.translate("Frame", "Select to normalize the data to the beam monitor count.", None, QtGui.QApplication.UnicodeUTF8))
        self.normalization_monitor_radio.setText(QtGui.QApplication.translate("Frame", "Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.att_scale_factor_label.setText(QtGui.QApplication.translate("Frame", "Absolute scale factor", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter a scaling factor to be multiplied to I(Q).", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_chk.setToolTip(QtGui.QApplication.translate("Frame", "Check to calculate the absolute scale factor using the direct beam method.", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_chk.setText(QtGui.QApplication.translate("Frame", "Calculate absolute scale factor", None, QtGui.QApplication.UnicodeUTF8))
        self.direct_beam_label.setText(QtGui.QApplication.translate("Frame", "Direct beam file", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_data_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter a valid file path for a direct beam data file.", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_data_browse_button.setToolTip(QtGui.QApplication.translate("Frame", "Click to browse.", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_data_browse_button.setText(QtGui.QApplication.translate("Frame", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_data_plot_button.setToolTip(QtGui.QApplication.translate("Frame", "Click to plot 2D data.", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_data_plot_button.setText(QtGui.QApplication.translate("Frame", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.beamstop_chk.setText(QtGui.QApplication.translate("Frame", "Beam spot diameter [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_beam_radius_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter the diameter around the beam center to include when measuring the total beam signal, in mm.", None, QtGui.QApplication.UnicodeUTF8))
        self.att_trans_label.setText(QtGui.QApplication.translate("Frame", "Attenuator Transmission", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_att_trans_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter the attenuator transmission from the Attenuator Efficiency Chart.", None, QtGui.QApplication.UnicodeUTF8))
        self.dark_current_check.setText(QtGui.QApplication.translate("Frame", "Dark current file", None, QtGui.QApplication.UnicodeUTF8))
        self.dark_file_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter a valid file path to be used for the dark current data.", None, QtGui.QApplication.UnicodeUTF8))
        self.dark_browse_button.setToolTip(QtGui.QApplication.translate("Frame", "Click to browse.", None, QtGui.QApplication.UnicodeUTF8))
        self.dark_browse_button.setText(QtGui.QApplication.translate("Frame", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.dark_plot_button.setToolTip(QtGui.QApplication.translate("Frame", "Click to plot 2D data.", None, QtGui.QApplication.UnicodeUTF8))
        self.dark_plot_button.setText(QtGui.QApplication.translate("Frame", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.solid_angle_chk.setToolTip(QtGui.QApplication.translate("Frame", "Select to perform a solid angle correction.", None, QtGui.QApplication.UnicodeUTF8))
        self.solid_angle_chk.setText(QtGui.QApplication.translate("Frame", "Perform solid angle correction", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Frame", "Radial averaging", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Frame", "Number of Q bins  ", None, QtGui.QApplication.UnicodeUTF8))
        self.n_q_bins_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter the number of Q bins for the output I(Q) distribution.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Frame", "Number of sub-pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.n_sub_pix_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter the number of sub-pixels in each direction of a detector pixel to use for the\n"
"radial averaging. For instance, entering 3 will sub-divide each detector pixel by 3\n"
"in each direction and will create 9 sub-pixels.", None, QtGui.QApplication.UnicodeUTF8))
        self.log_binning_radio.setToolTip(QtGui.QApplication.translate("Frame", "Select to use logarithmic binning for I(Q).", None, QtGui.QApplication.UnicodeUTF8))
        self.log_binning_radio.setText(QtGui.QApplication.translate("Frame", "Log binning", None, QtGui.QApplication.UnicodeUTF8))
        self.geometry_options_groupbox.setTitle(QtGui.QApplication.translate("Frame", "Experiment Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.experiment_parameter_help.setText(QtGui.QApplication.translate("Frame", "The sample-detector distance and wavelength are updated automatically when a sample data file is selected.\n"
"Values can be selected by hand by checking the boxes below.", None, QtGui.QApplication.UnicodeUTF8))
        self.detector_offset_chk.setToolTip(QtGui.QApplication.translate("Frame", "Select to set the detector distance offset.", None, QtGui.QApplication.UnicodeUTF8))
        self.detector_offset_chk.setText(QtGui.QApplication.translate("Frame", "Detector distance offset [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.detector_offset_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter the detector distance offset in mm.", None, QtGui.QApplication.UnicodeUTF8))
        self.sample_dist_chk.setToolTip(QtGui.QApplication.translate("Frame", "Select to force the sample-detector distance.", None, QtGui.QApplication.UnicodeUTF8))
        self.sample_dist_chk.setText(QtGui.QApplication.translate("Frame", "Sample-detector distance [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.sample_dist_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter the value of the sample-to-detector distance in mm.", None, QtGui.QApplication.UnicodeUTF8))
        self.wavelength_chk.setToolTip(QtGui.QApplication.translate("Frame", "Select to force the wavelength to a given value.", None, QtGui.QApplication.UnicodeUTF8))
        self.wavelength_chk.setText(QtGui.QApplication.translate("Frame", "Wavelength [Angstrom]", None, QtGui.QApplication.UnicodeUTF8))
        self.wavelength_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter the value of the neutron wavelength.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Frame", "Wavelength spread [Angstrom]", None, QtGui.QApplication.UnicodeUTF8))
        self.wavelength_spread_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter the value of the neutron wavelength spread.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Frame", "Mask", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Frame", "Choose a file to set your mask. Note that only the mask information, not the data, will be used in the reduction.\n"
"The data is only used to help you setting the mask.\n"
"The mask information is saved separately so that your data file will NOT be modified.", None, QtGui.QApplication.UnicodeUTF8))
        self.mask_check.setToolTip(QtGui.QApplication.translate("Frame", "Select to apply the mask built from the specified data file.", None, QtGui.QApplication.UnicodeUTF8))
        self.mask_check.setText(QtGui.QApplication.translate("Frame", "Mask file", None, QtGui.QApplication.UnicodeUTF8))
        self.mask_edit.setToolTip(QtGui.QApplication.translate("Frame", "Enter a file to be used to create your mask.", None, QtGui.QApplication.UnicodeUTF8))
        self.mask_browse_button.setToolTip(QtGui.QApplication.translate("Frame", "Click to browse.", None, QtGui.QApplication.UnicodeUTF8))
        self.mask_browse_button.setText(QtGui.QApplication.translate("Frame", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.mask_plot_button.setToolTip(QtGui.QApplication.translate("Frame", "Click to plot 2D data and edit mask.", None, QtGui.QApplication.UnicodeUTF8))
        self.mask_plot_button.setText(QtGui.QApplication.translate("Frame", "Edit Mask", None, QtGui.QApplication.UnicodeUTF8))

