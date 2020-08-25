#!/bin/bash

stty -F /dev/ttyUSB0 speed 9600 cs8 -cstopb -parenb min 0 time 10 > /dev/null 2>&1 

count=0

while :
do
    sleep 6
    ((count++))
    read -r line < /dev/ttyUSB0
    echo "${count}, ${line}" >> data.csv
    echo "${count}, ${line}"
done
