#!/bin/bash
#Reverse as cosnider with while

Num=1

until [ $Num -gt 10 ]
do 
    echo $Num
    #Num=$((Num + 1))
    (( Num++ ))
done