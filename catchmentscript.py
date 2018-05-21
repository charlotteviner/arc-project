"""
@author: gy17cev

Calculate the catchment area from a specified pour point.

Args:
    Flow_acc (raster) -- Input flow accumulation raster.
	Pour_point (feature set) -- Select pour point interactively.
	Snap_dist (int) -- Snap pour point distance in map units.
	Flow_dir (raster) -- Input flow direction raster.
	Catchment (shapefile) -- Output catchment polygon.
    
Returns:
    drainage_area (double) -- Drainage area of catchment.
"""


# Import arcpy module.
import arcpy
import sys
import traceback

arcpy.env.overwriteOutput = True # Allow files to be overwritten.

# Script arguments.
Flow_acc = arcpy.GetParameterAsText(0)

Pour_point = arcpy.GetParameterAsText(1)
if Pour_point == '#' or not Pour_point:
    Pour_point = "in_memory\\{BD1F06B4-09DC-44EF-86C6-D51D03734C29}" # Provide a default value if unspecified.

Snap_dist = arcpy.GetParameterAsText(2)
if Snap_dist == '#' or not Snap_dist:
    Snap_dist = "0" # Provide a default value if unspecified.

Flow_dir = arcpy.GetParameterAsText(3)

Catchment = arcpy.GetParameterAsText(4)

# Local variables:
SnapPourPt = ".../SnapPourPt"
Output_raster = ""

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
        arcpy.Catchment_project(Flow_acc,Pour_point,Snap_dist,Flow_dir,Catchment)
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

# Calculate catchment area and add to attribute table.
# Source: https://gis.stackexchange.com/questions/90685/
arcpy.AddField_management(Catchment, "Area_sq_km", "Double")
drainage_area = "{0}".format("!SHAPE.area@SQUAREKILOMETERS!")
arcpy.CalculateField_management(Catchment, "Area_sq_km", drainage_area, "PYTHON", )
