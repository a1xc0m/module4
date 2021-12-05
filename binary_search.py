from random import randint

n = 10
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

bubbleSort(a)
print('Sort array: ', a)

def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
                
    return found

testlist = a
b = int(input('Search value: '))
print(binarySearch(testlist, b))
