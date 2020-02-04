def bc(sums,l):
    for i in l:
        if sums%i==0:
            return 1
        
n=int(input())
s=set()
l=[3,5,10]
sums=0
c=0
if n==3 or n==5:
    print(1)
elif n in l:
    c=1
elif n>5:
    while(sums!=n):
        if bc(n-(sums+l[0]),l)==1:
            c+=1
        elif bc(n-(sums+l[1]),l)==1:
            c+=1
        elif bc(n-(sums+l[2]),l)==1:
            c+=1
        
    
