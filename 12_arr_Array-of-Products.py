
#************************ Brute Force Approach ****************************
#**Time --> O(n^2) --> as we traverse through the array twice using 2 for loops (n--> total number of elements in array)
#**Space --> O(n) --> as we store a new array with required output

# def arrayOfProducts(array):
#     products = [1 for _ in range(len(array))]

#     for i in range(len(array)):
#         runningProduct = 1
#         for j in range(len(array)):
#             if i != j:
#                 runningProduct *= array[j]
#         products[i] = runningProduct
#     return products

# array = [5, 1, 4, 2]
# print(arrayOfProducts(array))

#************************ Creating left and right array ****************************
#**Time --> O(n) --> as we traverse through array using for loops (n + n + n = 3n ~> O(n)) (n--> total number of elements in array)
#**Space --> O(n) --> as we store a new array with required output

# def arrayOfProducts(array):
#     products = [1 for _ in range(len(array))]
#     leftProducts = [1 for _ in range(len(array))]
#     rightProducts = [1 for _ in range(len(array))]
    
#     leftRunningProduct = 1
#     for i in range(len(array)):
#         leftProducts[i] = leftRunningProduct
#         leftRunningProduct *= array[i]

#     rightRunningProduct = 1 
#     for i in reversed(range(len(array))):
#         rightProducts[i] = rightRunningProduct
#         rightRunningProduct *= array[i]

#     for i in range(len(array)):
#         products[i] = leftProducts[i] * rightProducts[i]

#     return products

# array = [5, 1, 4, 2]
# print(arrayOfProducts(array))


#************************ Combining both left and right array into single Product array ****************************
#**Time --> O(n) --> as we traverse through array using for loops (n + n + n = 3n ~> O(n)) (n--> total number of elements in array)
#**Space --> O(n) --> as we store a new array with required output

#**** OPTIMAL SOLUTION OF ALL 3****

def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1 
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products

array = [5, 1, 4, 2]
print(arrayOfProducts(array))