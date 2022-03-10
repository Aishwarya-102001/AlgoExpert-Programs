
#** SORTING ALGORITHM ***********

#** Time =  Best = O(n) --> as the whole input array would already be sorted.
#**         Average & Worst = O(n^2) --> as we traverse through the array a bunch of times using the while loop.

#** Space = Best, Average & Worst = O(1) --> no considerable space required other than few swaps and array is sorted in-place.

def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True 
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))