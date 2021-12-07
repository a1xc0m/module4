from random import randint

n = int(input('Size array: '))
a = [randint(0, 100) for i in range(n)]
print('Getting array: ', a)

def insertionSort(a):
    for i in range(len(a) - 1):
        j = i - 1
        key = a[i]
        while a[j] > key and j >= 0:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    return
            
insertionSort(a)
print('Result: ', a)
            
            