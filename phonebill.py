l=[]
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(int(input())):
    log=input()
    n=log.split(',')
    l.append(n)
for i in l:
    time=i[0].split(':')
    num=i[1].split('-')
    timetotal=int(time[0])*60*60 + int(time[1])*60 + int(time[2])
    if(time[0]=='00' and time[1]=='05' and time[2]=='00' or time[0]=='00' and time[1]=='04' and time[2]=='60'):
        l1.append(750)
    elif(time[0]=='00' and int(time[1])<5):
        l1.append(timetotal*3)
    elif(int(time[1])>=5 and int(time[2])>0):
        l1.append((int(time[1])+1)*150)
    else:
        l1.append(int(time[1])*150)
    l2.append(timetotal)
    l3.append(''.join(num))
m=list(zip(l1,l2,l3))
l3=set(l3)
l3=list(l3)
for i in l3:
    bill=0
    for j in m:
        if(j[2]==i):
           bill+=j[0]
    l4.append(bill)
m1=list(zip(l3,l4))
m1=sorted(m1,key=lambda x:x[1],reverse=True)
print(m,m1)
