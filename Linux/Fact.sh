#!/bin/bash
echo "Enter a number : "
read a
fact=1
while [ $a -gt 0 ]
do
fact=$(( fact * a ))
a=$(( a - 1 ))
done
echo $fact
