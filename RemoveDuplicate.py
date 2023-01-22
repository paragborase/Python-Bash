#######################################################
#Type       :File Automation
#Description:Design Automation script which accept directory name and all remove duplicate Files and sent duplicate files names on mail
#Author     : Parag Borase
#Date       : 22/01/2023
#usage      : With Command line argument
#Command    : python RemoveDuplicate.py [Directory Path]
########################################################
import os
from sys import *
import hashlib
import time
import smtplib 

def DeleteFiles(dict1,RemovedData):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    fd1 = open(RemovedData, 'a')
    fd1.write("Removed File are: \n")
    iCnt = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                iCnt = iCnt + 1
                if iCnt >= 2:
                    fd1.write(subresult + '\n')
                    os.remove(subresult)
            iCnt = 0


        # list of email_id to send the mail 
        li = ["paragborase***@gmail.com"] 

        for dest in li: 
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls() 
            s.login("paragborase***gmail.com", "**********") 
            SUBJECT = "Removed files from servers"
            TEXT = fd1.read()
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            s.sendmail("paragborase***@gmail.com", dest, message) 
            s.quit() 

    else:
        print("No Duplicate File Found")

def hashfile(path, blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    
    fd.close()

    return hasher.hexdigest()

def findDup(path):
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

def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicate found: ")
        print("The Following files are identical")
        for result in results:
            for subresult in result:
                print("\t\t%s" % subresult)
    else:
        print("No deplicate files found")

def main():
    print("____Automation script which accept directory name and all remove duplicate Files and sent duplicate files names on mail By PARAG BORASE____")
    
    print("Application Name: "+argv[0])

    if(len(argv) != 2):
        print("Error: Invalid Number of Argument")
        exit()

    if(argv[1] == '-h') or (argv[1] == '-H'):
        print("Automation Script which accept directory name from user and rmeove duplicate files from that Directory")
        exit()
    
    if(argv[1] == '-u') or (argv[1] == '-U'):
        print("Usage: python application_Name absolute_path")
        exit()
    
    try:
        arr = {}
        startTime = time.time()
        arr = findDup(argv[1])
        printResults(arr)
        print("enter the File Name need to create: ")
        RemovedData = input()
        DeleteFiles(arr,RemovedData)
        endTime = time.time()

        print("Tool %s second to evolute "%(endTime - startTime))

    except ValueError:
        print("Error: Invalid DataType of Input")
    except Exception as E:
        print("Error : Invalid Input",E)

if __name__=="__main__":
    main()