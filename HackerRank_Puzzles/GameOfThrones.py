def GameOfThrones(string):
    dict_local={}
    count=0
    for char in string:
        if char in dict_local.keys():
            dict_local[char]=dict_local[char]+1
        else :
            dict_local[char]=1
    for val in dict_local.values():
        if val%2 ==1 :
            odd=val
            count=count+1
            if count >= 2 :
                return "NO"
    return "YES"
        
string=raw_input()
print GameOfThrones(string)

