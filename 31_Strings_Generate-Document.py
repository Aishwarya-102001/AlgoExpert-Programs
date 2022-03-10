
#** Time = O(m * (n + m)) --> as we traverse through the whole string (n(for loop) + n(joining string)) times = O(2n) = O(n)
#** Space = O(1) --> no extra database used  

def generateDocument(characters, document):
    for character in document:
        documentFrequency = countCharacterFrequency(character,document)  #takes O(n) time
        characterFrequency = countCharacterFrequency(character, characters)   #takes O(m) time

        if documentFrequency > characterFrequency:
            return False

    return True

# document.count(character)  --> takes O(n) time to run behind the scenes

# this is how .count method works:-
def countCharacterFrequency(character, target):
    frequency = 0 

    for char in target:
        if char == character:
            frequency += 1
    return frequency

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
print(generateDocument(characters, document))