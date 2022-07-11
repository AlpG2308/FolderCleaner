import os
import glob
import shutil
keepers=("ipynb_checkpoints","EndNote X9-win-ukn","ipynb", "md", "py")

def getFileTypes(keepers):
    files = []
    types = []
#making a list of files and filetypes
    for file in os.listdir("."):
        if len(file.split(".")) <= 2:
            files.append(file)
    for f in files:
        t = f.split(".")[-1]
        if t not in types:
            types.append(t)
    types = [type for type in types if type not in keepers]
    return types
#making folders for each filetype
def createFolders(types):
    for type in types:
        if os.path.isdir("."+type):
            pass
        else:
            os.makedirs("./"+type, exist_ok = True)

#moving all files of same type in same folder
def moveFiles(types):
    for n in types:
       for i in glob.glob("./*."+n):
          shutil.move(i,"./"+n)

if __name__ == "__main__":
    types = getFileTypes(keepers)
    createFolders(types)
    moveFiles(types)
