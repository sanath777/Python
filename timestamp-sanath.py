n=int(input("Enter n value : "))
l1=[]
for i in range(0,n):
      a=input()
      l1.append(a)
l2=[]
for i in range(0,len(l1)):
    a=l1[i]
    a=a[1:len(a)-1]
    l2.append(a.split(','))
max1=0
l3=[]
for i in range(0,len(l2)):
    b=l2[i]
    if(b[2]=='enter'):
        max1=max1+int(b[1])
        l3.append(max1)
    elif(b[2]=='exit'):
        max1=max1-int(b[1])
        l3.append(max1)
z=max(l3)
c=l3.index(z)
q=l2[c]
print(q[0],end=' ')
for i in range(c,len(l3)):
    if l3[i]<z:
        c1=l3.index(l3[i])
        q1=l2[c1]
        break
print(q1[0])


    
