import sys
sys.setrecursionlimit(100000)
# lessons learnt - Max recursion depth in Python by default is 999, so we may choose to set this.
# Base case of cross over- to avoid invalid string indexes, by checking i==j & i<j. Also, the cost in base case=cost+0
def dict_alphabet():
    i=0
    dict_alpha={}
    for key in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        dict_alpha[key]=i+1
        i=i+1
    return dict_alpha


def LoveLetterMystery(letter,i,j,cost,dict_alpha):
    if i==j: # stop if i=j, trival case, or when cross-over has occured
        cost=cost+0
        return cost
    # we either change the corresponding index in left half, or the correponding index right half, based on costs & consideration of reduce b=>a is valid, but not a=>b
    elif i<j and dict_alpha[letter[i]]<dict_alpha[letter[j]]: # i<j change "j" till it equals i
        cost=cost+(dict_alpha[letter[j]]-dict_alpha[letter[i]])
        letter=letter[0:j]+letter[i]+letter[j+1:] # since we replaced j with i
        cost=LoveLetterMystery(letter,i+1,j-1,cost,dict_alpha)
    elif i<j and dict_alpha[letter[i]]>dict_alpha[letter[j]] :
        cost=cost+(dict_alpha[letter[i]]-dict_alpha[letter[j]])
        letter=letter[0:i]+letter[j]+letter[i+1:] # since we replaced i with j
        cost=LoveLetterMystery(letter,i+1,j-1,cost,dict_alpha)
    elif i<j and dict_alpha[letter[i]]==dict_alpha[letter[j]]:
        cost=LoveLetterMystery(letter,i+1,j-1,cost,dict_alpha)
    return cost

# Enter input strings
letter_list=[]
T=input()
for t in xrange(T):
    letter_list.append(raw_input())
dict_alpha=dict_alphabet()
i=0
while len(letter_list) != 0:
    try :
        print LoveLetterMystery(letter_list[i],0,len(letter_list[i])-1,0,dict_alpha)
        letter_list.remove(letter_list[i])
    except Exception as e:
        print e

        




    
