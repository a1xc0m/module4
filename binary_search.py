from random import randint

n = int(input('Size array: '))
a = [randint(0, 100) for i in range(n)]
print('Getting array: ', a)

def bubbleSort(a):
    l = len(a)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        mid = (first + last) // 2
        
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            last = mid - 1
        elif list[mid] < item:
            first = mid + 1

bubbleSort(a)
print('Sort array: ', a)
b = int(input('Search value: '))
print(binarySearch(a, b))
