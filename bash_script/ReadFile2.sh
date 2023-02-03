#!/bin/bash
echo "===============Second Method=================="
cat ReadFile2.sh | while read line
do 
    echo $line
done 
