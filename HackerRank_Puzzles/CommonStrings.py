"""
Write a program that gives count of common characters presented in an array of strings..(or array of character arrays)
For eg.. for the following input strings..
aghkafgklt
dfghako
qwemnaarkf

The output should be 3. because the characters a, f and k are present in all 3 strings.
Note: The input strings contains only lower case alphabets

"""

def CommonStrings(N) : # N is an array of strings
    for i in xrange(len(N)):
        if i==0 :
            s1=set(" ".join(N[i]).split())
        elif i>0 :
            s2=set(" ".join(N[i]).split())
            s1=s1.intersection(s2)
    return len(s1)

N=['aghkafgklt','dfghako','qwemnaarkf ']
print CommonStrings(N)

            
