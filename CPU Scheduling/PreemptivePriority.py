from concurrent.futures import process
import queue
from re import S


n=int(input("enter no of process: "))
d=dict()
for i in range(n):
    key="P"+str(i+1)
    a=int(input("enter arrival time of process "+key+": "))
    b=int(input("enter burst time of process "+key+": "))
    c=int(input("Enter priory of process "+key+": "))
    l=[]
    l.append(a)
    l.append(b)
    l.append(0)
    l.append(c)
    l.append(0)#4 et
    l.append(0)#5 wt
    l.append(0)#6 tat
    l.append(b)#7 copyof burst time
    d[key]=l
d=sorted(d.items(),key=lambda item:item[1][0])
print(d)
s_time=0
seqp=[]
while 1:
    rq=[]
    temp=[]
    nq=[]
    for j in range(len(d)):
        if(d[j][1][0]<=s_time and d[j][1][2]==0):
            rq.append(d[j])
        elif d[j][1][2]==0:
            nq.append(d[j])
    if(len(rq)==0 and len(nq)==0):
        break
    if len(rq)!=0:
        rq.sort(key=lambda x:x[1][3],reverse=True)
        #print(rq)
        cpy=s_time
        s_time+=1

        seqp.append(rq[0][0])
        for k in range(len(d)):
            if(d[k][0]==rq[0][0]):
                break
        d[k][1][1]=d[k][1][1]-1
        if(d[k][1][1]==0):
            d[k][1][2]=1
            d[k][1][4]=s_time
    if len(rq)==0:
        nq.sort(key=lambda item:item[1][0])
        if s_time<nq[0][1][1]:
            s_time=nq[0][1][1]
        cpy=s_time
        s_time+=1
        for k in range(len(d)):
            if(d[k][0]==nq[0][0]):
                break
        d[k][1][1]=d[k][1][1]-1
        if(d[k][1][1]==0):
            d[k][1][2]=1
            d[k][1][4]=s_time
avg_tat=0
for i in range(len(d)):
    d[i][1][6]=d[i][1][4]-d[i][1][0]
    avg_tat+=d[i][1][6]
avg_tat/=n
avg_wt=0
for i in range(len(d)):
    d[i][1][5]=d[i][1][6]-d[i][1][7]
    avg_wt+=d[i][1][5]
avg_wt/=n
print("PROCESS  | ARRIVAL | BURST | PRIORITY | EXIT TIME | WT  |  TAT")
for i in range(n):
    print(" ",d[i][0]," | ",d[i][1][0],"  |  ",d[i][1][7],"  |  ",d[i][1][3],"  |  ",d[i][1][4],"  |  ",d[i][1][5],"  |  ",d[i][1][6])
print("Averge Turn around time: ",avg_tat)
print("Average waiting time: ",avg_wt)
print(seqp)