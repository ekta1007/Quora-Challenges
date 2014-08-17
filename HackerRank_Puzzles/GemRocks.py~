def Gemrocks(gem):
    dict_local={}
    for i in xrange(len(gem)):
        if gem[i] not in dict_local.keys():
            dict_local[gem[i]]=1
        else:
            pass
    return dict_local.keys()

gem_list=[]
T=input()
for t in xrange(T):
    gem_list.append(raw_input())
i=0
flag=0
while len(gem_list) != 0:
    try :
        if flag==0:
            c1=Gemrocks(gem_list[i])
	    gem_list.remove(gem_list[i])
            flag=1
        elif flag ==1:
            c2=Gemrocks(gem_list[i])
            c1 = [item for item in c1 if item in c2 ]
            gem_list.remove(gem_list[i])
    except Exception as e:
        print e
print len(c1)

