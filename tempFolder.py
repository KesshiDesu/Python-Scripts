import os
import stat
import shutil
import time
FileName = "Temp"

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWUSR)
    func(path)
    
if os.path.exists(FileName):
    if os.listdir(FileName): #if directory isnt empty
        shutil.rmtree(FileName, onerror=remove_readonly)#remove folder tree
        #shutil.rmtree(FileName, ignore_errors=True, onerror=remove_readonly)#remove folder tree
        time.sleep(.1)
        os.makedirs(FileName)#make temp folder
else:
    os.makedirs(FileName)
