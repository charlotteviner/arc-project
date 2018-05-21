# Advanced Programming Project

This project aimed to create a new hydrology toolbar for ArcGIS which contained a simplified model for delineating catchments and calculating drainage areas. Another aim of the project was to provide the user with the option for alternative flow direction algorithms to be run within the model.

## Components of the Project

### Add-In Toolbar

The toolbar contains two buttons which each contain models created in ModeBuilder. These models were exported to Python scripts and some additional features were added.

#### 1 Determine Flowpaths

The 'Determine Flowpaths' button is the first in the two-step process to delineate a catchment. This script produces both a flow direction raster and a flow accumulation raster from a filled digital elevation model. An optional drop raster can also be created, and the option to apply a weight raster during calculation of flow accumulation is provided.

#### 2 Delineate Catchment

The 'Delineate Catchment' button delineates a catchment from an interactively selected pour point. Multiple pour points can be selected if multiple catchment delineation is desired. Additional code was added to the script which calculates the area (in square kilometres) of each catchment polygon produced, and this is added to the attribute table(s) of the catchment(s).

##### Interactive Selection of Pour Points

To select the pour point location(s) when using the 'Delineate Catchment' script, simply click in the map window on a pixel of high flow accumulation that defines the outlet point of the catchment.

### Flow Direction Script

The 'Flow Direction' script is a hand-coded version of the D8 flow direction algorithm (O'Callaghan and Mark, 1984). It is designed to assign values to cells using the same system that is used by the Arc 'Flow Direction' tool found in the Hydrology toolset of Spatial Analyst. This script produces a flow direction raster.

Originally, this script was going to contain an alternative flow direction algorithm, such as the Rho-8 (Fairfield and Leymarie, 1991) or D-infinity (Tarboton, 1997) algorithm, but these have yet to be developed.

## Instructions for Use

### Adding the Project Toolbox to ArcMap

1.	Open ArcToolbox.
2.	Right-click on ‘ArcToolbox’ at the top of the window and select ‘Add Toolbox…’.
3.	Navigate to the toolbox in the ‘arc_project’ folder and open it. The Project toolbox should now appear in the toolbox list.

#### Selecting the Location of the Scripts

For reasons unknown, the toolbox is not correctly locating the scripts to run the models in ArcMap. To resolve this issue, do the following steps:
1.	Open the Project toolbox in ArcToolbox.
2.	Right-click on ‘Determine Flowpaths’ and select ‘Properties…’.
3.	Select the ‘Source’ tab.
4.	Click on the folder icon and locate the ‘flowpathsscript.py’ file in the ‘arc_project’ folder.
5.	Select this file and click ‘Open’.
6.	Click ‘Apply’ and then ‘OK’.
7.	Repeat Steps 2-6 for ‘Delineate Catchment’ and select the ‘catchmentscript.py’ file.
8.	Repeat Steps 2-6 for ‘Flow Direction’ and select the ‘flowdirectionscript.py’ file.

#### Modifying the File Pathname for the Project Toolbox in the Scripts

In the ‘Determine Flowpaths’ and ‘Delineate Catchment’ scripts, the toolbox location needs to be entered to the script. An attempt was made to make this file path relative, but this was unsuccessful so has not yet been implemented to the scripts. To modify the file pathname, do the following steps:
1.	Open the Project toolbox in ArcToolbox.
2.	Right-click on ‘Determine Flowpaths’ and select ‘Edit…’.
3.	Find the line in the script that is currently written as:
    ```
    arcpy.ImportToolbox(“M:/Programming/project2/Project.tbx”, “project”)
    ```
4.	Edit the file pathname to the location of the Project toolbox on your computer.
5.	Click ‘File’ then ‘Save’.
6.	Close the window.
7.	Repeat Steps 2-6 for ‘Delineate Catchment’. 

### Installing the Add-In Toolbar

1.	In the zip-folder ‘arc_project’, locate the folder ‘hydrology_addin’, open it, and double-click on the ‘hydrology_addin.esriaddin’ file.
2.	Click ‘Install Add-In’ at the bottom of the Esri ArcGIS Add-In Installation Utility window.
3.	Click ‘Ok’.
4.	Relaunch ArcMap. The toolbar should now appear in the map window.
Note: If the scripts have been edited to contain the correct file pathname for the Project toolbox, the add-in should be able to run without adding the Project toolbox to ArcToolbox.

## Known Issues Which Need Resolving

All the issues listed below are still being resolved.

* The add-in toolbar does not always work when installed on different computers. Sometimes, the buttons in the toolbar just appear with a '[Missing]' alert, but the cause of this issue is unknown.
* The arcpy.overwriteOutput function does not consistently work.
* The algorithm in the 'Flow Direction' script is far from perfect and it not currently suitable for use in subsequent hydrological analysis. Issues include incorrect assignment of values and outputs with very large file sizes.

## References

Fairfield, J. and Leymarie, P. 1991. Drainage Networks From Grid Digital Elevation Models. *Water Resources Research.* **27**(5), pp.709-717.

O'Callaghan, J. F. and Mark, D. M. 1984. The Extraction of Drainage Networks from Digital Elevation Data. *Computer Vision, Graphics, and Image Processing.* **28**, pp.323-344.

Tarboton, D. G. 1997. A new method for determination of flow directions and upslope areas in grid digital elevation models. *Water Resources Research.* **33**(2), pp.309-319.
