import random
def BubbleSort(list):
    k = len(list) - 1
    flip = True
    while flip == True:
        flip = False
        for i in range(0,k):
            if list[i] > list[i+1]:
                list[i+1], list[i] = list[i], list[i+1]
                flip = True
        k -= 1

my = []
for i in range(100):
    my.append(random.randint(0,1000))
BubbleSort(my)
numIter = []
for i in range(100):
    n = BubbleSort(my[i])
    numIter.append(n)
avgIter = sum(numIter)(len(numIter))
print numIter