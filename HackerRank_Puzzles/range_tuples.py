"""
Given a list of tuples representing intervals, return the range these intervals
covered.
e.g:
[(1,3), (2,5),(8,9)] should return 5
"""
def range_tuples(N): # N is a list of tuples
    l=[]
    for i in xrange(len(N)):
        if i ==0:
            s1=set(xrange(N[i][0],N[i][1]+1))
        else :
            s2=set(xrange(N[i][0],N[i][1]+1))
            s1=s2.union(s1)
    s1=sorted(list(s1))
    max_continous=0
    low=s1[0]
    k=0
    # now find the max continuos array from this s1, set
    for j in xrange(len(s1)-1):
        if s1[j+1]-s1[j]==1:
            high=s1[j+1]
            print "high iside ok"
            print high
            max_continous = high-low+1
            print "max_continous %d" %max_continous 
            pass
        elif s1[j+1]-s1[j]>1:
            low=high
            high=s1[j+1]
            print "low,high"
            print low,high
            max_continous = high-low+1
    return max_continous

N=[(1,3), (5,6),(8,9)]
print range_tuples(N)
"""
1 2 3
2 3 4 5
8 9
1 2 3 4 5 8 9
"""
                 
        
        
