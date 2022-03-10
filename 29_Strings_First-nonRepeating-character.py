
#** Brute-Force Approach ***********

#** Time = O(n^2) --> as we traverse through the whole string n*n times = n^2 times with ith and jth iteration
#** Space = O(1) --> as no other DS is used other than 2 pointers
# def firstNonRepeatingCharacter(string):
#     for idx in range(len(string)):
#         foundDuplicate = False
#         for idx2 in range(len(string)):
#             if string[idx] == string[idx2] and idx != idx2:
#                 foundDuplicate = True

#         if foundDuplicate == False:
#             return idx
#     return -1

# print(firstNonRepeatingCharacter("abcdcaf"))


#** Using dictionary to store count of each alphabet ***********

#** Time = O(n) --> as we traverse through the whole string (n + n) times = O(2n) = O(n)
#** Space = O(1) --> as no other DS is used other than a pointer to traverse the input string

def firstNonRepeatingCharacter(string):
    characterFrequencies = {}

    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1   
        #for every key store 0 as default value and for the existing key, update the value by 1

    for idx in range(len(string)):
        character = string[idx]  #traverse the input string and check if it's value=1 (it has occured only once and is the first non-repating charcter)
        if characterFrequencies[character] == 1:
            return idx

    return -1

print(firstNonRepeatingCharacter("abcdcaf"))
