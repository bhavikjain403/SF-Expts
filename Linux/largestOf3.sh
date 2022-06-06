#!/bin/bash

echo "Enter first number :"
read a
echo "Enter second number :"
read b
echo "Enter third number :"
read c
if [ $a -gt $b ] && [ $a -gt $c ]
then
	echo $a is largest
elif [ $b -gt $a ] && [ $b -gt $c ]
then
	echo $b is largest
else
	echo $c is largest
fi 
