# This program will calculate the total size of any directory

import os

totalSize = 0
folderLocation = 'C:\\Users\\programming\\python' # Enter your folder location here

for fileName in os.listdir(folderLocation):
    if not os.path.isfile(os.path.join(folderLocation, fileName)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(folderLocation, fileName))

# converting totalSize from Byte to MB below

totalSizeInMB = ((totalSize/1024)/1024) 

print("Total file size is ", round(totalSizeInMB, 2), "MB")
