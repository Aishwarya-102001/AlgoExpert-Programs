
#**Time --> O(n) --> as we traverse through the whole array using while loops (n--> total number of elements in array)
#**Space --> O(1) --> as we don't store any new data structure other than variable names
def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i] > array[i - 1]  and array[i] > array[i + 1]  #check for tip of peak
        if not isPeak:
            i += 1
            continue      

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:      #traverse towards the left 
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:   #traverse towards the right 
            rightIdx += 1
        
        currentPeakLength = rightIdx - leftIdx - 1  #gives length of peak
        longestPeakLength = max(longestPeakLength, currentPeakLength)  #find the maximum(longest peak) amongst both 
        i = rightIdx #start traversing again from the next right index
    return longestPeakLength

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))