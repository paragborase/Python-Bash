#!/bin/bash
#use Case
#For loop with Command execution
for Command in ls pwd date
do
    echo "-----------------$Command-------------------------"
    $Command
done

