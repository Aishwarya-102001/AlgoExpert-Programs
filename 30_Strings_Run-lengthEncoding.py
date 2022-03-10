
#** Time = O(n) --> as we traverse through the whole string (n(for loop) + n(joining string)) times = O(2n) = O(n)
#** Space = O(n) --> as we store all the given string values 

def runLengthEncoding(string):
    encodedStringCharacters= []
    currentRunLength = 1

    for i in range (1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i-1]

        if currentCharacter != previousCharacter or currentRunLength == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousCharacter)
            currentRunLength = 0

        currentRunLength += 1

    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string) - 1])


    return "".join(encodedStringCharacters)

string = "AAAAAAAAAAAAABBCCCCDD"
print(runLengthEncoding(string))