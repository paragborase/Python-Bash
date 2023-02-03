#!/bin/bash
#use Case
#To check all directory present
# * check all files recursively
for item in *
do
    if [ -d  $item ]
    then
        echo $item
    fi
done