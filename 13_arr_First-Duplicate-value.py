
#************************ Brute Force Approach ****************************
#**Time --> O(n^2) --> as we traverse through the array twice using 2 for loops (n--> total number of elements in array)
#**Space --> O(1) --> as we donot store any extra space or data structure
# def firstDuplicateValue(array):
#     minimumSecondIndex = len(array)
#     for i in range(len(array)):
#         value = array[i]
#         for j in range(i + 1, len(array)):
#             valueToCompare = array[j]
#             if value == valueToCompare:
#                 minimumSecondIndex = min(minimumSecondIndex, j)

#     if minimumSecondIndex == len(array):
#         return -1

#     return array[minimumSecondIndex]

# input = [2, 1, 5, 3, 3, 2, 4]
# print(firstDuplicateValue(input))

#************************ Using set() ****************************
#**Time --> O(n) --> as we traverse through array using for loop once (n--> total number of elements in array)
#**Space --> O(n) --> as we store a new DS i.e set() to keep track of traversed values

# def firstDuplicateValue(array):
#     seen = set()
#     for value in array:
#         if value in seen:  #if value is present in set then return value as we have found the first duplicate
#             return value
#         seen.add(value)  #if value not in aet then add that value to the set
#     return -1            # if we didn't find any duplicate value

# input = [2, 1, 5, 3, 3, 2, 4]
# print(firstDuplicateValue(input))


#************************ MOST OPTIMAL SOLUTION - Creating absolute value variable and negative indication ****************************
#**Time --> O(n) --> as we traverse through the array once using one for loop (n--> total number of elements in array)
#**Space --> O(1) --> as we donot store any extra space or data structure other that variable

def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:   #check if value at that index is negative, if yes--> duplicate found --> return value
            return absValue
        array[absValue - 1] *= -1    # if no--> update the value to negative value by multiplying the value with -1
    return -1

input = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(input))