def Utopian_trees(stage,start_height,n):
    if n>0 :
        if stage=="moonsoon":
            start_height=start_height*2
            stage="summer"
        elif stage=="summer":
            start_height=1+start_height
            stage="moonsoon"
        return Utopian_trees(stage,start_height,n-1)
    elif n==0:
        return start_height
    return start_height
T=input()
N=[]
for line in xrange(T):
    N.append(input())
for n in N:
    print Utopian_trees("moonsoon",1,n)

