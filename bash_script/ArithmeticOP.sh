#!/bin/bash
echo -e "Enter the Number 1: \c"
read Num1
echo -e "Enter the Number 2: \c"
read Num2

echo "$(( Num1 + Num2 ))"
echo "$(( Num1 - Num2 ))"
echo "$(( Num1 * Num2 ))"
echo "$(( Num1 / Num2 ))"
echo "$(( Num1 % Num2 ))"

echo "OR=============================================="

echo "$( expr $Num1 + $Num2 )"
echo "$( expr $Num1 - $Num2 )"
echo "$( expr $Num1 \* $Num2 )"
echo "$( expr $Num1 / $Num2 )"
echo "$( expr $Num1 % $Num2 )"