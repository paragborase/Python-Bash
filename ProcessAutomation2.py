#######################################################
#Type         :Process Automation
#Description  :Automation script which sent mail of all running processes and VMS 
#              VMS : Virtual Memory Size which is the virtual memory that process is using
#Author       :Parag Borase
#Date         :16/01/2023
#usage        :With Command line argument
#Command      :python ProcessAutomation2.py 
########################################################
import ssl
import psutil 
import smtplib
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def sendmail(file_name):
    #print(type(file_name))   <class '_io.TextIOWrapper'>

    sender_mail = 'paragborase001@gmail.com'
    password = 'xsvslwesuqywkqdz'
    receiver_mail = 'paragborase01@gmail.com'
    subject = "Automation Process Details"
    body = "Process Details for Windows OS"

    message = MIMEMultipart()
    message["From"] = sender_mail
    message["To"] = receiver_mail
    message["Subject"] = subject
    message["Bcc"] = receiver_mail

    message.attach(MIMEText(body, "plain"))

    attachment = open(file_name, 'r')
    #attachment = io.TextIOWrapper.read(file_name)
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    file_name.close()


    encoders.encode_base64(part)

    part.add_header("content-Disposition", f"attachment; filename={file_name}")

    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
       
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_mail, password)
        server.sendmail(sender_mail, receiver_mail, text)

    print("Mail has been Sent")

                
def WriteProcFile():
    Listprocess = ProcessDisplay()

    #Create File with Current datetime
    FileName = open(datetime.now().strftime('proc_details_%H_%M_%d_%m_%Y.txt'), 'a')
    FileName.write("Running Process Data"+"\n")

    #We can only Write output in String to file
    #first convert dictory output to string
    for process in Listprocess:      
        result = str(process)
        FileName.write(result+" "+"\n") 

    
    sendmail(FileName)

##########################################
# Output: {'name': 'chrome.exe', 'pid': 15348, 'username': 'DESKTOP-JPPB8IL\\Window 10 Pro', 'vms': 46.43359375}
###########################################   
def ProcessDisplay():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms']= proc.memory_info().vms/(1024*1024)

            listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def main():
    print("____Python Automation Script__________")
    print("Process Monitor")

    WriteProcFile()

if __name__=="__main__":
    main()




#Process Monitor with memory uses
#Automation script which display All running processes
import psutil

def ProcessDisplay():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms']= proc.memory_info().vms/(1024*1024)

            listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def main():
    print("Marvellous infosystem: python automation & machine learning")
    print("Process Monitor")

    listprocess = ProcessDisplay()

    for elem in listprocess:
        print(elem)

if __name__=="__main__":
    main()
