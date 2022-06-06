n = int(input("Enter number of processes :"))
head = int(input("Enter initial head position : "))
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
    mov = large[-1]-head + large[-1]-small[0]+small[-1]-small[0]
    order=large+small
else:
    small.sort(reverse=True)
    large.sort(reverse=True)
    mov= head-small[-1] + large[0]-small[-1]+large[0]-large[-1]
    order = small+large
print("The seek sequence is ",order)
print("Total head movement is :",mov)