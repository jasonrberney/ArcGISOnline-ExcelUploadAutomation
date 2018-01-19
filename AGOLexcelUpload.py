"""
Title: Uploading Excel Spreadsheet to ArcGIS Online
By: Jason Berney
"""

import openpyxl
import os
import Tkinter, tkFileDialog, re
import arcpy
from ExcelVerify import analyzeWB
from ZippingSHP import zipShapefile
from AddItem import addItem
from arcpy import env
arcpy.env.overwriteOutput = True
# Enter a Workspace
env.workspace = "C:/"
workspace = env.workspace

#Select an Excel spreadsheet to upload to your ArcGIS Online account
excel_input = tkFileDialog.askopenfilename(title='Select File to Analyze')
excel_inputSplit = excel_input.split('/')
excel_inputSplit2 = excel_inputSplit[-1]
excel_inputSplit3 = excel_inputSplit2.split('.')
extension = excel_inputSplit3[1]

# check the Excel extension to make sure that the user selects the correct format
if str(extension) == "xls":
    sys.exit("Oops you tried to upload an Microsoft Excel 97-2003 Worksheet (.xls), this program only supports Microsoft Excel 2007 and later (.xlsx). Please save your document in a more modern format.")
elif str(extension) == "xlsx":
    # analyze the excel spreadsheet to make sure it is properly formatted
    analyzeWB(excel_inputSplit2)
else:
    sys.exit("You did not select an Excel spreadsheet, please try again.")

# extract a general name that can be applied to the files as they're converted
generalNameUse = excel_inputSplit3[0]
print generalNameUse
file_output = excel_inputSplit3[0] + ".dbf"
# convert the Excel spreadsheet to a ArcGIS DBF table
arcpy.ExcelToTable_conversion(excel_inputSplit2, file_output)

# if the Excel to Table conversion was successful, create a shapefile
if file_output is not None:
    try:
        # Set the local variables
        in_Table = file_output
        x_coords = "Lng"
        y_coords = "Lat"
        out_Layer = "{0}_layer".format(generalNameUse)
        saved_Layer = "{0}.lyr".format(generalNameUse)
        SHPNAME = "{0}_final.shp".format(generalNameUse)
        ZIPSHP = "{0}_SHP.zip".format(generalNameUse)

        # Set the spatial reference
        spatialReference = arcpy.SpatialReference(4326)

        # Make the XY event layer
        arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spatialReference)

        # Save to a layer file
        finalLayer = arcpy.SaveToLayerFile_management(out_Layer, saved_Layer)
        print finalLayer

        # Copy features to shapefile
        arcpy.CopyFeatures_management(saved_Layer, "Output.shp")
        arcpy.FeatureClassToFeatureClass_conversion("Output.shp", workspace, SHPNAME)

    except:
        # If an error occurred print the message to the screen
        print arcpy.GetMessages()

    print "Shapefile created"

    # transfer the shapefile to a compressed (zipped) folder
    zipShapefile(SHPNAME, ZIPSHP)
    print "Shapefile is zipped and ready to go!"

    # upload the item to your ArcGIS Online account
    addItem()
    print "Your shapefile has been uploaded to AGOL!"
