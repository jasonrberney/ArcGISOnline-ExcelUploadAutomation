# ArcGISOnline-ExcelUploadAutomation

This python is used to upload an excel workbook to an individuals ArcGIS Online account. The script analyzes the excel workbook to confirm there is a valid Latitude and Longitude. The process then transforms that excel into a shapefile before compressing the .shp and uploading to an AGO account.

Script does not publish as a hosted feature service and therefore after the shapefile has been 
uploaded by the script you must 'Publish' the shapefile in the items property page in your ArcGIS Online account
before adding it to a web map. 

Enjoy!

# Script Execution
Please make sure to input a workspace in the 'AGOLexcelUpload.py' file. 
Install Python libraries:
arcpy, openpyxl
