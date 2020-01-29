import time
start_time = time.time()

sentences=[["how are you doing"],["Tom Like you doing"],["Like are you Tom"]]
queries=[["how you"],["Like Tom"]]

def Solution(sentences,queries):
    l1=[set(i[0].split(" ")) for i in sentences]
    l2=[set(i[0].split(" ")) for i in queries]
    
    for i in l2:
        c=0
        for j in l1:
            if i.issubset(j):
                print(l1.index(j),end=' ')
                c=1
        print()
        if c==0:
            print(-1)
        
    print("--- %s seconds ---" % (time.time() - start_time))

Solution(sentences,queries)
