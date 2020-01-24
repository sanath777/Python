n=input()
n.replace(' ','')
n=n.split(';')
data=[]
for i in n:
    data.append(i.split('$'))
day=[]
war=[]
data2=[]
for i in data:
    day.append(i[0])
    a=i[1].split(':')
    war.append(a)
war3=[]
for i in war:
    war2=[]
    for j in i:
        war2.append(j.split('-'))
    war3.append(war2)

default=['N','S','W','E']
for i in range(len(day)):
    direct=[]
    for j in default:
        direction=[]
        for l in war3[i]:
            if(j in l[1]):
                direction.append(int(l[3]))
        if(direction!=[]):
            direct.append(max(direction))
        else:
            direct.append(0)
    data2.append(direct)
m=list(zip(day,data2))

q=m[0]
default1=q[1]
count=0
for i in default1:
    if(i>0):
        count+=1
for i in data2[1:]:
    if(i[0]>default1[0]):
        count+=1
        default1[0]=i[0]
    if(i[1]>default1[1]):
        count+=1
        default1[1]=i[1]
    if(i[2]>default1[2]):
        count+=1
        default1[2]=i[2]
    if(i[3]>default1[3]):
        count+=1
        default1[3]=i[3]

print(m)
print(count)



#day1$t1-n-x-5:t2-w-x-7:t3-n-x-1:t2-w-x-9;day2$t1-s-x-3;day3$t1-e-x-12
#Day1$T1-S-X-4:T1-N-X-2:T3-W-X-3;Day2$T2-S-X-5:T2-N-X-1:T3-N-X-3;Day3$T1-W-X-2:T1-W-X-4:T2-N-X-3:T2-S-X-4
