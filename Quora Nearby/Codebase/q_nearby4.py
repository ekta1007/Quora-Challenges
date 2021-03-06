# -*- coding: utf-8 -*-
# Author : Ekta Grover 
# Problem Statment - "Quora Nearby", see also attached document in the folder
from datetime import datetime
startTime = datetime.now()
import timeit
import collections #collections.defaultdict(dict)
import math , operator, sys
#from itertools import takewhile, count
#import ast
"""All imports below used to profile - time,memory & memory leaks """
#import psutil
#import objgraph
#objgraph.show_most_common_types()
#objgraph.show_growth()
#import pdb; pdb.set_trace()
#from memory_profiler import profile # use if using profiling from cmd line


pow_custom=math.pow
sqrt_custom=math.sqrt
round_custom=round

#Scope for Improvement : Better data structures & reading through the list (N_matrix) - I assume for 1000 rows it can get very slow
# Design corner cases - solve the 0.001 threshold & also trim down the distance returned to that for comparision
# Timing on largest output  all under 5 secs , see also the q_CreateTestData.py file
# Read problem statement more carefully
# unit tests
# see the floating, if better solution to that
# MOST IMPORTANTLY MEET TIME !

"""
A short note on time profiling -
At the loss of loosing generality with ast.literal_eval(), I acheived the following with the "transform function"
Function: ReadInputIntoMatrices

#Orignal approach using ast.literal_eval(), which does tree level parsing to identify the type of the object
Total time: 0.000336 s
Time  Per Hit   % Time
172     43.0     51.2

# Transformed T_matrix using transform_T function 
Total time: 0.000214 s
Time  Per Hit   % Time
33      8.2     15.4 

After this, I also transformed N_matrix for doing away with ast.literal_eval(), here's what I achieved -:
Total time: 0.000336 s (as teh status quo bechmark, before)
Time  Per Hit   % Time
91     45.5     27.1
14      4.7      4.2

# Transformed T_matrix using transform_N function 
Total time: 0.000102 s  # Whoo ! what an improvement compared to 0.000336 s earlier 
Time  Per Hit   % Time
22      7.3     21.6


Usage for profiling : When using line_profiler via "kernprof.py -l -v q_nearby.py" , it writes the profile results to q_nearby.py.lprof
# Then to view the results "python -m line_profiler q_nearby.py.lprof"
Notes : To run in Idle, you need to comment out the decorators for profiling the individual functions
TODO : from profilehooks import coverage, profile

Usage for Memory profiling(from Shell) :  python -m memory_profiler q_nearby3.py
(from IDLE, should use from memory_profiler import profile) Gives lesser floating point numbers, so preferable to use from shell promt
Also note that it is prerable to use "psutil" for memory profiling, otherwise memory_profiler will be slow.


Usage for detecting memory leakage : objgraph
The way this works is that "the cPython interpreter uses reference counting as it’s main method of keeping track of memory. This means that every object contains a counter, which is incremented when a reference to the object is stored somewhere, and decremented when a reference to it is deleted. When the counter reaches zero, the cPython interpreter knows that the object is no longer in use so it deletes the object and deallocates the occupied memory."
We will detect these memory leaks using "objgraph"
More precisely, objgrapgh does the following -:
show the top N objects occupying our python program’s memory
show what objects have been deleted or added over a period of time
show all references to a given object in our scrip

See also a quick primer on Profiling - http://www.huyng.com/posts/python-performance-analysis/

Alternatively, we can also generate & see the running time using
python -m cProfile -o timeStats.profile q_nearby4.py  # This generates the timeStats.profile in the same folder as the q_nearby4.py
python -m pstats timeStats.profile # view the profile using an interactive profile statistics browser. Just key in the name of the function to see the time it took, etc.
"""
"""
#@profile
def transform_T(element): #element is a list
    yield int(element[0]), float(element[1]),float(element[2])
#@profile
def transform_N(element): #element is a list
    yield element[0], int(element[1]),float(element[2]),float(element[3])

"""
"""
Commented out the status quo approach with ast.literal_eval, for you to compare when profiling the individual functions, for both T_matrix & N_matrix
"""
#@profile
def ReadInputIntoMatrices(data):
    flag = True 
    for item in data :
        if item.split() !=[] :
            if flag == True : # read 1st line
                T, Q, N = [int(i) for i in item.split()]
                t,q,n=0,0,0
                T_matrix,N_matrix,Q_matrix=[],[],[]
                flag = False
            elif t <T and flag == False : # store all values in a matrix
                T_matrix.append(int(element[0]), float(element[1]),float(element[2]))
                #T_matrix.append(transform_T(item.split()))
                t=t+1
            elif t==T and q<Q:
                Q_matrix.append([int(item_val) for item_val in item.split()])
                q=q+1
            elif  t==T and q==Q and n <N :
                N_matrix.append(element[0], int(element[1]),float(element[2]),float(element[3]))
                #N_matrix.append(transform_N(item.split()))
                n=n+1  
        else :
            break       
    return T_matrix,Q_matrix,N_matrix


def ReadInputIntoMatricesForTestData(data):
    flag = True 
    for item in data.next() :
        #print item
        if flag == True :
            T, Q, N = [int(i) for i in item]
            t,q,n=0,0,0
            T_matrix,N_matrix,Q_matrix=[],[],[]
            flag = False
        elif t <T and flag == False : # store all values in a matrix
            T_matrix.append(item)
            t=t+1
        elif t==T and q<Q:
            Q_matrix.append(item)
            q=q+1
        elif  t==T and q==Q and n <N :
            N_matrix.append(item)
            n=n+1  
        else :
            break
    #print "T_matrix,Q_matrix,N_matrix"
    #print T_matrix,Q_matrix,N_matrix
    return T_matrix,Q_matrix,N_matrix


def ReadInputIntoMatricesFromFilehandle(filehandle):
    file_open =open(filehandle, 'r')
    with file_open as f:
        T,Q,N = map(int, next(f).split())
        T_matrix=[transform_T(next(f).split()) for i in xrange(T)]
        Q_matrix=[map(int,next(f).split()) for i in xrange(Q)] # I know Q will never have floats/strings, else could use ast.literal_eval
        N_matrix=[transform_N(next(f).split()) for i in xrange(N)]
    return T_matrix,Q_matrix,N_matrix

#@profile
def MinDistanceCandidates(T_matrix,Q_matrix,N_matrix):
    query_dict,topic_dict=collections.defaultdict(dict),collections.defaultdict(dict)#collections.defaultdict(lambda : collections.defaultdict(dict)) # dict of a dict in Python#collections.defaultdict(lambda : collections.defaultdict(dict))
    dict_lat_long_q, dict_lat_long_t={},{}#collections.defaultdict(dict)
    for row in N_matrix :# Force to read the 'q' the row 1st, can have multiple 'q' rows, need to build an abstraction for this
        for topic_IdRows in T_matrix : 
            """ store all the lat-long seeked, for both 'q' & 't' queries - contains (lat, long) as key & rows_needed as value"""
            topic_dict[(row[-2],row[-1])][topic_IdRows[0]]=round_custom(sqrt_custom(pow_custom((topic_IdRows[-2]-row[-2]),2)+pow_custom((topic_IdRows[-1]-row[-1]),2)),3)
        if row.__contains__('q') :
            dict_lat_long_q[(row[-2],row[-1])]=row[1] # storing the needed rows in another dict for quick reference
            for row_InQmatrix in Q_matrix: # for each question in Q_matrix , write only min dist for all topics associated with that question
                for item in row_InQmatrix[2:]:
                    if query_dict[(row[-2],row[-1])].has_key(row_InQmatrix[0]) and topic_dict[(row[-2],row[-1])][item]<query_dict[(row[-2],row[-1])][row_InQmatrix[0]]:
                        query_dict[(row[-2],row[-1])][row_InQmatrix[0]] = topic_dict[(row[-2],row[-1])][item]
                    else :
                        query_dict[(row[-2],row[-1])][row_InQmatrix[0]] = topic_dict[(row[-2],row[-1])][item]
        elif row.__contains__('t') :
            dict_lat_long_t[(row[-2],row[-1])]=row[1]            
    # keeping this, since I "ate" one loop, will see if I can discard this all-together
    """
    for row in N_matrix :
        if row.__contains__('q') :
            for row_InQmatrix in Q_matrix: # for each question in Q_matrix , write only min dist for all topics associated with that question
                for item in row_InQmatrix[2:]:
                    if query_dict[(row[-2],row[-1])].has_key(row_InQmatrix[0]) and topic_dict[(row[-2],row[-1])][item]<query_dict[(row[-2],row[-1])][row_InQmatrix[0]]:
                        query_dict[(row[-2],row[-1])][row_InQmatrix[0]] = topic_dict[(row[-2],row[-1])][item]
                    else :
                        query_dict[(row[-2],row[-1])][row_InQmatrix[0]] = topic_dict[(row[-2],row[-1])][item]# fetch the dist for the corresponding topic id for that lat-long
    """
    # Now just return the q & t for lat-long queried
    for row in N_matrix :
        if query_dict.has_key((row[-2],row[-1])):
            print[item[0] for item in sorted(query_dict[(row[-2],row[-1])].items() , key=lambda x: (x[1],-x[0]))][0:dict_lat_long_q[(row[-2],row[-1])]]
        elif topic_dict.has_key((row[-2],row[-1])):
            print [item[0] for item in sorted(topic_dict[(row[-2],row[-1])].items() , key=lambda x: (x[1],-x[0]))][0:dict_lat_long_t[(row[-2],row[-1])]]


def ReadFromStdin():
    data=[]
    while True :
        line = sys.stdin.readline()
    if line:
        data.append(line)    
    else:                                                     
        T_matrix,Q_matrix,N_matrix=ReadInputIntoMatrices(data)
        #print T_matrix,Q_matrix,N_matrix
        if T_matrix and Q_matrix and N_matrix :
            MinDistanceCandidates(T_matrix,Q_matrix,N_matrix)
        sys.exit(0)

#### READ from Stdin, filehandle, or the test data generated using####

# Read using Stdin
ReadFromStdin()

# OR read from filehandle
filehandle='/home/ekta/Github_Repositories/Quora Challenges/Quora Nearby/Input Files/q_input_orignal.txt'
T_matrix,Q_matrix,N_matrix=ReadInputIntoMatricesFromFilehandle(filehandle)
MinDistanceCandidates(T_matrix,Q_matrix,N_matrix)

# OR read the largest possible input to time it
execfile("/home/ekta/Github_Repositories/Quora Challenges/Quora Nearby/Codebase/q_CreateTestData.py")
#T,Q,N=10000,1000,10000
#data=CreateTestData(T,Q,N)
data=CreateTestData(13,4,5)
T_matrix,Q_matrix,N_matrix=ReadInputIntoMatricesForTestData(data)
MinDistanceCandidates(T_matrix,Q_matrix,N_matrix)

print(datetime.now()-startTime)

#filehandle='/home/ekta/Github_Repositories/Quora Challenges/Quora Nearby/Input Files/q_input_orignal.txt'
#T_matrix,Q_matrix,N_matrix=ReadInputIntoMatrices(filehandle)

"""
#For profiling using objgraph
MinDistanceCandidates(T_matrix,Q_matrix,N_matrix)
objgraph.show_backref() # to show backreferencing
objgraph.show_backref([T_matrix], filename="/home/ekta/Github_Repositories/Quora Challenges/Quora Nearby/Input Files/backrefs.png")
"""
