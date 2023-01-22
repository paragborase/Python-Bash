
#######################################################
#Type       :Network Automation SSH KEY
#Description:Create client-server model, execute command from client to server and print output result.
#            SSH key based authentication
#Author     : Parag Borase
#Date       : 22/01/2023
#usage      : With Command line argument
#Command    : python SSHlogin_authorised_keys.py
########################################################
import paramiko
from getpass import getpass
import time

def main():
    host1 = "Hostname1"
    user1 = (input("Enter Username: ")or "e11111")
    pass1 = getpass("Enter Password")

    #Enter use name or by default its takes from given username as e11111
    #getpass : password is not visible while providing input as password

    session = paramiko.SSHClient()

    #server send Key while login, if key is not avaible then automatically add host key in client
    #only use if clinet do not have host entry in trusted host list
    #session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #if ~/.ssh/known_hosts already having host key entry then we can read from file Known_host
    session.load_system_host_keys()

    #if you want to provide exact  file name
    #session.load_host_keys('/home/Linux_setup1/.ssh/knwon_hosts')

    key_pass = getpass("Enter private key passowrd: ")
    key_file = paramiko.RSAKey.from_private_key_file("/home/server/.ssh/new_id", keypass)

    commands = ['echo$TOMCAT_HOME','echo $USER','hostname','echo $JAVA', 'Incorrect' ]

    
    session.connect(hostname=host1, username=user1,pkey=key_file,allow_agent=False, look_for_keys=False)


    for command in commands:
        print(f"{'*'*5} Execute Command: {command} {'*'*5}")
        stdin, stdout, stderr = session.exec_command(command)
        time.sleep(1)
        print(stdout.read().decode())

        ERROR = stderr.read().decode()
        if ERROR:
            print(ERROR)


    session.close()

if __name__=="__main__":
    main()


#descrition:
#step.1) Login To client remove already existed authorized key (cd /home/client/.ssh/)
#step.2) Login to Master_server exceute $ssh-keygen (Enter: Id name be default id_rsa; Enter: passphrase)
#step.3) From Master_server $ssh-copy-id client1@client1_ip/hostname (enter: passowrd) (or manullay copy)
#step.4) Verify content ssh public key of clinet from server.
#        from client check newly key in authorised_key .