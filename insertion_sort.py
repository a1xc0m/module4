from random import randint

n = int(input('Size array: '))
a = [randint(0, 100) for i in range(n)]
print('Getting array: ', a)

def insertionSort(a):
    l = len(a)
    for i in range(1, l):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                temp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = temp
            else:
                break
            
insertionSort(a)
print('Result: ', a)