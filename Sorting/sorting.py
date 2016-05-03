def sequentialSearch(aList, val):
    for i in range(len(aList)):
        if i == val:
            return True
    return False

def binarySearch(aList, val):
    pickedNum = len(aList)/2
    while pickedNum != val:
        if val > pickedNum:
            #go to the right half
            aList = aList[pickedNum:]
            pickedNum = len(aList) / 2
        if val < pickedNum:
            #go to the left half
            aList = aList[:pickedNum]
            pickedNum = len(aList) /2
    return pickedNum