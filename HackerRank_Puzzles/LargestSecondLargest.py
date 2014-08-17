def LargestSecondLargest(N): # N is an array
    largest=N[0]
    second_largest=N[1]
    for i in xrange(1,len(N)):
        if N[i]>largest :
            second_largest=largest
            largest=N[i]
        elif second_largest<N[i] :
            second_largest=N[i]
    print largest, second_largest
N=[-5,3,1,10,2,14]
LargestSecondLargest(N)
