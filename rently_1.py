import time
def getRes(sent, ph): 
    sentHash = dict() 
  
    # Loop for adding hased sentences to sentHash 
    for s in range(1, len(sent)+1): 
        sentHash[s] = set(sent[s-1].split()) 
          
    # For Each Phrase 
    for p in range(0, len(ph)): 
        print("Phrase"+str(p + 1)+":") 
  
        # Get the list of Words 
        wordList = ph[p].split() 
        res = [] 
  
        # Then Check in every Sentence 
        for s in range(1, len(sentHash)+1): 
            wCount = len(wordList) 
  
            # Every word in the Phrase 
            for w in wordList: 
                if w in sentHash[s]: 
                    wCount -= 1
  
            # If every word in phrase matches 
            if wCount == 0: 
  
            # add Sentence Index to result Array 
                res.append(s) 
        if(len(res) == 0): 
            print("NONE") 
        else: 
            print('% s' % ' '.join(map(str, res))) 
  
# Driver Function 
def main(): 
    s="Sentences are an array of words"
    sent = ["Strings are an array of characters", 
    "Sentences are an array of words"] 
    for i in range(10000):
        sent.append(s)
    t1=time.time()
    ph = ["an array of", "sentences are strings"] 
    getRes(sent, ph) 
    print(time.time()-t1)
main()
