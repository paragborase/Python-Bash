#!/bin/bash
#To check signal *man signal 
trap "Echo exit signal is deletected" SIGINT
#SIGINT : interuupting the seqeunce i.e Even after presing ctrl+c script will complete execution
trap "Echo Kill Signal is detencted" SIGKILL SIGSTOP

echo "pis is $$"
while (( COUNT < 10 ))
do
    sleep 10
    (( COUNT++ ))
    echo $COUNT
done
exit 0


#Example:
#1
#2
#exit signal is deletected    when press crtl+c script still executing with echo statement
#3
#4