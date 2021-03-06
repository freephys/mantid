#pylint: disable=invalid-name
"""
    Script used to start the REFL SF calculator gui from Mantidplot
"""
from __future__ import (absolute_import, division, print_function)
from reduction_application import ReductionGUI

reducer = ReductionGUI(instrument="REFLSF", instrument_list=["REFLSF"])
if reducer.setup_layout(load_last=True):
    reducer.show()
