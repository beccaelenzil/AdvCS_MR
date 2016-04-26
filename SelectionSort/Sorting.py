import time
import random
some_list = [4,3,6,2]

def createRandomList(myList):
    for i in range(len(myList)):
        x = random.randint(0,100);
        myList[i] = x
    return myList

def quickSort(myList, start, stop):
    if stop-start < 1:
        return
    else:
        pivot = myList[0]
        left = start
        right = stop
        while left <= right:
            while myList[left] < pivot:
                left += 1
            while myList[right] > pivot:
                right -= 1
            if left <= right:
                myList[right],myList[left] = myList[left],myList[right]
                left += 1
                right -=1
            #print(some_list)

        quickSort(some_list, start, right)
        quickSort(some_list, left, stop)
    return myList

my = createRandomList(some_list)
my = quickSort([39,30,45,33,20,61,36,5,31,64], 0, 5)
print my

def insertionSort(some_list):
    list = some_list
    k = len(list) - 1
    flip = True
    while flip == True:
        flip = False
        for i in range(0,k):
            if list[i] > list[i+1]:
                list[i+1], list[i] = list[i], list[i+1]
                flip = True
        k -= 1

def selectionSort(some_list):
    i = 0
    x = 0
    smallest_value = i
    for i in range(len(some_list)):
        for j in range(i+1,len(some_list)):
            if some_list[j] < some_list[smallest_value]:
                smallest_value = j
            some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
            x+=1
    time.sleep(1)
    print(some_list)
    print x

def bubbleSort(some_list):
    list = some_list
    k = len(list) - 1
    flip = True
    while flip == True:
        flip = False
        for i in range(0,k):
            if list[i] > list[i+1]:
                list[i+1], list[i] = list[i], list[i+1]
                flip = True
        k -= 1



