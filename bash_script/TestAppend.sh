#!/bin/bash
#Append output to end of text file
echo -e "Enter the name of file : \c"
read FileName

if [ -f $FileName ]
then
    if [ -w $FileName ]
    then
        echo "Type some test data. To quite press ctrl+D"
        cat >> $FileName
    else
        echo "File do not have write permisison"
    fi
else
    echo "$FileName not exists"
fi