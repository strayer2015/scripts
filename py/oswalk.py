#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
#Author: Chia-Hsiang Chen

import os,re

def getsize(sizeStr):
    while(re.match('\d{4}',sizeStr)): sizeStr = re.sub('^(\d+)(\d{3})',r'\1,\2',sizeStr)
    return sizeStr


for folderName, subfolders, filenames in os.walk(input()):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename + ' size: ' + getsize(str(os.path.getsize(os.path.join(folderName,filename)))))

    print('')
