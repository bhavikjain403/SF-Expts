#!/bin/bash

echo Enter a number :
read n
sum=0
while [ $n -gt 0 ]
do
sum=$(( sum + n % 10 ))
n=$(( n / 10 ))
done
echo Sum is $sum
