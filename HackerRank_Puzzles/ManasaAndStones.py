import sys
def ManasaAndStones(n,a,b): # fisrt stone =0
    stone=[0]
    for i in xrange(n-1):
        stone=[item + j for j in [a,b] for item in stone]
        stone=list(set(stone))
    return sorted(list(set(stone)))


mat=[]
T=input()
for i in xrange(T):
    n=input()
    a=input()
    b=input()
    mat.append([n,a,b])
m=0
for i in xrange(len(mat)):
    stone= ManasaAndStones(mat[m][0],mat[m][1],mat[m][2])
    mat.remove(mat[m])
    for j in xrange(len(stone)) :
        sys.stdout.write(str(stone[m]))
        stone.remove(stone[m])
        sys.stdout.write(" ")
    sys.stdout.write("\n")






    
