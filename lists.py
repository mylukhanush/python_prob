l1 = [1,2,3,4]
l2 = [5,6,7,8]
l1.append(12)
# print(l1)
l1.insert(2,"apple")
# print(l1)
l1.pop(2)
# print(l1)
l1.remove(2)
# print(l1)
l1.reverse()
# print(l1)
l3 = [12,13,14,15,[23,45,34,35],(65,76,66,"bunny"),[45,54,66]]
print(l3)
x = l3.copy()
# print(x)
#Shallowcopy and Deepcopy
import copy
b = copy.deepcopy(l3)
print(f"b={b}")
b[4][0]= 4
print(b)
print(l3)
print(len(b))
print(l1[3])
l1.extend(l3)
print(l1)