print('---- exercise 1 ----', '\n')

# 1. Define the id of next variables:

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))


# ----------------------------------
print('\n', '---- exercise 2 ----', '\n')

# 2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d.append(4)
lst_d.append(5)

print(id(lst_d))


# ----------------------------------
print('\n', '---- exercise 3 ----', '\n')

# 3. Define the type of each object from step 1.

print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))


# ----------------------------------
print('\n', '---- exercise 4 ----', '\n')

# 4*. Check the type of the objects by using isinstance.
# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

wrk_string = "Anna has ___ apples and ___ peaches."

wrk_string = wrk_string.replace('___ apples', '4 apples').replace('___ peaches', '6 peaches')

print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

print(wrk_string)


# ----------------------------------
print('\n', '---- exercise 5 ----', '\n')

# 5. With .format and curly braces {}

print("Anna has {} apples and {} peaches.".format(3, 5))


# ----------------------------------
print('\n', '---- exercise 6 ----', '\n')

# 6. By passing index numbers into the curly braces.

print("Anna has {0} apples and {1} peaches.".format(7, 1))


# ----------------------------------
print('\n', '---- exercise 7 ----', '\n')

# 7. By using keyword arguments into the curly braces.

print("Anna has {apples_nmbr} apples and {peaches_nmbr} peaches.".format(apples_nmbr=1, peaches_nmbr=9))


# ----------------------------------
print('\n', '---- exercise 8 ----', '\n')

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0:5} apples and {1:3} peaches.".format(3, 3))


# ----------------------------------
print('\n', '---- exercise 9 ----', '\n')

# 9. With f-strings and variables

usr_apples = 8
usr_peaches = 1

print(f"Anna has {usr_apples} apples and {usr_peaches} peaches.")


# ----------------------------------
print('\n', '---- exercise 10 ----', '\n')

# 10. With % operator

usr_ap = 8
usr_pe = 1

print("Anna has %s apples and %s peaches." % (usr_pe, usr_ap))


# ----------------------------------
print('\n', '---- exercise 11 ----', '\n')

# 11*. With variable substitutions by name (hint: by using dict)

a = 6
p = 2
user_dict = {'apple': a, 'peach': p}

print("Anna has %(apple)s apples and %(peach)s peaches." % (user_dict))


# ----------------------------------
print('\n', '---- exercise 12 ----', '\n')

# 12. Convert (1) to list comprehension
'''
Comprehensions:
(1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
'''

list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]

print(list_comprehension)


# ----------------------------------
print('\n', '---- exercise 13 ----', '\n')

# 13. Convert (2) to regular for with if-else
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

lst = []

for num in range(10):

    if num % 2 == 0:
        lst.append(num // 2)

    else:
        lst.append(num * 10)

print(lst)


# ----------------------------------
print('\n', '---- exercise 14 ----', '\n')

# 14. Convert (3) to dict comprehension.
'''
(3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
'''

d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}

print(d)


# ----------------------------------
print('\n', '---- exercise 15 ----', '\n')

# 15*. Convert (4) to dict comprehension.
'''
(4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
'''

d_2 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}

print(d_2)


# ----------------------------------
print('\n', '---- exercise 16 ----', '\n')

# 16. Convert (5) to regular for with if.
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}

dict_comp = {}

for x in range(10):

    if x ** 3 % 4 == 0:
        dict_comp[x] = x ** 3

print(dict_comp)


# ----------------------------------
print('\n', '---- exercise 17 ----', '\n')

# 17*. Convert (6) to regular for with if-else.
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

dict_comp_2 = {}

for x in range(10):

    if x ** 3 % 4 == 0:
        dict_comp_2[x] = x ** 3

    else:
        dict_comp_2[x] = x

print(dict_comp_2)


# ----------------------------------
print('\n', '---- exercise 18 ----', '\n')

# 18. Convert (7) to lambda function
'''
Lambda:
(7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y
'''

foo = lambda x, y: x if x < y else y

print(foo(3, 6))


# ----------------------------------
print('\n', '---- exercise 19 ----', '\n')

# 19*. Convert (8) to regular function
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

def foo_2(x, y, z):

    if y < x and x > z:
        return z

    else:
        return y

print(foo_2(3, 7, 1))


# ----------------------------------
print('\n', '---- exercise 20 ----', '\n')

# 20. Sort lst_to_sort from min to max

lst_to_sort_20 = [5, 18, 1, 24, 33, 15, 13, 55]

print(sorted(lst_to_sort_20))


# ----------------------------------
print('\n', '---- exercise 21 ----', '\n')

# 21. Sort lst_to_sort from max to min

lst_to_sort_21 = [5, 18, 1, 24, 33, 15, 13, 55]

print(sorted(lst_to_sort_20, reverse=True))


# ----------------------------------
print('\n', '---- exercise 22 ----', '\n')

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

lst_to_sort_22 = [5, 18, 1, 24, 33, 15, 13, 55]

print(list(map(lambda x: x * 2, lst_to_sort_22)))


# ----------------------------------
print('\n', '---- exercise 23 ----', '\n')

# 23*. Raise each list number to the corresponding number on another list:

list_A = [2, 3, 4]
list_B = [5, 6, 7]

print(list(map(pow, list_A, list_B)))


# ----------------------------------
print('\n', '---- exercise 24 ----', '\n')

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

from functools import reduce


list_to_sort_24 = [5, 18, 1, 24, 33, 15, 13, 55]

print(reduce(lambda x, y: x + y, list_to_sort_24))


# ----------------------------------
print('\n', '---- exercise 25 ----', '\n')

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

list_to_sort_25 = [5, 18, 1, 24, 33, 15, 13, 55]

print(list(filter(lambda elem: elem % 2 == 1, list_to_sort_25)))


# ----------------------------------
print('\n', '---- exercise 26 ----', '\n')

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

print(list(filter(lambda i: i < 0, range(-10, 10))))


# ----------------------------------
print('\n', '---- exercise 27 ----', '\n')

# 27*. Using the filter function, find the values that are common to the two lists:

list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

print(list(filter(lambda i: i in list_2, list_1)))
