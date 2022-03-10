
# import program
# import unittest

# class TestProgram(unittest.TestCase):
#     def test_case_1(self):
#         output = program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
#         self.assertTrue(len(output) == 2)
#         self.assertTrue(11 in output)
#         self.assertTrue(-1 in output)

#***************** Solution 1- Using 2 for loops*********************
# O(n^2)---> Time---> as we use 2 for loops its not recommended to use this method
# O(1)---> Space

def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))  #Can change the test cases

#***************** Solution 2- Using Hash table*********************
# O(n)---> Time --->cuz we traverse via the whole array 
# O(n)---> Space --->as we added the traversed values into the hash table
 
def twoNumberSum(array, targetSum):
    nums ={}
    for x in array:
        y = targetSum - x
        if y in nums:
            return [y, x]
        else:
            nums[x]= True  #To store the traversed values
    return[]

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))  #Can change the test cases


#***************** Solution 3- Sorting array and using 2 pointers*********************
# O(nlog(n))---> Time ---> #****most efficient method**** 
# O(1)---> Space 

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[right], array[left]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))  #Can change the test cases

