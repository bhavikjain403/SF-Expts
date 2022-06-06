n = int(input("Enter number of processes : "))
l = []
gantt = []
for i in range(n):
    temp = []
    temp.append(i)
    temp.append(int(input(f"Enter arrival time for process {i} : ")))
    temp.append(int(input(f"Enter burst time for process {i} : ")))
    l.append(temp)
l.sort(key=lambda x:x[1])
completionTime = [l[0][1]+l[0][2]]
gantt.append(f"P{l[0][0]} scheduled from time {l[0][1]} to {l[0][1]+l[0][2]}")
for i in range(1,n):
    if l[i][1]<=completionTime[i-1]:
        completionTime.append(completionTime[i-1]+l[i][2])
        gantt.append(f"P{l[i][0]} scheduled from time {completionTime[i-1]} to {completionTime[i]}")
    else:
        completionTime.append(l[i][1]+l[i][2])
        gantt.append(f"P{l[i][0]} scheduled from time {l[i][1]} to {l[i][1]+l[i][2]}")
WT = l[0][1]
for i in range(1,n):
    if l[i][1]<=completionTime[i-1]:
        WT+=completionTime[i-1]-l[i][1]
TAT = WT
for i in range(0,n):
    TAT+=l[i][2]
    print(gantt[i])
print("Avg WT is",WT/n,"and Avg TAT is",TAT/n)