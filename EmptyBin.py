import os
import urllib.request

def Download(link, fName):
    #File.retrieve("http://www.nirsoft.net/utils/nircmd.zip", "nircmd.zip")
    urllib.request.urlretrieve(link, fName)

def unZip(fName):
    import zipfile
    zip_ref = zipfile.ZipFile(fName, 'r')
    zip_ref.extractall()
    #zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()

fileCheck = ("nircmd.exe")
downFile = ("nircmd.zip")
if not os.path.isfile(fileCheck): #check if file exists
    Download("http://www.nirsoft.net/utils/nircmd.zip", downFile)
    unZip(downFile)
    os.remove("NirCmd.chm")
    os.remove("nircmd.zip")
    os.remove("nircmdc.exe")

scriptLoc = os.getcwd()
shortcutName = "EmptyBin.lnk"
shortcutLoc = ('"'+scriptLoc+"\\"+shortcutName+'"')
print(shortcutLoc)
print(scriptLoc)
vbsName = ("shortcut.vbs")

target = ('"'+os.getcwd()+"\\"+fileCheck+'"')
startIn = ('"'+os.getcwd()+'"')

file = open(vbsName, "w")
file.write(r"""Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = """+shortcutLoc+r"""
Set oLink = oWS.CreateShortcut(sLinkFile)

oLink.TargetPath = """+target+r"""
oLink.Arguments = "emptybin"
'  oLink.Description = "MyProgram"
'  oLink.HotKey = "ALT+CTRL+F"
'  oLink.IconLocation = "F:\Users\, 2"
'  oLink.WindowStyle = "7"
'  oLink.WorkingDirectory = """+startIn+r"""
oLink.Save""")
file.close()
os.startfile(vbsName)
os.startfile(shortcutName)
