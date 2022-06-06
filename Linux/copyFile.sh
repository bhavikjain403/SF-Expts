#!/bin/bash

echo Enter name of new directory
read d
mkdir $d
echo Enter name of file to be copied
read f
cp $f $d
