n=1
while(n==1):
    n1=input()
    n2=input()
    if len(n1)>=50 or len(n2)>=50:
        print("Re-enter Strings")
    else:
        break
if n1==n2:
    print("Equal")
else:
    print("Not Equal")

    
