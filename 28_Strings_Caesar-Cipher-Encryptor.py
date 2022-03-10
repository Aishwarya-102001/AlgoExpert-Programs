
#**  using UNICODE VALUES ***********

#** Time = O(n) --> as we traverse through the whole string using loop and if-else conditions
#** Space = O(n) --> as we create new output DS of length "n"

# def caesarCipherEncryptor(string, key):
#     newLetters = []
#     newKey = key % 26
#     for letter in string:
#         newLetters.append(getNewLetter(letter,newKey))

#     return "".join(newLetters)

# def getNewLetter(letter, key):
#     newLetterCode = ord(letter) + key
#     if newLetterCode <= 122:
#         return chr(newLetterCode)
#     else:
#         return chr(96 + newLetterCode % 122)

# print(caesarCipherEncryptor("xyz", 2))

#** Creating a list and assigning values to all alphabets ***********

#** Time = O(n) --> as we traverse through the whole string using loop and if-else conditions
#** Space = O(n) --> as we create new output DS of length "n"

def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for letter in string:
        newLetters.append(getNewLetter(letter,newKey,alphabet))

    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    if newLetterCode <= 25:
        return alphabet[newLetterCode]
    else:
        return alphabet[-1 + newLetterCode % 25]

print(caesarCipherEncryptor("xyz", 2))
