"""
@author: gy17cev

Calculate flow direction and accumulation for a landscape.

Args:
    DEM (raster) -- Input digital elevation model.
	Flow_dir (raster) -- Output flow direction raster.
	Drop_rast (raster) -- Output drop raster.
	Weight_rast (raster) -- Input weight layer.
	Flow_acc (raster) -- Output flow accumulation raster.
"""

# Import arcpy module.
import arcpy
import sys
import traceback

arcpy.env.overwriteOutput = True # Allow files to be overwritten.

# Script arguments.
DEM = arcpy.GetParameterAsText(0)

Flow_dir = arcpy.GetParameterAsText(1)

Drop_rast = arcpy.GetParameterAsText(2)

Weight_rast = arcpy.GetParameterAsText(3)

Flow_acc = arcpy.GetParameterAsText(4)

# Local variables:
DEM_Filled = ".../DEM_Filled.tif"

try:

    try:
        arcpy.ImportToolbox("M:/Programming/project2/Project.tbx", "project") # Change file path to location of Project toolbox.
    except arcpy.ExecuteError as e:
        print("Import toolbox error", e)
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        print(tbinfo)
        arcpy.AddError(tbinfo)
        
    try:
        arcpy.Flowpaths_project(DEM,Flow_dir,Drop_rast,Weight_rast,Flow_acc)
    except arcpy.ExecuteError as e:
        print("Model run error", e)
        tb2 = sys.exc_info()[2]
        tb2info = traceback.format_tb(tb2)[0]
        print(tb2info)
        arcpy.AddError(tb2info)
        
except Exception as e:
    print(e)
    tb3 = sys.exc_info()[2]
    tb3info = traceback.format_tb(tb3)[0]
    print(tb3info)
    arcpy.AddError(tb3info)
