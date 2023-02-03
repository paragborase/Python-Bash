#!/bin/bash
echo To print the arg at on Time 
echo "$@"
echo ========================================================
args=("$@")
echo ${args[0]}, ${args[1]}, ${args[2]}
echo
echo ========================================================
echo Count the Number of element
echo $#

