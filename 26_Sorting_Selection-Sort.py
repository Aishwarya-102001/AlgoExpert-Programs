
#** SORTING ALGORITHM ***********

#** Time =  Best = O(n) --> as the whole input array would already be sorted.
#**         Average & Worst = O(n^2) --> as we traverse through the array a bunch of times using the for and while loop.

#** Space = Best, Average & Worst = O(1) --> no considerable space required other than few swaps and array is sorted in-place.

def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if  array[smallestIdx] > array[i]:
                smallestIdx = i

        swap(currentIdx, smallestIdx, array)
        currentIdx +=1

    return array

def swap (i, j, array):
    array[i], array[j] = array[j], array[i]

print(selectionSort([8, 5, 2, 9, 5, 6, 3]))