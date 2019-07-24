n=[]
a=input("Enter a string : ")
for i in a:
    n.append(i)
n.sort()
s=set(n)
l1=list(s)
l1.sort()
l=[]
for i in l1:
    l.append(n.count(i))
z=l.index(max(l))
l.remove(max(l))
l1.remove(l1[z])
p=l.index(max(l))
print(l1[p])

