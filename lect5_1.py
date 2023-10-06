#1
"""
qlist = []

def enqueue(qlist, data):
    qlist.append(data)

def dequeue(qlist):
    data = qlist[0]
    del qlist[0]
    return data

enqueue(qlist, 1)
print(qlist)

enqueue(qlist, 2)
print(qlist)

enqueue(qlist, 3)
print(qlist)

dequeue(qlist)
print(qlist)
"""

#arr
"""
arr = [1, 2, 3, 4, 5]

def ret_01(idx):
    return arr[idx]

print(ret_01(2))

"""

#3
"""
import time
arr = [1, 2, 3, 4, 5]

def print_elements(arr):
    for elem in arr:
        print(elem)

start = time.time()
print_elements(arr)
end = time.time

print(f"{end - start : 5f} sec")
"""


#time
"""
def ret_01(idx):
    return arr[idx]


start = time.time()
print(ret_01(2))
end = time.time()
print(f"{end - start : 5f} sec")
""
"""

#arr
"""
arr = [1, 2, 3, 4, 5]

def print_elements(arr):
    for elem in arr:
        print(elem)

print_elements(arr)

"""


# o
"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(left, right)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
"""
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""
my_list = [1, 2, 3, 4, 5]

result = binary_search(my_list, 4)
if result != -1:
    print(f"요소가 {result}번째 인덱스에 있습니다.")
else:
    print("요소를 찾을 수 없습니다.")
"""

# mul_for
"""
import time

def mul_for():
        for i in range(5):
            for j in range(5):
                print(i, j)

start = time.time()
mul_for()
end = time.time()
print(f"{end - start : 5f} sec")
"""


#
"""
def bubble_sort(arr) :
    N = len(arr) # 데이터의 갯수 : 5
    for i in range(N): # 0,1,2,3,4
        # print(i, arr)
        for j in range(N-i-1): #4,3,2,1
            if arr[j] > arr[j+1]: # arr[4]
                #print(arr[j+1, ])
                arr[j], arr[j+1] = arr[j+1],arr[j]
            print(i, j, arr, arr[i], arr[j])

    return arr

lrr = [1, 9, 2, 7, 5]
print(bubble_sort(lrr)) # [-1, 0, 9, 11, 45]
"""

"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("piv ", pivot)
    print("left ", left)
    print("mid ", middle)
    print("rgt ", right)

    return quick_sort(left) + middle + quick_sort(right)

my_list = [1, 9, 6, 4, 5, 7, 3, 2]
print(len(my_list))

sorted_list = quick_sort(my_list)

print(sorted_list)

"""
"""
import requests

res = requests.get('<https://www.google.com>')
print(res)
"""



#numpy
"""
import numpy as np
#1
a = np.array([1, 2, 3])
print(a)

#2
b = np.zeros((2, 3))
print(b)

#2차 3핼 배얼, 1로 초기화
c = np.ones((2, 3))
print(c)


d = np.array([1, 2, 3])
e = np.array([4, 5, 6])

#배얼간 연산
f = d + e
g = d - e
h = d * e
i = d / e

print(f)
print(g)
print(h)
print(i)

"""
#pandas
"""
import pandas as pd

data = {'Name': ['John', 'Jane', 'Mike', 'Sarah'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print(df)



# age 관련숙성
print(df['Age'].describe())

#Spot the datafram by age in descending order
print(df.sort_values(by='Age', ascending = False))
print("===============")
print(df.sort_values(by='Age', ascending = True))
print("===============")
print(df.sort_values(by='Name', ascending = True))

"""

#matplotlib
import matplotlib.pyplot as plt

#Create examlpe data
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]


#  Plot the data
plt.plot(x, y)

# Add labels and tiltle
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Example plot')

#Show the plot
plt.show()


