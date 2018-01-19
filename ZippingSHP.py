import zipfile
import sys, os, glob

def zipShapefile(inShapefile, newZipFN):
    print 'Starting to Zip '+(inShapefile)+' to '+(newZipFN)

    # check if zipfile already exists
    if not (os.path.exists(inShapefile)):
        print inShapefile + ' Does Not Exist'
        return False

    # if zipfile exists then delete the zip file
    if (os.path.exists(newZipFN)):
        print 'Deleting '+newZipFN
        os.remove(newZipFN)

        # if the zipped file cannot be removed then notify the user
        if (os.path.exists(newZipFN)):
            print 'Unable to Delete'+newZipFN
            return False

    # create new zip file object
    zipobj = zipfile.ZipFile(newZipFN,'w')

    # grab all files associated with the shapefile and write them to the compressed folder
    for infile in glob.glob(inShapefile.lower().replace(".shp",".*")):
        print infile
        zipobj.write(infile,os.path.basename(infile),zipfile.ZIP_DEFLATED)

    zipobj.close()

    return True

