def BoBChoclate(N,C,M):
    no_choclates=N/C 
    no_wrapers=no_choclates
    while M<=no_wrapers: 
        more_choclates=no_wrapers/M 
        left_wrapers=no_wrapers%M
        no_choclates=no_choclates+more_choclates 
        no_wrapers=left_wrapers+more_choclates# 0+1+(no_wrapers-no_wrapers/M)
    if no_wrapers <M :
        return no_choclates

mat=[]
T=input()
for i in xrange(T):
    N,C,M=raw_input().split()
    N,C,M=int(N),int(C),int(M)
    mat.append([N,C,M])
for item in mat :
    print BoBChoclate(item[0],item[1],item[2])
    

