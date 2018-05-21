# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:48:25 2018

@author: gy17cev

Create flow direction raster using the D8 algorithm.

Input filled digital elevation model and find all coordinates and
heights for each pixel. Find the coordinates and heights for the 
neighbours of each pixel. Find the biggest height difference between
a pixel and its neighbouring pixels. Assign each pixel with a flow
direction value based on the direction of the biggest height
difference.

Args:
    inRas (raster) -- Input filled digital elevation model.
    Flow_Direction (raster) -- Output flow direction grid.
    
Returns:
    FlowDirGrid (raster) -- Flow direction grid.
"""

import csv
import random
import matplotlib
import arcpy
import numpy


# Get user to select input raster surface.
inRas = arcpy.Raster(arcpy.GetParameterAsText(0))

# Find lower left coordinate of input raster.
lowerLeft = arcpy.Point(inRas.extent.XMin, inRas.extent.YMin)

# Find cell size of input raster.
cellSize = inRas.meanCellWidth

# Convert raster to numpy array.
land = arcpy.RasterToNumPyArray(inRas)

# Get user to name output flow direction raster.
Flow_Direction = arcpy.GetParameterAsText(1)



w = len(land) - 2 # Set width to len(land) - 2.
h = len(land) - 2 # Set height to len(land) - 2.

# Create empty flow direction grid the same size as environment data.
FlowDir = [[0 for x in range(w)] for y in range(h)]



# Create lists of heights and their positions in the landscape.

heights = [] # Create empty list of land heights.
positions = [] # Create empty list of coordinates in the landscape.

for i in range(0, len(land) - 2):
    for j in range(0, len(land) - 2):
		# Append heights for each coordinate to heights list.
        heights.append(land[i][j])
		# Append coordinates to positions list.
        positions.append([i,j])
        



# Find coordinates of neighbouring pixels.

neigh = [] # Create empty list of neighbouring coordinates.

for x, y in positions:
    neighbours = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), \
                  (x, y), (x, y + 1), (x + 1, y - 1), (x + 1, y), \
				  (x + 1, y + 1)]
    neigh.append(neighbours) # Append each list of neighbours to neigh list.




# Find heights of neighbouring pixels.

neigh_heights = [] # Create empty list of heights of neighbouring pixels.

for i in range(len(neigh)):
    row = []
    for j in range(len(neigh[i])):  
        pos = land[neigh[i][j][0]][neigh[i][j][1]]
        row.append(pos) # Append each neighbouring coordinate to a list.
    neigh_heights.append(row) # Append each list to neigh_heights list.




# Find height differences between pixel and neighbours.

# Create empty list of differences between pixel and its neighbours.
height_diffs = []

for b in range (0, len(neigh)):
    row2 = []
    for c in range(0, len(neigh[b])):
        diff = neigh_heights[b][c] - heights[b]
        row2.append(diff) # Append each difference to a list.
    height_diffs.append(row2) # Append each list to height_diffs list.




# Find largest difference in cell heights and find their index(es).'

# Create empty list of maximum height differences.
big_steps = []

for i in range(0, len(neigh)):
	# Find maximum height difference (most negative number).
    big_step = min(height_diffs[i]) 
    big_steps.append(big_step) # Append maximum to big_steps list.
    
# Create empty list of index(es) of maximum height differences.
indices = []

# Find the index(es) of maximum height differences.
for i in height_diffs:
    minimum = min(i)
    index = 0
    row3 = []
    for j in i:
        if j == minimum:
			# Append maximum height difference(s) for each pixel to a list.
            row3.append(index) 
        index += 1
    indices.append(row3) # Append each list to indices list.




# Randomly select direction and assign pixel with the appropriate value.

directions = [] # Create empty directions list.

for item in indices:
	# Randomly select a neighbouring pixel for flow direction.
    big_index = random.choice(item) 
    directions.append(big_index) # Append index to directions list.


# Assign each pixel with a flow direction value.
for i in range(len(neigh)):
    if directions[i] == 0:        
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 8
        
    elif directions[i] == 1:
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 4
        
    elif directions[i] == 2:
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 2
        
    elif directions[i] == 3:
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 16
        
    elif directions[i] == 4:
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 0
        
    elif directions[i] == 5:
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 1
        
    elif directions[i] == 6:
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 32
        
    elif directions[i] == 7:
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 64
        
    elif directions[i] == 8:
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 128
        
    else:
        pass

'''   
The code below was written to attempt to get the cells to look at their
neighbouring pixels and assign the same flow direction. This was attempted to
tackle issues with the large flat areas, such as the sea, to not have
extremely complex flow direction grids, but this is yet to be perfected so is
currently not included in the code.
 
for i in range(len(neigh)):
    if neigh_heights[i][4] == neigh_heights[i][0] == neigh_heights[i][1] == \
	neigh_heights[i][2] == neigh_heights[i][3]:
        FlowDir[neigh[i][4][0]][neigh[i][4][1]] = 0
'''    
    

# Convert flow direction list into a numpy array.
FlowDirArray = numpy.array(FlowDir)

# Convert numpy array to raster.
FlowDirGrid = arcpy.NumPyArrayToRaster(FlowDirArray, lowerLeft, cellSize)

# Save the flow direction raster.
FlowDirGrid.save(Flow_Direction)
