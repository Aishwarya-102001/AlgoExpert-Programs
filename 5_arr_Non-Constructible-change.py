
#***Time --> O(nlog(n)) --> as we use sorting algo
#***Space --> O(1) --> as we are sorting the array in place nd not using any additional space
def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0

    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1

input = [5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(input))

input2 = [1, 2, 3]
print(nonConstructibleChange(input2))