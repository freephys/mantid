"""
    Classes for each reduction step. Those are kept separately
    from the the interface class so that the HFIRReduction class could
    be used independently of the interface implementation
"""
from __future__ import (absolute_import, division, print_function)
import xml.dom.minidom
from reduction_gui.reduction.scripter import BaseScriptElement
from reduction_gui.reduction.reflectometer.refl_sf_calculator_data_script import DataSets as REFLDataSets


class DataSeries(BaseScriptElement):

    data_sets = []

    def __init__(self, data_class=REFLDataSets):
        super(DataSeries, self).__init__()
        self._data_class = data_class
        self.reset()

    def to_script(self):
        """
            Generate reduction script
            @param execute: if true, the script will be executed
        """
        script = ""
        for item in self.data_sets:
            script += item.to_script()
            script += "\n"

        return script

    def update(self):
        """
            Update transmission from reduction output
        """
        pass

    def to_xml(self):
        """
            Create XML from the current data.
        """

        xml  = "<DataSeries>\n"
        for item in self.data_sets:
            xml += item.to_xml()
        xml += "</DataSeries>\n"

        return xml

    def from_xml(self, xml_str):
        """
            Read in data from XML
            @param xml_str: text to read the data from
        """
        self.reset()
        self.data_sets = []
        dom = xml.dom.minidom.parseString(xml_str)

#        # Get Mantid version
#        mtd_version = BaseScriptElement.getMantidBuildVersion(dom)

        self._data_class = REFLDataSets
        element_list = dom.getElementsByTagName("Data")
        if len(element_list)==0:
            element_list = dom.getElementsByTagName("RefLSFCalculator")

        if len(element_list)>0:
            for item in element_list:
                if item is not None:
                    data_set = self._data_class()
                    data_set.from_xml_element(item)
                    self.data_sets.append(data_set)

        if len(self.data_sets)==0:
            self.data_sets = [self._data_class()]

    def reset(self):
        """
            Reset state
        """
        self.data_sets = [self._data_class()]
