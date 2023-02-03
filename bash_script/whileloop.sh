#!/bin/bash

Num=1

while (( Num <= 10))
do
    echo "$Num"
    Num=$(( Num+1 ))
done

echo =============================================

Num1=1

while [ $Num1 -le 5 ]
do
    echo "$Num1"
    (( Num1++ ))
done