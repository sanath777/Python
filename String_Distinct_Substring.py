def max_d_char(string, n): 
    count = [0] * 256
    for i in range(n): 
        count[ord(string[i])] += 1
      
    max_d = 0
    for i in range(256): 
        if (count[i] != 0): 
            max_d += 1    
      
    return max_d 
 
if __name__ == "__main__": 
    string=input()
    if len(string)>=1 and len(string)<=10**5:
        n = len(string) 
        max_d = max_d_char(string, n) 
        m= n
    
        for i in range(n): 
            for j in range(n): 
                s = string[i:j] 
                s1 = len(s) 
                s2 = max_d_char(s,s1) 
      
                if(s1<m and max_d==s2): 
                    m=s1
        print(m)
    else:
        print("String Length Constraint met 1<=S<=10^5")
    
