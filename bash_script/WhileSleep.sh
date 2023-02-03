#!/bin/bash

Num=1

while [ $Num -le 10 ]
do
    echo $Num
    #(( Num++ ))
    Num=$(( Num+1 ))
    sleep 1               #sleep 1 second
    echo "$(date)"
done