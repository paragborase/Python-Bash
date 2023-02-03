#!/bin/bash
echo "Enter the Input"
read INPUT 
echo "Input is $INPUT"
echo
echo "======================================================="
echo  Enter the Multiple Input
echo "======================================================="
echo "Enter you friend names: "
read Name1 Name2 Name3
echo "Friend names are : $Name1 $Name2 $Name3"
echo
echo "======================================================="
echo  Enter the input on same line
echo "======================================================="
read -p "Username is : " Username
echo "Username is $Username"
echo
echo "======================================================="
echo  input are password with reflecting on terminal
echo "======================================================="
read -sp "Password is : " PASS 
echo password is $PASS 
echo 
echo "======================================================="
echo  insert input inside Array
echo "======================================================="
echo "Enter 3 Input: "
read -a names
echo "Names are  : ${names[0]}, ${names[1]}, ${names[2]}"
echo
#First elemnt condider as zeroth element
echo "======================================================="
echo  without using input variable
echo "======================================================="
echo "Enter Name: "
read
echo "Name is : $REPLY"