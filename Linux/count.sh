#!/bin/bash

echo Enter name of file:
read f

echo Number of lines is:
wc -l < $f

echo Number of words is :
wc -w < $f

echo Number of characters is :
wc -c < $f
