#K total cuts - to be distributed in Horizontal & vertical 
def HaloweenParty(K):
    if K==1:
        return 0
    elif K==2:
        return 1
    else :
        vertical=K/2
        horizontal=K-(K/2)
        return vertical*horizontal
K=[]
i=0
T=input()
for t in xrange(T):
    K.append(input())
while len(K)!=0:
    print HaloweenParty(K[i])
    K.remove(K[i])
