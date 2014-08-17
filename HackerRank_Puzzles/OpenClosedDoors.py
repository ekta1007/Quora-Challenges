def OpenClosedDoors(N):
    #initialize all doors as closed
    N_arr=[0]*(N+1)
    M=range(1,N+1)
    m=0
    for n in xrange(1,N+1):      
        for i in xrange(n,N+1,M[m]*n):
            if N_arr[i]==0:
                N_arr[i]=1
            elif N_arr[i]==1:
                N_arr[i]=0
    return N_arr
def print_1(N_arr):
    for i in xrange(1,len(N_arr)):
        if N_arr[i]==1:
            print i
N_arr= OpenClosedDoors(6)
print N_arr
print_1(N_arr)


            
        
        
