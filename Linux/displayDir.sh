#!/bin/bash

echo Enter directory name
read d

echo 'Enter 1 for short description'
echo 'Enter 2 for long description'
echo 'Enter 3 for hidden file display'
read c

case "$c" in
1) ls $d
;;
2) ls -l $d
;;
3) ls -a $d
;;
*) echo Invalid choice
esac
