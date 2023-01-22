#######################################################
#Type       :Automation Template Pattern
#Description:Automation standard template pattern 
#Author     : Parag Borase
#Date       : 22/01/2023
#usage      : With Command line argument
#Command    : python Automation_Template.py [Argument1]
########################################################
from sys import *

def Script_Task(No):
    pass

def main():
    print("________Automation_Template_BY_PARAG_BORASE________")
    print("Automation script started with name : ",argv[0])

    if len(argv) != 2:
        print("Error : Insufficient Argument")
        print("Use -h for help and use -s uses for the script")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")) :
        print("Help : This script is use to perform _______")

    elif((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage: Provide _____Number of argument as")
        print("First Argument as : _________")
        print("Second Argument as : _________")
        exit()

    else:
        Script_Task(int(argv[1]))

if __name__=="__main__":
    main()