
#** SORTING ALGORITHM ***********

#** Time =  Best = O(n) --> as the whole input array would already be sorted.
#**         Average & Worst = O(n^2) --> as we traverse through the array a bunch of times using the for and while loop.

#** Space = Best, Average & Worst = O(1) --> no considerable space required other than few swaps and array is sorted in-place.

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j-1, array)

            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(insertionSort([8, 5, 2, 9, 5, 6, 3]))