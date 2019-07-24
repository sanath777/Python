n=int(input("Enter n value : "))
l=[]
print("Enter The List Elements : ",end='\n')
for i in range(0,n):
    a=int(input())
    l.append(a)
l.sort()
z=l[0]
x=0
l1=[]
for i in range(0,len(l)):
    if(l[i]==z):
        z+=1
    else:
        x=0
        l1.append(z)
        z+=2
if(x==0):
    print(l1)
else:
    print("No Missing Elements")
        
