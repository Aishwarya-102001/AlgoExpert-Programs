
#*********** Iterative approach *************

#**Time --> O(n) --> as we traverse through the whole matrix using for loops (n--> total number of elements in entire matrix)
#**Space --> O(n) --> as we are storing all n elements in new array

# def spiralTraverse(array):
#     result = []
#     startRow, endRow = 0, len(array) - 1
#     startCol, endCol = 0, len((array)[0]) - 1

#     while startRow <= endRow and startCol <= endCol:
#         for col in range(startCol, endCol + 1):
#             result.append(array[startRow][col])

#         for row in range(startRow + 1, endRow + 1):
#             result.append(array[row][endCol])

#         for col in reversed(range(startCol, endCol)):
            #Handle the edge case when there's a single row in the middle of the matrix. 
			#In this case, we don't want to double-count the values in this row, 
			#which we've already counted in the first for loop above.
			#{
			# "array": [
			# 	[1, 2, 3, 4],
			# 	[10, 11, 12, 5],
			# 	[9, 8, 7, 6]
			#   ]
			# }
            # if startRow == endRow:
            #     break
#           result.append(array[endRow][col])

#         for row in reversed(range(startRow + 1, endRow)):
            #Handle the edge case when there's a single column in the middle of the matrix. 
			#In this case, we don't want to double-count the values in this column, 
			#which we've already counted in the second for loop above.
			# {
			#   "array": [
			# 	[1, 2, 3],
			# 	[12, 13, 4],
			# 	[11, 14, 5],
			# 	[10, 15, 6],
			# 	[9, 8, 7]
			#   ]
			# }
            #if startCol == endCol:
            #     break
#           result.append(array[row][startCol])


#         startRow += 1
#         endRow -= 1
#         startCol += 1 
#         endCol -= 1
#     return result

# matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
# print (matrix)
# print (spiralTraverse(matrix))


#*********** Recursive approach *************

#**Time --> O(n) --> as we traverse through the whole matrix using for loops (n--> total number of elements in entire matrix)
#**Space --> O(n) --> as we are storing all n elements in new array and also memory is allocated in stack while every fucntion is called

def spiralTraverse(array):
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result

def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return

    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):
            #Handle the edge case when there's a single row in the middle of the matrix. 
			#In this case, we don't want to double-count the values in this row, 
			#which we've already counted in the first for loop above.
			#{
			# "array": [
			# 	[1, 2, 3, 4],
			# 	[10, 11, 12, 5],
			# 	[9, 8, 7, 6]
			#   ]
			# }
        if startRow == endRow:
            break
        result.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):
        #Handle the edge case when there's a single column in the middle of the matrix. 
			#In this case, we don't want to double-count the values in this column, 
			#which we've already counted in the second for loop above.
			# {
			#   "array": [
			# 	[1, 2, 3],
			# 	[12, 13, 4],
			# 	[11, 14, 5],
			# 	[10, 15, 6],
			# 	[9, 8, 7]
			#   ]
			# }
        if startCol == endCol:
            break
        result.append(array[row][startCol])

    spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)

matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print (matrix)
print (spiralTraverse(matrix))