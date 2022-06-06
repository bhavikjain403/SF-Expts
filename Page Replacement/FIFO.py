l = []
n = int(input("Enter number of pages : "))
f = int(input("Enter number of frames : "))
for i in range(n):
    l.append(int(input(f"Enter page {i+1} : ")))
pages = [-1]*n
fault = 0
for i in range(0,n):
    if l[i] not in pages:
        for j in range(0,f-1):
            pages[j]=pages[j+1]
        pages[f-1]=l[i]
        fault+=1
print("Number of faults is",fault)