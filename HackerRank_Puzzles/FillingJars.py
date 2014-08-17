# we need to find avg, why store in individual columns ?
def FillingJars(N,M,mat):
    sum_jar=0
    for m in xrange(M):
        a,b,k=mat[m][0],mat[m][1],mat[m][2]
        sum_jar=(b-a+1)*k+sum_jar
    return int(sum_jar/N)
# Average of all candies in the Jars now
    
mat=[]
N,M=[int(item) for item in raw_input().split()]#,int(M)# M operations on N jars
for m in xrange(M):
    a,b,k=[int(item) for item in raw_input().split()]
    mat.append([a,b,k])
print FillingJars(N,M,mat)


