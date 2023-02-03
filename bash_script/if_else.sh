#!/bin/bash

count=10
if [ $count -eq 10 ]
then 
    echo "Number is equal to 10"
else
    echo "Number is not equal to 10"
fi

echo =======================================================

word="b"
if [[ $word > "b" ]]
then 
    echo "condition is true"
elif [[ $word = b ]]
then
    echo "Value of $word"
else
    echo "Condition is false"
fi


echo =======================================================