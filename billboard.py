from asyncio.windows_events import NULL
import sys
import numpy as np


arrayLength = input("Enter array length: ")

try:
    arrayLength = int(arrayLength)
except:
    print('invalid array length')
    sys.exit()

inputArrayStr = input("Enter array: ")
array = []
inputArray = inputArrayStr.split(' ')

try: 
    for i in range(arrayLength):
        array.append(int(inputArray[i]))
    array = np.array(array)
except:
    print('invalid array')
    sys.exit()

print(array)

# def billboard(arr):
#     arr.sort()
#     max = int(sum(recur(arr))/2)
#     print('billboard', arr, max)
#     return findEqual(arr, max)

# def recur(arr):
#     print('recur', arr)
#     max = sum(arr)/2
#     if arr[-1] > max:
#         print('recur', arr[:-1])
#         return recur(arr[:-1])
#     firstOddIndex = NULL
#     alreadyDefined = False
#     countOdd = 0
#     for i in range(len(arr)):
#         if arr[i]%2 == 1: 
#             countOdd += 1
#             if (not alreadyDefined):
#                 firstOddIndex = i
#                 alreadyDefined = True
#     if countOdd%2 == 1: 
#         arr = np.delete(arr, firstOddIndex)
#     return arr

def billboard(arr):
    return findEqual(arr, int(sum(arr)/2))

def findEqualRecur(arr1, target, arr2):

    if target == 0:
        return arr2
    if target < 0:
        return []
    if sum(arr1) == target:
        return np.append(arr1,arr2)
    if len(arr1) == 0:
        return []
    
    arr2Copy1 = arr2.copy()
    arr2Copy2 = arr2.copy()
    list1 = findEqualRecur(arr1[:-1],target - arr1[-1], np.append(arr2Copy1, arr1[-1]))
    list2 = findEqualRecur(arr1[:-1],target, arr2Copy2)
    if len(list1) != 0:
        return list1
    elif len(list2) != 0:
        return list2
    else:
        return []

def findEqual(arr, target):
    if target == 0:
        return 0
    if len(arr) == 0:
        return 0
    list1 = findEqualRecur(arr, target, np.array([]))
    if sum(list1) == target:
        arrCopy = arr.copy()
        for item in list1:
            pointer = np.where(arrCopy == item)
            arrCopy = np.delete(arrCopy, pointer[0][0])
        print(arr, arrCopy)
        list2 = findEqualRecur(arrCopy, target, np.array([]))
        if sum(list2) == target:
            return target
    return findEqual(arr, target-1)

# print(billboard(array))
# print(len(l))
# print(findEqualRecur(array, 10, l))
# s = int(sum(array)/2)

print(billboard(array))
