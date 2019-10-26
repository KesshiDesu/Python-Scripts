import os


#if file is zip
    #and has a folder of the same name:
    #delete the zip file

Files = os.listdir() #outputted as a list
print(Files)
#zipFiles = [f for f in Files if ".zip" in f]
zipFiles = [f for f in Files if ".zip" in f]
print(zipFiles)
i = len(zipFiles)
print(i)
while i > 0:
    nFileName = zipFiles[i-1].replace(".zip","")
    print(nFileName)
    if os.path.exists(nFileName):
        os.remove(zipFiles[i-1])
        print("deleted")
    else:
        print("not extracted")
    i = i-1
