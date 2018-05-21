import arcpy
import pythonaddins

class DelineateCatchment(object):
    """Implementation for hydrology_addin_addin.catchmentbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog("M:/Programming/project2/Project.tbx", "CatchmentScript")

class DetermineFlowpaths(object):
    """Implementation for hydrology_addin_addin.flowpathsbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog("M:/Programming/project2/Project.tbx", "FlowpathsScript")