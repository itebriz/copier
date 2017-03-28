import os
import shutil

sourcePath = input("Enter source directory  ")
destinationPath = input("Enter destinationination  ")

for root, dirs, files in os.walk(sourcePath):
    destination = destinationPath + root.replace(sourcePath, '')
    
    if not os.path.isdir(destination):
        os.mkdir(destination)
        print('New directory path: ' + destination)    
    for f in files:
        oldLoc = root + '\\' + f
        newLoc = destination + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print('File ' + f + ' copied.')
            except IOError:
                print('file "' + f + '" already exists')