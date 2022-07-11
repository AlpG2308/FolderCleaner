
# Folder Cleaner

This was my first python project which made my life a whole-lot easier.
What kind of problem did we try to solve?

Well, just think about following situation you need to download something and it lands in your download folder. 
What happens next? Of course... you copy and paste it to the respective location.

1000 download, copy and paste cycles later your download folder looks like a mess and even cleaning it is a lot of work.

Here comes the folder cleaner to your rescue. Just run it and each filetype will be moved to the respective folder
making cleaning and looking through these old files a whole-lot easier.

## Code Description

### Identify Filetypes

The first functions takes a _keepers_ tuple as an input, which can look like following:

`keepers = ("py","ipynb")`

As you can see only the filetype without the "**.**" is needed.
```python
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
```
The `getFileType()` function return a type list. Which is used to create the necessary folder.
With the `createFolders()` function.

### Create Folders

```python
def createFolders(types):
    for type in types:
        if os.path.isdir("."+type):
            pass
        else:
            os.makedirs("./"+type, exist_ok = True)
```

### Move Files in respective Folder

```python
def moveFiles(types):
    for n in types:
       for i in glob.glob("./*."+n):
          shutil.move(i,"./"+n)
```
After all this work the specific folder where this script is located should atleast look much neater.

## Code as a Graph

```mermaid
graph LR
getFileTypes --> createFolders & moveFiles
moveFiles --> Folders
createFolders --> Folders
```

AlpG