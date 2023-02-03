#!/bin/bash

select name in Mark John Dinu Guru
do
    case $name in
    Mark)
        echo mark selected
        ;;
    John)
        echo John selected
        ;;
    Dinu)
        echo Dinu selected
        ;;
    Guru)
        echo Guru selected
        ;;
    *)
        echo Please provide Number between 1 to 4
    esac
done


#$ ./SelectLoop1.sh 
#1) Mark
#2) John
#3) Dinu
#4) Guru
#? 1