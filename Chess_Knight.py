import itertools

def attack(i,j,l):
    try:
        l[i+2][j+1][1]+=1
        if(j-1)>=0:
            l[i+2][j-1][1]+=1
        if(i-2)>=0:
            l[i-2][j+1][1]+=1
        if(j-1)>=0 or (i-2)>=0:
            l[i-2][j-1][1]+=1
        l[i+1][j+2][1]+=1
        if(j-2)>=0:
            l[i+1][j-2][1]+=1
        if (i-1)>=0:
            l[i-1][j+2][1]+=1
        if(j-2)>=0 or (i-1)>=0:
            l[i-1][j-2][1]+=1
    except Exception as e:
        p=1
    return l
            
class Chess:
    def __init__(self):
        self.l=[]
        for i in range(1,9):
            l1=[]
            q=97
            for j in range(8):
                l2=[]
                strs=chr(q)+''+str(i)
                l2.append(strs)
                l2.append(0)
                l1.append(l2)
                q+=1
            self.l.append(l1)
        
    def match(self,a):
        for i in range(1,9):
            q=97
            for j in range(8):
                strs=chr(q)+''+str(i)
                q+=1
                for i1 in a:
                    if i1==strs:
                        self.l=attack(i-1,j,self.l)
                        break
        return self.l
        
        
    def display(self):
        self.l=[print(*i) for i in self.l]
        

if __name__=="__main__":
    a=input().split(' ')
    obj=Chess()
    chess_board=obj.match(a)
    count=0
    max_el=[]
    for j in chess_board:
        for i in j:
            if i[1]==0:
                count+=1
            else:
                m=[]
                m.append(i[1])
                m.append(chess_board.index(j))
                m.append(j.index(i))
                max_el.append(m)
    
    
    print(count)
    m=sorted(max_el,key=lambda x:x[0],reverse=True)
    if m[0][0]!=m[1][0]:
        print(chess_board[m[0][1]][m[0][2]][0])
    else:
        print('-1')
    
        
    #obj.display()
    
