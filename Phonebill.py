n=int(input("Enter No. of Logs : "))
l=[]
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(0,n):
    a=input("Enter log : ")
    l.append(a)
for i in l:
    a=i
    a1=i
    a=a[2:10]
    a1=a1[13:25]
    n1=a.split(':')
    n2=a1.split('-')
    l1.append(n1)
    l2.append(n2)
mins=0
bill=0
for i in l1:
    mins=(int(i[0])*3600)
    mins=mins+(int(i[1])*60)
    mins=mins+int(i[2])
    l4.append(mins)
    if(int(i[1])<5):
        bill=mins*3
    elif(int(i[1])<=5):
        bill=mins*5
    else:
        bill=mins*6
    l3.append(bill)
for i in


mins=max(l4)
q=l4.index(mins)
l3[q]=0
for i in range(0,n):
    print("Customer - {} call duration={} and Bill amount={}".format(i+1,l4[i],l3[i]))
