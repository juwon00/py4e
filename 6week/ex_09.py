fname = input('Enter File: ')

if len(fname) < 1:
    fname = 'clown.txt'
    
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        
        # if w in di:
        #     di[w] = di[w] + 1
        # else:
        #     di[w] = 1
        
        
        
        # if the key is not there th count is zero
        
        # oldcount = di.get(w,0)
        # print(w, 'old', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        # print(w, 'new', newcount)
        
        
        
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        # print(w, di[w])


# now we want to find the most common word
largest = -1
theword = None
for k,v in di.items():
    if v > largest:
        largest = v
        theword = k #cature/remember the key that was largest
        
print(theword, largest)