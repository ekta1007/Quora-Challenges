def MinimumStepsToOne(N):
    Memo=[-1]*N
    print Memo
    if N==1 :
        Memo[N-1]=0
        return 0
    if Memo[N-1]!=-1 :
        r= Memo[N-1]
        return r
    r= 1+ MinimumStepsToOne(N-1)
    if (N%2)==0 :
        r= min(1,MinimumStepsToOne(N/2))
    if (N%3)==0 :
        r= min(1,MinimumStepsToOne(N/3))
    Memo[N-1]=r
    return r , Memo
print MinimumStepsToOne(2)
