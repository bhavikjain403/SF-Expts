n = int(input("Enter number of processes : "))
r = int(input("Enter number of resources : "))
maxResources = []
allocated = []
maxRequired = []
available = []
need = []
for i in range(r):
    maxResources.append(int(input(f"Enter number of resources of type {i+1} : ")))
for i in range(0,n):
    print(f"Enter number of allocated resources for process {i+1} :")
    temp = []
    for j in range(r):
        temp.append(int(input(f"Number of resource {j+1} : ")))
    allocated.append(temp)
for i in range(0,n):
    print(f"Enter maximum number of resources for process {i+1} :")
    temp = []
    for j in range(0,r):
        temp.append(int(input(f"Number of resource {j+1} : ")))
    maxRequired.append(temp)
for i in range(0,r):
    temp = 0
    for j in range(0,n):
        temp+=allocated[j][i]
    available.append(maxResources[i] - temp)
for i in range(0,n):
    temp = []
    for j in range(0,r):
        temp.append(maxRequired[i][j]-allocated[i][j])
    need.append(temp)

visited = [0]*n
order = []
n1 = n

while n1:
    for i in range(n):
        if visited[i]==0:
            flag = 1
            for j in range(0,r):
                if available[j]<need[i][j]:
                    flag=0
                    break
            if flag:
                visited[i]=1
                order.append(f"P{i+1}")
                for j in range(0,r):
                    available[j]+=allocated[i][j]
    n1-=1
print("The sequence of executed processes is :", order)
if len(order)==n:
    print("Since all processes are executed, the system is in safe state.")
else:
    print("Since all processes are not executed, the system is in unsafe state.")