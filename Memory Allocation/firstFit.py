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
        for j in range(0,m):
            if b[j]>=p[i]:
                allocated[i]=1
                order.append(f"Process {i+1} allocated to block {j+1} having size {b[j]}")
                b[j]-=p[i]
                break
for i in range(0,n):
    if allocated[i]==0:
        order.append(f"Process {i+1} is not allocated any block")
for i in range(0,n):
    print(order[i])