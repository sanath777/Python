class Node:  
    def __init__(self, data): 
        self.data = data  
        self.next = None  
  
class LinkedList: 
    def __init__(self): 
        self.head = None

def printList(l): 
    for i in l:
        print("Node ----",l.index(i)+1,"----",i.data) 


def reverse(l):
    l=[i for i in l[::-1]]
    for i in range(len(l)-1):
        l[i].next=l[i+1]
    return l

def insert(l,pos,data):
    l.insert(pos,Node(data))
    for i in range(len(l)-1):
        l[i].next=l[i+1]
    return l

def delete(l,data):
    for i in l:
        if i.data==data:
            l.remove(i)
    for i in range(len(l)-1):
        l[i].next=l[i+1]
    return l
l=[]
x=[12,233,445,878,232,343,4,34,2323,2334,334]
for i in x: 
    l.append(Node(i))
for i in range(len(l)-1):
    l[i].next=l[i+1]
printList(l)
print()
printList(reverse(l))
print()
printList(insert(l,2,'sdcsa'))
print()
printList(delete(l,4))
print()


           








