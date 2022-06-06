n = int(input("Enter number of processes : "))
m = int(input("Enter number of blocks : "))
p = []
b = []
order = []
allocated = [0]*n
for i in range(n):
    p.append(int(input(f"Enter size of process {i+1} : ")))
for i in range(0,m):
    b.append(int(input(f"Enter size of block {i+1} : ")))

for i in range(0,n):
    if allocated[i]==0:
        diff = []
        for j in range(0,m):
            if b[j]-p[i]<0:
                diff.append(99999999)
            else:
                diff.append(b[j]-p[i])
        if min(diff)!=99999999:
            ind = diff.index(min(diff))
            allocated[i]=1
            order.append(f"Process {i+1} allocated to block {ind+1} having size {b[ind]}")
            b[ind]-=p[i]
for i in range(0,n):
    if allocated[i]==0:
        order.append(f"Process {i+1} is not allocated any block")
for i in range(0,n):
    print(order[i])