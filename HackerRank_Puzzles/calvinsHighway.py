def CalvinsHighway(N,width,entry_exit):
    return min(width[entry_exit[0]:(entry_exit[1]+1)])

entry_exit=[]
N, T = raw_input().split()
N, T = int(N), int(T)
width=raw_input().split()
width=[int(item) for item in width]
for t in xrange(T):
    i,j=raw_input().split()
    i,j=int(i),int(j)
    entry_exit.append([i,j])
# for each i,j print the largest segment that is allowed
for t in xrange(T):
    print CalvinsHighway(N,width,entry_exit[t])

    
