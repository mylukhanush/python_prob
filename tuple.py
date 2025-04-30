a = ("bunny",21,"nellore")
print(type(a))
b = ("mini",20,"gudur")
c = a + b
print(c)
print(a[0])
d=list(c)
d.remove("bunny")
print(d)
print(c)

print(d)
print(c)
print(c[0:3])
print(c[2:])
print(c[:4])
if "bunny" in c:
    print("true")
else:
    print("false")