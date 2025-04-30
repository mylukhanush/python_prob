i = 2
while i < 10:
    print(i)
    i+=2

j = 20
while j < 200:
    print(j)
    if j == 200:
        continue
    j += 10

k = 2
while k < 48:
    print(k)
    k += 2
else:
    print("k is no longer less than 6 ")

fruits = ["apple","banana","orange","kiwi"]
for x in fruits:
    if x == "orange":
        pass
    print(x)
#BREAK
cars = ["verna","polo","porchse"]
for x in cars:
    if x == "polo":
        break
    print(x)

#CONTINUE
for x in cars:
    if x == "polo":
        continue
    print(x)


#ELSE
for x in cars:
    if x == "polo":
         continue
    print(x)
else:
    print("i love polo")
