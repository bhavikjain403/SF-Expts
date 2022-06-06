l = []
n = int(input("Enter number of pages : "))
f = int(input("Enter number of frames : "))
for i in range(n):
    l.append(int(input(f"Enter page {i+1} : ")))
pages = []
fault = 0
for i in range(n):
    if len(pages)<f:
        if l[i] not in pages:
            pages.append(l[i])
            fault+=1
    else:
        if l[i] not in pages:
            a = []
            for j in range(i+1,n):
                if len(a)<f-1:
                    if l[j] in pages:
                        a.append(l[j])
            a = set(a)
            s = set(pages)
            rep = list(s-a)[0]
            pages[pages.index(rep)]=l[i]
            fault+=1
print("Number of faults is", fault)