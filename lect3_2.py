"""
x = [1, 2, 3]
y = [1, 2, 3]
z = x   

print(x is y)
print(x is z)
print(x is not y)   
"""


"""
a = 5
b = 5

print(a is b)
print(a is not b)
"""


"""
a = 3
b = 3.0

print(a ==b)
print(a is b)
print(a is not b)
"""
    
    
"""    
a = [3, 5, 1]
b = a
print(a is b)

a[0] = 2

print(a, b)

print(a is b)
"""


"""# a = 2 + 3 * 4
print(a)
# a = 10 / 5 / 2
print(a)
# a = 2 ** 3 ** 2
print(a)
# a = 10 % 3 % 2
print(a)
# a = 1 + 2 > 3 and 4 - 1 < 2
print(a)
# a = not False and True
print(a)
# a = not True or False add True
print(a)
# a = 1 & 2 | 3 ^ 4
print(a)
# a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
print(a)
# a = 2 * -3 // 2
print(a)
# a = 1 == 2
print(a)
# a = FALSE != 3
print(a)"""


"""
x = 10

if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is zero")
"""

"""
num = 23
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
"""


"""
a = 2 
b = 3
if a == b:
    print("같습니다")
else:
    print("다릅니다")
"""


"""    
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
"""


"""
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)
"""


"""
for i in range(18) :
    print(i)
"""


"""
for char in "Python":
    print(char)
"""


"""
for fruit in reversed(fruits):
    print(fruit)
"""


"""
for fruit in sorted(fruits, reverse=True):
    print(fruit)
"""
"""
for i in range(1, 10):
    fro "j" in range(1, 10):
    print(i, "x", j, "=", i*j)
"""


"""
rang = [5, 8, 3, 1, 6]

for i in rang:
    print("element : ", i)
else :
    print("edd Process")
"""


"""
for i in range(10):
    if i == 7:
        print("break ", i)
        break
    elif i == 1:
        print("continue ", i)
        continue
    else:
        print("pass ", i)
        pass
    print(i)
"""


""" 
i = 1

while i <= 5:
    print(i)
    i += 1
"""
 
 
"""
i = 1

while i <= 9:
    print(i)
    i += 1
"""


"""
str_word = "python"
i = 0 

while i < len(str_word):
    print(str_word[i])
    i += 1
"""


"""sum = 0
i = 1

while i <= 10:
    sum += i
    i += 1
print(sum)
"""


"""
i = 100
for num in range(1, i + 1):
    if num % 2 != 0:
        print(num)

"""


"""
i = 100 
for num in range (2, i + 1 ,2):
    print(num)
"""
i =1
while i <= 100:
    if i % 2 == 0:
        print("짝수 : ", i)
    elif i % 2 == 1:
        print("홀수 : ", i)
    i += 1