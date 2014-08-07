#Author : Ekta Grover

"""
Test using sample data to time the code, analyze performance & coverage
Constraints/Range of possible inputs
1 <= T <= 10000
1 <= Q <= 1000
1 <= N <= 10000
Integer ids are between 0 and 100000 inclusive.
Number of topics associated with a question is not more than 10.
The number of results required for a query is not more than 100.
0.0 <= x,y <= 1000000.0 (10^6)
For the large testcases, all topic x,y co-ordinates will be approximately uniformly distributed over the bounds.
You should aim to have your algorithm be fast enough to solve our largest test inputs in under 5 seconds, or be as close to that as possible.
"""
import numpy as np
from itertools import chain #list(chain.from_iterable(list_to_unchain))

global T,Q,N,geo_lat,geo_long,q_topics,q_results
T,Q,N=10000,1000,10000
geo_lat,geo_long=(0.0,1000000.0),(0.0,1000000.0)
q_topics=10 # topics with a question are not more than 10
q_results=100

# To sample floating numbers between a different range(uniform distribution), use (b - a) * random_sample() + a
# To sample integers, use np.random.random_integers(geo_lat[0],geo_lat[1],size=None<or specify>)

# create a dataset T,Q,N in that order
def CreateTestData(t,q,n):
    data = [[] for _ in range(t+q+n+1)]
    data[0].extend([t,q,n])
    for i in xrange(1,t+q+n+1):
        if  i<=t :
            data[i].extend([i-1,float(format((geo_lat[1]-geo_lat[0])* np.random.random_sample()+geo_lat[0],'.1f')) , float(format((geo_lat[0]-geo_lat[1])* np.random.random_sample()+geo_lat[1],'.1f'))])
        elif i >t and i <=t+q :#for i in xrange(q):
            number_topics=np.random.randint(q_topics)# np.random.choice(t, number_topics, replace=False)
            # Topics with a question can't be more than q_topics
            data[i].extend([i-1-t ,number_topics])
            if number_topics >0:
                data[i].extend(list(np.random.choice(t, number_topics, replace=False))) # select any of "t" questions of size "topic_ids"
        elif i>t+q : #for i in xrange(n):
            topics_associated=np.random.randint(0,q_results)
            type_query='t' if np.random.rand() > 0.5 else 'q'
            data[i].extend([type_query ,topics_associated, float(format((geo_lat[1]-geo_lat[0])* np.random.random_sample()+geo_lat[0],'.1f')) , float(format((geo_lat[0]-geo_lat[1])* np.random.random_sample()+geo_lat[1],'.1f'))])
    yield data

# test the profiling
import profile
profile.run('CreateTestData(13,3,4)')

# Call this from the main file 
"""
data=CreateTestData(13,3,4)
print list(data)
print "new one"
data=CreateTestData(T,Q,N)
print list(data)
"""
#execfile("/home/ekta/Github_Repositories/Quora Challenges/Quora Nearby/Codebase/q_CreateTestData.py") 
