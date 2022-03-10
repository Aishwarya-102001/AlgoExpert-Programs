
#** ITERATIVE METHOD USING ANOTHER STRING ***********

#** Time = O(n^2) --> as we traverse through the whole string and also perform concatation of strings
#** Space = O(n) --> as we create new string to store the reversed order of string

# def isPalindrome(string):
#     reversedString =""
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#     return string == reversedString

# print(isPalindrome("abcdcba"))

#** ITERATIVE METHOD USING ARRAY TO STORE REVERSED STRING ***********

#** Time = O(n) --> as we traverse through the whole string and just append elements to array
#** Space = O(n) --> as we create new string to store the reversed order of string

# def isPalindrome(string):
#     reversedChar = []
#     for i in reversed(range(len(string))):
#         reversedChar.append(string[i])
#     return string == "".join(reversedChar)

# print(isPalindrome("abcdcba"))

#** RECURSIVE METHOD ***********

#** Time = O(n) --> as we traverse through the whole string and compare both i,j values
#** Space = O(n) --> as we create recursive call stack at every function call

#  def isPalindrome(string, i=0):
#     j = len(string) - 1 - i
#     return True if i>=j else string[i] == string[j] and isPalindrome(string, i+1)

# print(isPalindrome("abcdcba"))

#** TAIL RECURSIVE METHOD ***********
# def isPalindrome(string, i=0):
#     j = len(string) - 1 - i
#     if  i<=j:
#         return True
#     if string[i] != string[j]:
#         return False
#     return isPalindrome(string, i+1)
    
# print(isPalindrome("abcdcba"))

#**  ITERATIVE METHOD (MOST OPTIMAL) ***********

#** Time = O(n) --> as we traverse through the whole string using loops
#** Space = O(1) --> as no other DS is used other than 2 pointers

def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

print(isPalindrome("abcdcba"))
