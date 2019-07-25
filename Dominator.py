n=int(input("Enter a Number : "))
l=[]
l1=[]
c={}
for i in range(0,n):
    a=int(input())
    l.append(a)
from collections import Counter
c=dict(Counter(l))
size=len(l)//2
for i in c.values():
    l1.append(i)
if(max(l1)>size):
    print(c[max(l1)])
else:
    print("No")
    
