#######################################################
#Type       :File Automation
#Description:Design Automation script which accept directory name and display ChechSum of all Files
#Author     : Parag Borase
#Date       : 22/01/2023
#usage      : With Command line argument
#Command    : python DirectoryCheckSum.py [Directory Path]
########################################################
from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayCheckSum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    if exists:
        for DirName, SubDirs, FileList in os.walk(path):
            print("Current Folder is : "+DirName)
            for Files in FileList:
                path = os.path.join(DirName, Files)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
    else:
        print("Invalid Path")

def main():
    print("___Automation script which accept directory name and display ChechSum of all Files____")
    print("Application Name: "+argv[0])

    if(len(argv) != 2):
        print("Error : Invalid Number of arguments")
        exit()
    
    if((argv[1] == '-h') or (argv[1] == '-H')):
        print("Design Automation script which accept directory name and display CheckSum of all Files")
        exit()
    
    if((argv[1] == '-u') or (argv[1] == '-U')):
        print("Usage: Application AbsolutePath_of_Directory")
        exit()

    try:
        DisplayCheckSum(argv[1])
    except ValueError:
        print("Error: Invalid Dataype of input")
    except Exception:
        print("Error: Invalid Dataype of input")

if __name__=="__main__":
    main()