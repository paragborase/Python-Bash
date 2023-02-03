#!/bin/bash

os=('ubuntu' 'windows' 'kali')
os[3]='mac'

echo "To print all element of array"
echo "${os[@]}"
echo
echo "To print 0th element"
echo "${os[0]}"
echo
echo "To print indexes of array"
echo "${!os[@]}"
echo
echo "To print count of indexes"
echo "${#os[@]}"
echo
echo "To remove 2nd element"
unset os[2]
echo "To print all element of array"
echo "${os[@]}"
