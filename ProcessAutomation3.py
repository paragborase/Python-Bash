#######################################################
#Script which accept the Directory name from user and create log filein that 
#directory which contains information of all running process
#Author : Parag Borase
#Date: 16/01/2023
#usage:
#python ProcessAutomation3.py 
########################################################
from datetime import datetime
import os
import psutil
import time
from sys import *

def ProcessDisplay(log_dir = "Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    seperator = "_" * 80
    #log_path = os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    log_path = os.path.join(log_dir,datetime.now().strftime('ProcessLogs_%H_%M_%d_%m_%Y.log'))
    f = open(log_path,'w')
    f.write(seperator + "\n")
    f.write(" Process Logger: "+time.ctime()+ "\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

def main():
    print("____Process Automation by Parag Borase______")
    print("Application Name:"+argv[0])

    ProcessDisplay(argv[1])
    if(len(argv) != 2):
        print("Error: Invalid Number of argument")
        exit()

    if(argv[1] == "-h") or (argv[1] =="-H"):
        print("This script is used log record of running processes")
        exit()

    if(argv[1] == "-u") or (argv[1] =="-U"):
        print("Usage: Application AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])
    except ValueError:
        print("Error: Invalid Datatype of Input")
    except Exception:
        print("Error: Invalid Input")

if __name__=="__main__":
    main()