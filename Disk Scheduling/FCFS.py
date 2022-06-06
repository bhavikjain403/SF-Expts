n = int(input("Enter number of processes :"))
x = int(input("Enter initial head position : "))
l = []
for i in range(n):
    l.append(int(input(f"Enter process {i+1} : ")))
sum = abs(x-l[0])
for i in range(1,n):
    sum += abs(l[i]-l[i-1])
print("The seek sequence is ",l)
print("Total head movement is :",sum)