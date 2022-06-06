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
small.sort(reverse=True)
large.sort()
if head-small[0]<large[0]-head:
    mov = head-small[-1]+large[-1]-small[-1]
    order = small+large
else:
    mov = large[-1]-head+large[-1]-small[-1]
    order = large+small
print("The seek sequence is ",order)
print("Total head movement is :",mov)