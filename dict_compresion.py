new_dict = {x:x**3 for x in range(5)}
# print(new_dict)

#
dict = {x:x+3 for x in range(10) if x%1 == 0}
# print(dict)
#
l="chc"
dic = {x:{y:x+y for y in l}for x in l}
# print(dic)
# dic
x = {x:x-2 for x in range(20) if x > 3}
# print(x)
#
keys=['a','b','c','d']
values=[1,2,3,4]
my_dict = {k:v for(k,v)in zip(keys,values)}
# print(my_dict)