
#***Time --> O(nlog(n) + mlog(m)) --> n = (length of arrayOne) and m = (length of arrayTwo)
#***Space --> O(1) --> as we are sorting the array in place nd not using any additional space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    currentSmallestDiff = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            currentSmallestDiff = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            currentSmallestDiff = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        
        if smallest > currentSmallestDiff:
            smallest = currentSmallestDiff
            smallestPair = [firstNum, secondNum]

    return smallestPair
input = smallestDifference([-1, 5, 10, 20, 28, 3, 26], [26, 134, 135, 15, 17])
print(input)