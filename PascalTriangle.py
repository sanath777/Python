l1=[0]
l2=[1]
print(*l2)
for i in range(8):
    l2=[x+y for x,y in zip(l1+l2,l2+l1)]
    print(*l2)
