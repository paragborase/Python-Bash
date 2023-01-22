#######################################################
#Type       :File Automation
#Description:Design Automation script which accept directory name and Display recursive Duplicate Files from Directory
#Author     : Parag Borase
#Date       : 22/01/2023
#usage      : With Command line argument
#Command    : python DisplayDuplicate [Directory Path]
########################################################
import os
from sys import *
import hashlib

def hashfile(path, blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    
    fd.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.abspath(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        
        return dups
    else:
        print("Invalid Path")

def PrintDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicate found: ")

        print("The Following files are identical")

        iCnt = 0
        for result in results:
            for subresult in result:
                iCnt = iCnt + 1
                if iCnt >= 2:
                    print("\t\t%s" % subresult)
    else:
        print("No deplicate files found")

def main():
    print("____Automation script which accept directory name and Display recursive Duplicate Files from Directory____")
    
    print("Application Name: "+argv[0])

    if(len(argv) != 2):
        print("Error: Invalid Number of Argument")
        exit()

    if(argv[1] == '-h') or (argv[1] == '-H'):
        print("This script is used to file duplicates file in specified path")
        exit()
    
    if(argv[1] == '-u') or (argv[1] == '-U'):
        print("Usage: python application_Name absolute_path")
        exit()
    
    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error: Invalid DataType of Input")
    
if __name__=="__main__":
    main()