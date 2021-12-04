a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def bubbleSort(a):
    l = len(a)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

def binarySearch(a):
    value = int(input())
    
    mid = len(a) // 2
    low = 0
    high = len(a) - 1
    
    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid - 1
        else:
            high = mid - 1
        mid = (low + high) // 2
        
    if low > high:
        print('No value')
    else:
        print("ID = ", mid)
        
bubbleSort(a)
print(a)
binarySearch(a)
print(a)