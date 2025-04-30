# l = [2,3,1,5,2,6,1,10,5,5,12]
#print duplicates
# x=[]
# print(l.count())
# for i in l:
#    if l.count(i) > 1:
       # print(i)
       # x.append(i)
# print(i)

#
# l = [2,3,1,5,2,6,1,10,5,5,12]
# x = set()
# y = set()
# # y = set()
# # y = set(l)
# # # print(y)
# for i in l:
#     if i in x:
#         y.add(i)
#     else:
#         x.add(i)
# print("Duplicate values", list(y))

""""""
# s = "5"
# m = "15"
# n = int(s) +int(m)
# print(n)


""""""
# s = "srinivasulu"

#PRINT IN REVERSE
# print(s[::-1])

#FINDIND EVEN VALUES USING STEPPING
# print(s[0:11:2])

# FINDIND VOWELS
# v=('a','e','i','o','u')
# for i in s:
#      if i in v:
#          print(i)


#JOINING THE ELEMENTS
# l = ["a","s","s","e","t"]
# x = "". join(l)
# print(x)
# x = ""
# for i in l:
    # x += i
    # x = x+i
# print(x)


# a = [1,3,5,7,9]
# b = [2,4,6,8,10]
# c = []
# a.extend(b)
# print(a)
# a = sorted(a)
# print(a)
# print(len(a))
# print(a)
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)


# a = {"a":1,"b":2}
# for i,j in a.items():
#     print(i,j)



# a=[1,4,3,2,1,5,4,6,3,7,8,7]
#
# dic={}
# for i in a:
#     if i not in dic:
#         dic[i]=1
#
#     else:
#         dic[i]+=1
#
# print(dic)

#using get write one dictionary
company ={"name": "BMW", "model": "7 series", "year": "2024"}
name = company.get("name")
model = company.get("model")
price_with_default = company.get("price","Not provided")
print(name)
print(model)
print(price_with_default)












