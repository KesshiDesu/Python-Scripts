#All characters unzip
import os, zipfile
'''
def unZip(fName, directory = os.getcwd()):
    import zipfile
    zip_ref = zipfile.ZipFile(fName, 'r')
    zip_ref.extractall(directory)
    zip_ref.close()#test unzipping non latin characters
'''

def refresh_zipFiles():
    files = os.listdir()
    global zipFiles
    zipFiles = [f for f in files if f.endswith(".zip")]

'''
def unZip(fName, directory = os.getcwd()):
    import zipfile
    with zipfile.ZipFile(fName, 'r') as f:
        #filelist = [info.filename for info in f.infolist() if info.is_dir()]
        filelist = f.namelist()
        print(filelist)
        #with thezip.open(fName[:-4]) as thefile:
            #shutil.copyfileobj(thefile,directory)

#âGâCâèâAâôâGâCâèâAâô feat ânâìü[üAânâbâsü[âÅü[âïâhüI
'''
'''
def unZip(fName):
    from pathlib import Path
    import zipfile
    import os
    with zipfile.ZipFile(fName, 'r') as f:
        for fn in f.namelist():
            extracted_path = Path(f.extract(fn))
            #extracted_path.rename(fn.encode('cp437').decode('gbk'))
            #extracted_path.rename(fn.encode('cp437').decode('gbk'))
            print(os.path.dirname(extracted_path))
            #print(fName)

'''
def unZip(fName, directory = os.getcwd()):
    #make sure existing folder doesnt exist
    if not os.path.isfile(fName[:-4]):
        zip_ref = zipfile.ZipFile(fName)
        zip_ref.extractall(directory)
        extracted_folder = os.path.join(directory, os.path.dirname(zip_ref.namelist()[0]))
        os.rename(extracted_folder,fName[:-4])

refresh_zipFiles()
unZip(zipFiles[0])
