def Permutation(N): # N is an int for which we generate perms
    #digit=FindDigits(N)
    if len(N)==0:
        return ''
    elif len(N)==1:
        return str(N)
    elif len(N)>0 :
        return ([N[i]+k],[k+N[i]] for i in xrange(len(N)) for k in Permutation(N[i+1:]))
    #[(chars[i]+ k) for i in xrange(len(chars)) for k in Permutation(chars[i+1:]), (k2+ chars[i2]) for k2 in Permutation(chars[i+1:]) for i2 in xrange(len(chars))]
        #chars[i] + k for k in Permutation(chars[i+1:])
        #j for j in Permutation(chars[i+1:])+chars[i]
        #return ((chars[i]+ item for item in Permutation(chars[i+1:]))for i in xrange(len(chars)))
        #return chars[i] + k for k in Permutation(chars[i+1:]) for i in xrange(len(chars))
    
"""
def FindDigits(N):
    digit=[]
    while N%10 >=0 and N >0:
        digit.append(N%10)
        N=N/10
    return digit
"""
N="981" # or N =98
#chars=" ".join(str(N)).split()
#digit=FindDigits(N)
gen= Permutation(N)
print gen
 
