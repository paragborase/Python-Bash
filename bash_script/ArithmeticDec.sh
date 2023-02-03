#!/bin/bash
echo -e "Enter the Number 1: \c"
read Num1
echo -e "Enter the Number 2: \c"
read Num2

echo "$Num1+$Num2" |bc
echo "$Num1-$Num2" |bc
echo "$Num1*$Num2" | bc
echo "scale=2;$Num1/$Num2" | bc  #get value upto 2 decimal places
echo "$Num1%$Num2" | bc


Num= 25

echo "scale=2;sqrt($Num)" | bc -l
echo "scale=2;3^3" | bc -l

echo "$Num++" | bc
