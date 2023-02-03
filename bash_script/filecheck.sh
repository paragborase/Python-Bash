#!/bin/bash
#File test operator
read -p "Enter Name of File: " FileName

#echo -e "Enter the Name of File : \c"
#read FileName

if [ -f $FileName ]
then
    echo File is Presnt
else
    echo File is not present
fi

echo
echo ==================================================

read -p "Enter directory Name: " DirName

if [ -d $DirName ]
then
    echo directory is Presnt
else
    echo directory is not present
fi

echo
echo ==================================================
echo to check block special file
echo "if [ -d Name ]" 
echo ==================================================
echo to check character special file
echo "if [ -c Name ]" 
echo ==================================================
echo to check file is present  file
echo "if [ -s Name ]" 
echo ==================================================
echo to check file having read, write,execute permisison
echo "if [ -r Name ]" 
echo "if [ -w Name ]" 
echo "if [ -x Name ]" 