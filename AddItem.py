import Tkinter, tkFileDialog, re
import arcrest
from arcresthelper import securityhandlerhelper
def trace():

    #trace finds the line, the filename and error message and returns it to the user

    import traceback, inspect
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    filename = inspect.getfile(inspect.currentframe())
    # script name + line number
    line = tbinfo.split(", ")[1]
    # Get Python syntax error
    synerror = traceback.format_exc().splitlines()[-1]
    return line, filename, synerror

def addItem():
    proxy_port = None
    proxy_url = None

    usernameInput = raw_input("Please enter your username: ")
    passwordInput = raw_input("Please enter your password: ")

    securityinfo = {}
    securityinfo['security_type'] = 'Portal'#LDAP, NTLM, OAuth, Portal, PKI
    securityinfo['username'] = usernameInput
    securityinfo['password'] = passwordInput
    securityinfo['org_url'] = "http://www.arcgis.com"
    securityinfo['proxy_url'] = proxy_url
    securityinfo['proxy_port'] = proxy_port
    securityinfo['referer_url'] = None
    securityinfo['token_url'] = None
    securityinfo['certificatefile'] = None
    securityinfo['keyfile'] = None
    securityinfo['client_id'] = None
    securityinfo['secret_id'] = None

    root = Tkinter.Tk()
    root.withdraw()

    filename = tkFileDialog.askopenfilename(parent=root,title='Select File to Upload')

    upload_file = filename
    try:

        shh = securityhandlerhelper.securityhandlerhelper(securityinfo)
        if shh.valid == False:
            print shh.message
        else:
            admin = arcrest.manageorg.Administration(securityHandler=shh.securityhandler)
            content = admin.content
            userInfo = content.users.user()

            titleInput = raw_input("Please enter a title for your upload: ")

            itemParams = arcrest.manageorg.ItemParameter()
            itemParams.title = titleInput
            #itemParams.thumbnail = None
            """
            Valid types
            "Shapefile", "CityEngine Web Scene", "Web Scene", "KML",
                         "Code Sample",
                         "Code Attachment", "Operations Dashboard Add In",
                         "CSV", "CSV Collection", "CAD Drawing", "Service Definition",
                         "Microsoft Word", "Microsoft Powerpoint",
                         "Microsoft Excel", "PDF", "Image",
                         "Visio Document", "iWork Keynote", "iWork Pages",
                         "iWork Numbers", "Map Document", "Map Package",
                         "Basemap Package", "Tile Package", "Project Package",
                         "Task File", "ArcPad Package", "Explorer Map",
                         "Globe Document", "Scene Document", "Published Map",
                         "Map Template", "Windows Mobile Package", "Pro Map",
                         "Layout", "Layer", "Layer Package", "File Geodatabase",
                         "Explorer Layer", "Geoprocessing Package", "Geoprocessing Sample",
                         "Locator Package", "Rule Package", "Workflow Manager Package",
                         "Desktop Application", "Desktop Application Template",
                         "Code Sample", "Desktop Add In", "Explorer Add In",
                         "ArcGIS Desktop Add-In", "ArcGIS Explorer Add-In",
                         "ArcGIS Explorer application configuration", "ArcGIS Explorer document"
            """
            itemParams.type = "Shapefile"
            itemParams.overwrite = True
            itemParams.description = "Auto Upload File"
            itemParams.tags = "tags"
            itemParams.snippet = "Auto Upload File"
            itemParams.typeKeywords = "Data"
            #itemParams.filename = upload_file
            item = userInfo.addItem(
                itemParameters=itemParams,
                filePath= upload_file,
                overwrite=True,
                relationshipType=None,
                originItemId=None,
                destinationItemId=None,
                serviceProxyParams=None,
                metadata=None)
            print item.title + " created"

    except:
        line, filename, synerror = trace()
        print "error on line: %s" % line
        print "error in file name: %s" % filename
        print "with error message: %s" % synerror

if __name__ == "__main__":
    main()
