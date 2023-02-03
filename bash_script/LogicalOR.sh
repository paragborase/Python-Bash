#!/bin/bash

read -p "Enter the Age : " Age
echo
if (( "$Age" > 18 )) || (( "$Age" < 30 )) 
#if [ "$Age" -gt 18 ] || [ "$Age" -lt 30 ] 
#if [[ "$Age" -gt 18  ||  "$Age" -lt 30 ]]
#if [ "$Age" -gt 18  -o  "$Age" -lt 30 ]
then 
    echo "Age is Valid"
else
    echo "Age is not Valid"
fi