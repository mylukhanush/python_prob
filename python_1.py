#Write a Python program to do arithmetical
# operations addition and division.
# a = float(input("Enter the first number for  addition: "))
# b = float(input("enter the second number for addition: "))
# result = a + b
# print(f"sum: {a} + {b} = {result}")

# c = float(input("enter the dividend for division:"))
# d = float(input("enter the divisior for division:"))
# if d == 0:
#     print("Error: Division by zero is not allowed: ")
# else:
#     resutl = c / d
#     print(f"division: {c} / {d} = {resutl}")


#Write a Python program to do arithmetical operations
# addition and division.
# kilometers = float(input("enter the distance in kilometers:"))
# conversion_factor = 0.621371
# miles = kilometers * conversion_factor
# print(f"{kilometers} kilometers is equal to {miles} miles")

#Write a Python program to display calendar
# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# cal = calendar.month(year, month)
# print(cal)

#write a python program to check if a number
# is positive,negative or zero
# num = float(input("Enter a number: "))
# if num > 0:
#     print("positive number")
# elif num == 0:
#     print("zero")
# else:
#     print("Negative number")

# write a python program to check if a number is odd or even
# num = int(input("Enter a number:"))
# if num%2 == 0:
#     print("This is a even number")
# else:
#     print("This is a odd number")

#write a python program to check leap year
# year = int(input("Enter year:"))
# if(year % 400 ==0) and (year %100 == 0):
#     print("{0} isz a leap year".format(year))
# elif (year % 4 == 0) and (year % 100 != 0):
#     print("{0} is ia leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))

#wwrite a python program to print all prime numbers
# in an interval of 1-10
# lower = 1
# upper = 10
# print("prime numbers between", lower, "and", upper, "are:")
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# write a python program to display the multiplication table
# num = int(input("Display multiplication table of: "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")



#write a python program to calculate your body mass index
# def bodymassindex(height, weight):
#     return round((weight / height**2),2)
# h = float(input("Enter your height in meters: "))
# w = float(input("Enter your weight in kg: "))
# print("welcome to the BMI calculator. ")
# bmi = bodymassindex(h, w)
# print("your BMI is: ", bmi)
# if bmi <= 18.5:
#     print("you are underweight.")
# elif 18.5 < bmi <= 24.9:
#     print("your weight is normal.")
# elif 25 < bmi <= 29.29:

#     print("you are overweight.")
# else:
#     print("you are obese.")


#write a python program to check Armstrong Number
# num = int(input("Enter a number: "))
# num_str = str(num)
# num_digits = len(num_str)
# sum_of_powers = 0
# temp_num = num
# while temp_num > 0:
#     digit = temp_num % 10
#     sum_of_powers += digit ** num_digits
#     temp_num //=10
# if sum_of_powers == num:
#     print(f"{num} is an Armstrong nunber.")
# else:
#     print(f"{num} is not an Armstrong number


#write a python program to find the sum of natural numbers
# limit = int(input("Enter the limit: "))
# sum = 0
# for i in range(1, limit + 1):
#     sum += i
# print("The sum of natural numbers up to", limit, "is:", sum)


# Write a Python Program to calculate the natural logarithm
# of any number.
# import math
# num = float(input("Enter a number: "))
# if num <= 0:
#     print("Please enter a positive number.")
# else:
#     result = math.log(num)
#     print(f"The natural logarithm of {num} is: {result}")

# Write a Python Program for cube sum of first n
# natural numbers?
# def cube_sum_of_natural_numbers(n):
#     if n <= 0:
#         return 0
#     else:
#         total = sum([i**3 for i in range(1, n+1)])
#         return total
# n = int(input("Enter the value of n: "))
# if n <= 0:
#     print("please enter a positive integer.")
# else:
#     result = cube_sum_of_natural_numbers(n)
#     print(f"The cube sum of the first {n} natural numbers is: {result}")


# Write a Python Program to find largest element in an array.
# def find_largest_element(arr):
#     if not arr:
#         return "Array is empty"
#     largest_element = arr[0]
#     for element in arr:
#         if element > largest_element:
#             largest_element = element
#     return largest_element
# my_array = [10, 20, 30, 99]
# result = find_largest_element(my_array)
# print(f"The largest element in the array is: {result}")

# Write a Python Program to check if given array is Monotonic.
# def is_monotonic(arr):
#     increasing = decreasing = True
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i - 1]:
#             decreasing = False
#         elif arr[i] < arr[i - 1]:
#             increasing = False
#     return increasing or decreasing
# arr1 = [1, 2, 2, 3]
# arr2 = [3, 2, 1]
# arr3 = [1, 3, 2, 4]
# print("arr1 is monotonic:", is_monotonic(arr1))
# print("arr2 is monotonic:", is_monotonic(arr2))
# print("arr3 is monotonic:", is_monotonic(arr3))

# Write a Python Program to Add Two Matrices.
# def add_matrices(mat1, mat2):
#     if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
#         return "Mstrices must have the same dimensions for addition"
#     result = []
#     for i in range(len(mat1)):
#         row = []
#         for j in range (len(mat1[0])):
#             row.append(mat1[i][j] + mat2[i][j])
#         result.append(row)
#     return result
# matrix1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# matrix2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
# result_matrix = add_matrices(matrix1, matrix2)
# if isinstance(result_matrix, str):
#     print(result_matrix)
# else:
#     print("sum of matrices:")
#     for row in result_matrix:
#         print(row)

# write a python program to Transpose a matrix
# def transpose_matrix(matrix):
#     rows, cols = len(matrix), len(matrix[0])
#     result = [[0 for _ in range(rows)]for _ in range(cols)]
#     for i in range(rows):
#         for j in range(cols):
#             result[j][i] = matrix[i][j]
#     return result
# matrix = [[1, 2, 3],[4, 5, 6]]
# transposed_matrix = transpose_matrix(matrix)
# for row in transposed_matrix:
#     print(row)


# Write a Python Program to Sort Words in Alphabetic Order.
# x = input("Enter a string: ")
# words = [word.capitalize() for word in x.split()]
# words.sort()
# print("The sorted words are:")
# for word in words:
#     print(word)


# Write a Python program to print even numbers in a list.
# x = range(11)
# even_numbers = [num for num in x if num % 2 == 0]
# print("Even numbers in the x: ", even_numbers)

# Write a Python program to Remove empty List from List.
# def is_binary_str(input_str):
#     for i in input_str:
#         if i not in '01':
#             return False
#     return True
# input_str = "1001110"
# if is_binary_str(input_str):
#     print(f"'{input_str}' is a binary string.")
# else:
#     print(f"'{input_str}' is not a binary string.")

#write a programme to merge two Dictionaries
# x = {'a' : 1, 'b' : 2}
# y = {'c' : 3, 'd' : 4}
# x.update(y)
# print("Merged Dictionary (using update()):",

# Write a program that accepts a sentence and calculate the
# number of letters and digits. Suppose the following
# input is supplied to the program:
# x = input("Enter a sentence: ")
# letter_count = 0
# digit_count = 0
# for char in x:
#     if char.isalpha():
#         letter_count += 1
#     elif char.isdigit():
#         digit_count += 1
# print("LETTERS", letter_count)
# print("DIGITS", digit_count)

# Write a program which takes 2 digits, X,Y as input and generates
# a 2-dimensional array. The element value in the i-th row
# and j-th column of the array should be i*j.
# x, y = map(int, input("Enter two digits (x, y): ").split(','))
# array = [[0 for j in range (y)]for i in range(x)]
# for i in range(x):
#     for j in range(y):
#         array[i][j] = i * j
# for row in array:
#     print(row)


# Write a program that accepts a sentence and calculate
# the number of letters and digits.
# sentence = input("Enter a sentence: ")
# letter_count = 0
# digit_count = 0
# for char in sentence:
#     if char.isalpha():
#         letter_count += 1
#     elif char.isdigit():
#         digit_count += 1
# print("LETTERS", letter_count)
# print("DIGITS", digit_count)

#Write a Python program to sort Python Dictionaries by
# Key or Value.
#SORTED BY KEYS
# sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
# sorted_dict_by_keys = dict(sorted(sample_dict.items()))
# print("Sorted by keys:")
# for key,value in sorted_dict_by_keys.items():
#     print(f"{key}: {value}")
#
# #SORTED BY VALUES
# sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'data': 4}
# sorted_dict_by_values = dict(sorted(sample_dict.items()))
# print("Sorted by values:")
# for key, value in sorted_dict_by_values.items():
#     print(f"{key}: {value}")

# Write a Python program to insertion at the
# beginning in OrderedDict.
# from collections import OrderedDict
# ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
# new_item = ('a', 1)
# new_ordered_dict = OrderedDict([new_item])
# new_ordered_dict.update(ordered_dict)
# print("update OrderedDict:", new_ordered_dict)

#Write a Python program to find the sum of
# all items in a dictionary.
# my_dict ={'a': 10,'b': 20,'c': 30,'d': 40,'e': 50}
# total_sum = 0
# for i in my_dict.values():
#     total_sum += i
# print("Sum of all item in the dictionary:",total_sum)

# Write a Python program to find all
# duplicate characters in string.
# def find_duplicates(input_str):
#     char_count = {}
#     duplicates= []
#     for i in input_str:
#         if i in char_count:
#             char_count[i] += 1
#         else:
#             char_count[i] = 1
#     for i, count in char_count.items():
#         if count > 1:
#             duplicates.append(i)
#     return duplicates
# input_string = "piyush sharma"
# duplicate_chars = find_duplicates(input_string)
# print("Duplicate characters:", duplicate_chars)

# Write a python program to check if a given string is
# binary string or not