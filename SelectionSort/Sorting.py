import time
import random
some_list = [4,3,6,2]

def createRandomList(some_list):
    for i in range(len(some_list)):
        x = random.randint();
        some_list[i] = x

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



