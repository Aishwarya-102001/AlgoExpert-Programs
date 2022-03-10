
#** RECURSIVE METHOD ***********
#** Time = O(2^n) --> as every step has 2 function calls and this continues till nth term i.e 2*2*2*2*2....n times
#** Space = O(n) --> as we keep storing all the call stacks upto n

# def getNthFib(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return getNthFib(n-1) + getNthFib(n-2)
# print(getNthFib(4))

#** RECURSIVE METHOD ***********
#** Time = O(n) --> as we have to traverse via all the n elements
#** Space = O(n) --> as we keep storing all the call stacks and also the "memoize" hash table

# def getNthFib(n, memoize = {1:0, 2:1}):
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
#         return memoize[n]

# print(getNthFib(4))

#** ITERATIVE METHOD ***********
#** Time = O(n) --> as we have to traverse via all the n elements
#** Space = O(1) --> as we do not store anything other than variables

def getNthFib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextfib = lastTwo[0] +lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextfib

        counter += 1
    return lastTwo[1] if n>1 else lastTwo[0]

print(getNthFib(3))

