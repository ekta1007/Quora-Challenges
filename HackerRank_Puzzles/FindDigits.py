def FindDigits(n):
    if n ==0:
        return 0
    # find unique digits in n - dont count for now
    digit_list, dict_digit,count=[],{},0
    N=n
    while n%10 >=0 and n!=0:
        digit_list.append(n%10)
        n=n/10
    for i in xrange(len(digit_list)) :
        if digit_list[i] in dict_digit.keys():
            dict_digit[digit_list[i]]=1+dict_digit[digit_list[i]]
        else :
            dict_digit[digit_list[i]]=1
     #now count how many integers in dict_digit divide "n"
    for key in dict_digit.keys():
        if key !=0 and N%key ==0 :
            count=count+dict_digit[key]
    return count
mat=[]
T=input()
for i in xrange(T):
    mat.append(input())
for j in xrange(len(mat)):
    print FindDigits(mat[j])


