def ReverseSentence(sentence):
    tokens=sentence.split()
    reversed_tok=[]
    j=len(tokens)-1
    for i in xrange(0,len(tokens)):
        if i <=j :
            tokens= tokens[0:i]+[tokens[j]]+tokens[i+1:j]+[tokens[i]]+tokens[j+1:]
            #print tokens
            #reversed_tok.append(tokens[j]+tokens[i+1:j]+tokens[i])
            #tokens=reversed_tok
            j=j-1
    print tokens
sentence="the house is blue"
#ReverseSentence(sentence)


def ReverseString(string):
    j=len(string)-1
    for i in xrange(0,len(string)):
        if i <=j :
            string= string[0:i]+string[j]+string[i+1:j]+string[i]+string[j+1:]
            j=j-1
    print string
string="thehouse"
ReverseString(string)
