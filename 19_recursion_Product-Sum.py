
#** RECURSIVE METHOD ***********
#** Time = O(N) --> where N = total no. of elements in the array including the sub-elements [here, N=12]
#** Space = O(d) --> as we have to make the recursive calls "d" times where, d = greatest depth of "special" array [here, d=3]

def productSum(array, multiplier= 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))