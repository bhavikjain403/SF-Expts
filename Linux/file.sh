echo Enter name of directory : 
read d
mkdir $d
cd $d
echo Enter number of files :
read n
for (( i=0; i<$n; i++ ))
do
echo Enter name of file $(( i + 1 )) :
read f
touch $f
done
echo files have been created in directory $d
