n = int(input("Enter number of processes :"))
head = int(input("Enter initial head position : "))
cyl = int(input("Enter number of disk cylinders : "))
l = []
small = []
large = []
order = []
for i in range(n):
    l.append(int(input(f"Enter process {i+1} : ")))
    if l[i]<head:
        small.append(l[i])
    else:
        large.append(l[i])

dir = int(input("Enter 0 for left, 1 for right : "))
if dir:
    small.sort()
    large.sort()
    mov = cyl-1-head+cyl-1+small[-1]    # since cylinders are numbered from 0
    order=large+small
else:
    small.sort(reverse=True)
    large.sort(reverse=True)
    mov= head + cyl-1+cyl-1-large[-1]
    order = small+large
print("The seek sequence is ",order)
print("Total head movement is :",mov)