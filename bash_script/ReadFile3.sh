#!/bin/bash
#echo "===============Third Method=================="
while IFS= read -r line
do 
    echo $line
done < ReadFile3.sh
