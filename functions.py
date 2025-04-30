#A function is a block of code which only runs when it is called.
#you can pass data, known as parameters,into function.
# A function can return data as a result
# In Python function is defined using the 'def' keyword


# def non_parameterized_function_odd_even():
#     print("first line")
#     print("second line")
#     if 13%2 == 0:
#         print("odd")
#     else:
#         print("even")
#     print("second last line")
# non_parameterized_function_odd_even()
# print("last line")
# print("new news")
#
# def chk_class(avg):
#     if avg >= 90:
#         print("toppers")
#     elif avg>= 75 :
#         print("distinction")
#     elif avg>= 60:
#         print("first class")
#     elif avg >= 50:
#         print('second class')
#     elif avg >= 40:
#         print("just pass")
#     else:
#         print("fail")
# print(chk_class(94))
# print(chk_class(55))
# print(chk_class(79))
# print(chk_class(39))
# print(chk_class(65))
# def prime_number(num):
#     for i in range(2 ,num):
#         if num % i == 0:
#             return True
#         else:
#             return False
# print(prime_number(49))
# print(prime_number(48))
#
# def add(x,y):
#     return x + y
# result = add(5,3)
# print(result)
#
#  Function with Variable-Length Arguments
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
#
# Lambda Function (Anonymous Function)
# multiply = lambda x,y: x * y
# print(multiply(2,5))
#
# BUilt - in functions
# x = [1, 5, 2, 8, 3]
# print(len(x))
# print(max(x))
# print(min(x))
# print(sorted(x))
#
# try:
#     fname = input("Enter file name:")
#     fhand = open(fname)
# except:
#     if fname == 'na na boo boo':
#         print("NA NA BOO BOO TO U -you have been puink 'd!")
#     else:
#         print("Please enter correct file name:", fname)
# count = 0
# total = 0
# try:
#     for line in fhand:
#         if line.startswith("X-DSPAM-Confidence"):
#             count = count + 1
#             start = line.find(" ")
#             num = float(line[start:])
#             total += num
#     avg = total/count
#     print("Average spam confidence:",avg)
# except ZeroDivisionError:
#     print("C")
#
# x = input("Enter the file name:")
# try:
#     y = open(x)
# except:
#     print("File cannot be opened:",x)
#     exit()
# count = 0
# for line in y:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in',x)
#
# def myFun(*argv):
#     for arg in argv:
#         print(arg)
# myFun('Hello', 'Welcome', 'To','MY WORLD')
#
#
# def fun(*args):
#     return sum(args)
# print(fun(1, 2, 3, 4))
# print(fun(5, 10, 15))
# def fun(**kwargs):
#     for k, val in kwargs.items():
#         print(k, val)
# fun(a=1, b=2, c=3)
#
# def fun(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
# fun(1, 2, 3, a=4, b=5)
#
#
