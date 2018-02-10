# ArcGISOnline-ExcelUploadAutomation

Repository contains python used to upload an excel workbook to an individuals ArcGIS Online account. The script analyzes the excel workbook to confirm there is a valid Latitude and Longitude. The process then transforms that excel into a shapefile before compressing the .shp and uploading to an AGO account.

Script does not publish as a hosted feature service. Therefore after the shapefile has been 
uploaded by the script you must 'Publish' the shapefile in the items property page in your ArcGIS Online account
before adding it to a web map. 

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Software you'll need to run the project

```
python
pip
arcpy - python library installed with ArcGIS for Desktop
openpyxl - python library
ArcGIS Online Account
```

### Installing

A step by step series of examples that tell you how to get a development env running

```
pip install openpyxl
```

Open AGOLexcelUpload.py in an IDE and run the script.

## Built With

* [Python](https://www.python.org/) - The programming language used

## Authors

* **Jason Berney**

## Acknowledgments

* University of Washington - Master of Science in Geospatial Technology

