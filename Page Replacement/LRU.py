l = []
n = int(input("Enter number of pages : "))
f = int(input("Enter number of frames : "))
for i in range(n):
    l.append(int(input(f"Enter page {i+1} : ")))
pages = []
hit = 0
age = 0
ageList = []
for i, r in enumerate(l):
    age+=1
    if len(pages)<f:
        if r not in pages:
            pages.append(r)
            ageList.append(age)
    elif r in pages:
        hit += 1
        ageList[pages.index(r)]=age
    else:
        ind = ageList.index(min(ageList))
        pages[ind]=r
        ageList[ind]=age
print("Number of hits is", hit)