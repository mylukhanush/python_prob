l = ["porcshe","bmw","merc","bentley"]
l1 = [x if x!="bmw" else "mustang"for x in l]
print(l1)
#SUGS
l2=[y for y in l]
print(l2)
#HBHS
l3=[x for x in l1 if x!="porcshe"]
print(l3)
#ESGGS
l4 = [x for x in l1 if x=="bentley"]
print(l4)
#UPPER
l5 = [x.upper() for x in l1]
print(l5)
#LOWER
l6=[x.lower() for x in l1]
print(l6)
#DICT
names = ['hp','dell','lenovo']
prices = [60,50,70]

res = (zip(names,prices))
print(dict(res))