# Need to come back on this again 
"""
A 'Decent' Number has -
1. Only 3 and 5 as its digits.
2. Number of times 3 appears is divisible by 5.
3. Number of times 5 appears is divisible by 3.
"""
# optimize the runtime of this program
global element_of_interest
element_of_interest=[3,5]
elements_not_of_Interest=range(0,10)
elements_not_of_Interest.remove(element_of_interest[0])
elements_not_of_Interest.remove(element_of_interest[1])

            
    
def AllDigits(list_digits): # this function owns the responsibilty of checking if any other numbers apart from 3 & 5 are in the list
    if element_of_interest[0] in list_digits or element_of_interest[1] in list_digits :
        return True

def NumberTimes(list_digits):
    dict_digits={}
    dict_digits[element_of_interest[0]]=0
    dict_digits[element_of_interest[1]]=0
    try :
        dict_digits[element_of_interest[0]]=list_digits.count(element_of_interest[0])
        dict_digits[element_of_interest[1]]=list_digits.count(element_of_interest[1])
        if dict_digits[element_of_interest[0]]%element_of_interest[1]==0 and dict_digits[element_of_interest[1]]%element_of_interest[0]==0 :
            return True
        else :
            return False
    except Exception as e:
        print "failing here with %s " %e
    
def FindDigits(N):
    list_digits=[]
    if N==0 :
        print "Number is Zero, trivial case Skipping"
        return False
    while N%10>=0 and N>0:
        list_digits.append(N%10)
        N=N/10
    return list_digits

def SherlockandTheBeast(n): # n is the no. of digits in that number, we still have to find the number
    try :
        high_val=(10**n)-1
        low_val=(10**(n-1))
        num=high_val
        flag=False
        flag_inner=True
        while num >=low_val :
            for item in elements_not_of_Interest: # first check if other elements exists
                if str(num).find(str(item))>-1:
                    flag_inner=False
                    break
            if flag_inner==True:
                print "num candiadates %d " %num
                list_digits=FindDigits(num)
                if AllDigits(list(set(list_digits))) and NumberTimes(list_digits) :
                    flag=True
                    return num
            num=num-1
        if not flag :
            return -1
    except Exception as e:
        print "caught %s "%e
print SherlockandTheBeast(3)

"""
mat=[]
T=input()
for i in xrange(T):
    mat.append(input())
for j in xrange(len(mat)):
    print SherlockandTheBeast(mat[j])
"""

