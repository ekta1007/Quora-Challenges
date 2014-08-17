#maximum subset using Kadane's algorithm
def maxsum(N): # N is an array
    neg=[]
    pos=[]
    for i in xrange(len(N)):
        print i
        if N[i] <0:
            neg.append(N[i])
        elif N[i]>=0 :
            pos.append(N[i])
    # next pick all +ves
    if len(pos)>0:
        sum_max = sum(pos)
    elif len(pos)==0 and len(neg)>0 :
        sum_max=0 # max sum is empty subset, if that is allowed
        #sum_max=sorted(neg,reverse=True)[0]
    return sum_max
N=[1,2,5,6,-9,7]
print maxsum(N)
    
            
        
