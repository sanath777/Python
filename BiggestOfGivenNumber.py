n=int(input("Enter n value"))
s1=input()
s=[]
s=s1.split(" ")
temp=0
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        a=int(s[i])
        b=int(s[j])
        if(a>b):
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
temp=0
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        a=s[i]
        b=s[j]
        if(int(a[0])<int(b[0])):
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
        else:
            if(int(a[0])==int(b[0])  and int(a)//10!=0 and int(b)//10!=0 and int(a[1])<int(b[1])):
                temp=s[i]
                s[i]=s[j]
                s[j]=temp
            
for i in s:
    print(i,end='')
            
    

