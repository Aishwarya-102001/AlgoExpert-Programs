
#*****Brute force Approach(works even if array is not sorted)*******
# O(nlog(n)) --> time
# O(n) --> space
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array] #initialize an empty array
    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value	
    sortedSquares.sort()
    return sortedSquares

# sortedInput = [-12, -2, 3, 5, 6, 8, 9]
# print("original sorted array", sortedInput)
# print("squared sorted array", sortedSquaredArray(sortedInput))

# unsortedInput =[3, -4, 2, 7, -8]
# print("original unsorted array", unsortedInput)
# print("squared sorted array", sortedSquaredArray(unsortedInput))


#*****Solution 2 (works only if array is sorted)*******
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array] #initialize an empty array
    smallerValueIdx = 0
    largerValueIdx = len(array)- 1
    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]
        
        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1
            
    return sortedSquares

sortedInput = [-12, -2, 3, 5, 6, 8, 9]
print("original sorted array", sortedInput)
print("squared sorted array", sortedSquaredArray(sortedInput))

