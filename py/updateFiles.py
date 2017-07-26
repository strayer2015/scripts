#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
###/usr/bin/python3.6
# Author: Chia-Hsiang Chen

import re, os, sys

#def replace(old,new):
patternStr = "ecyn_"
repStr = "acyn_"

# Replace wire name and file name
def replaceStringInFile(filePath):
    inputFile = open(filePath)
    tempName = filePath+"~~~"
    outputFile = open(tempName,'w')
    fContent = inputFile.read()
    outText = re.sub(patternStr, repStr, fContent)

    outputFile.write(outText)
    outputFile.close()
    inputFile.close()

    os.rename(tempName, filePath)
    destName = re.sub(patternStr, repStr, filePath)
    os.rename(filePath, destName)
    print("processed %s"%destName)

# File Walk through
def walkThrough(inputDir):
    for folderName, subfolders, fileNames in os.walk(inputDir):
        for fileName in fileNames:
            replaceStringInFile(os.path.join(folderName,fileName))



print("Enter the folder: ", end="")
inputDir = input()
print("Replacing pattern \033[91;1m%s\033[0m with \033[91;1m%s\033[0m, is it correct? (Y) to continue"%(patternStr,repStr))
assert input()=="Y","Exiting..."
walkThrough(inputDir)
                                                                                        
