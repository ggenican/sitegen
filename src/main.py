import os
import shutil

def copySourceFiles(base, items):
    source = items
    for item in os.listdir(base):
        if os.path.isdir(f"{base}/{item}/"):
            source[os.path.join(base, item)] = "folder"
            copySourceFiles(f"{base}/{item}/", source)
        else:
            source[os.path.join(base, item)] = "file"

    return source

def main():
    sourceFolder = os.getcwd()
    destFolder = os.getcwd() + "/public"

    if os.path.exists(destFolder):
        shutil.rmtree(destFolder)
    os.mkdir(destFolder)
    source = copySourceFiles(sourceFolder + "/static", {})

    # first create the folder structure
    for key in source.keys():
        if source[key] == "folder":
            os.mkdir(key.replace("static", "public"))

    # then copy all the files into the corresponding folder
    for key in source.keys():
        if source[key] == "file":
            shutil.copy(key, key.replace("static", "public"))
     
main()
