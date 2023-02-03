#!/bin/bash

function CheckFile()
{
    local file=$1
    if [ -f file ]
    then 
        echo "file is present"
    else
        echo "File is not presnet"
    fi
}

CheckFile Function2.sh