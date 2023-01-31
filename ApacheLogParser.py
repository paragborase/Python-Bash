#######################################################
#Type       :File Automation
#Description:Accept access log file from user and return Ip_address and count in csv format
#            _>Extention add sendmail module and automate process after every 24 hours
#Author     : Parag Borase
#Date       : 01/02/2023
#usage      : With Command line argument
#Command    : python ApacheLogParser.py File_Name
########################################################
import csv
from sys import *
import os
import re
from collections import Counter

def read_log(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
        print(path)
    
    regexpression = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    exists = os.path.isfile(path)

    if exists:
        fd = open(path)
        log = fd.read()
        ip_list = re.findall(regexpression,log)
        #print(ip_list)
        return ip_list
        
    else:
        print("Invalid Path")

def count_ip(input_list):
    IP_Count = Counter(input_list)
    #print(IP_Count)
    return IP_Count


def csv_writer(input_dict):

    with open('output.csv', 'w') as filewriter:
        writer = csv.writer(filewriter)

        header = ['IP','Access_count']

        writer.writerow(header)

        for server in input_dict:
            writer.writerow((server,input_dict[server]))



def main():
    print("___Automation script which Accept access log file from user and return Ip_address and count in csv format____")
    print("Application Name: "+argv[0])

    if(len(argv) != 2):
        print("Error : Invalid Number of arguments")
        exit()
    
    if((argv[1] == '-h') or (argv[1] == '-H')):
        print("Accept access log file from user and return Ip_address and count in csv format")
        exit()
    
    if((argv[1] == '-u') or (argv[1] == '-U')):
        print("Usage: Application Access_log_File_name")
        exit()

    try:
        arr = []
        dict = {}

        arr = read_log(argv[1])
        dict = count_ip(arr)
        csv_writer(dict)
    
    except ValueError:
        print("Error: Invalid Dataype of input")
    except Exception:
        print("Error: Invalid Dataype of input")

if __name__=="__main__":
    main()