import glob
import fileinput
import os
import json
from datetime import datetime

# Reading the JSON config. file

configFile = open('vu.json')

configData = json.load(configFile)

# Config. Variables

encodingType = configData["encoding"]
version = configData["version"]
package = configData["package"]
author = configData["author"]
iterations = configData["iterations"]
ignoredFolders = configData["ignore"]
extentions = configData["extentions"]
logFilePlace = configData["logFile"]

# Variables

lineReplacementCounter = 0
switchCounter = 0

versionText = " * @version "
packageText = " * @package "
authorText = " * @author "
firstGoodLines = ""
secondGoodLines = ""

switch = False
breakSwitch = False

files = []
toChange = [[version, versionText], [package, packageText], [author, authorText]]

# Log File
try:
    logFile = open(logFilePlace, "x")
    logFile.close()
    logFile = open(logFilePlace, "a")
except FileExistsError:
    logFile = open(logFilePlace, "a")

logFile.write("[" + str(datetime.now()) + "]: New Instance created.\n")
logFile.close()

for iteration in range(iterations):
    for extention in extentions:
        temp = glob.glob("*/" * iteration + extention)
        for file in temp:
            files.append(file)


# File Reading and Editing
for change in toChange:
    if change[0] == "":
        continue
    logFile = open(logFilePlace, "a")
    for file in files:
        for ignoredFolder in ignoredFolders:
            if ignoredFolder in file:
                logFile.write("[" + str(datetime.now()) + f"]: Directory {ignoredFolder} has been skipped because of {file}.\n")
                breakSwitch = True
        if breakSwitch:
            continue
        oldFile = open(file, encoding=encodingType)
        lines = oldFile.readlines()
        oldFile.close()
        os.remove(file)
        otherTemp = open(file, "x", encoding=encodingType)
        otherTemp.close()
        temp = open(file, "r+", encoding=encodingType)
        for line in lines:
            if change[1] + change[0] == line:
                break
            if change[1] not in line:
                if not switch:
                    firstGoodLines = firstGoodLines + line
                else:
                    secondGoodLines = secondGoodLines + line
            else:
                switch = True
                
        replacementLine = change[1] + change[0]
        final = "" + firstGoodLines + replacementLine + "\n" + secondGoodLines
        temp.write(final)
        temp.close()
        firstGoodLines, secondGoodLines, replacementLine = ("", "", "")
        switch = False
        breakSwitch = False
        logFile.write("[" + str(datetime.now()) + f"]: File {file} has been edited.\n")
    file = ""
    firstGoodLines, secondGoodLines, replacementLine = ("", "", "")
    switch = False
    breakSwitch = False
    logFile.close()
