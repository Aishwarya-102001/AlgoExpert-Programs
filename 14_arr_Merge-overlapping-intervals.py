
#**Time --> O(nlog(n)) --> as we sorted thr array with starting times (n--> total number of elements in array)
#**Space --> O(n) --> as we create new array to store the output

def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])  #we have sorted the intervals based on their very first value

    mergedIntervals = []   #create new array to store merged intervals
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)  #this cond. holds true only if we have at least 1 interval in the given array

    for nextInterval in sortedIntervals:
        _ , currentIntervalEnd = currentInterval
        nextIntervalStart , nextIntervalEnd = nextInterval   #both variables are used to decompose the respective interval

        if currentIntervalEnd >= nextIntervalStart:   #cond. to check for overlap is available or not
            currentInterval[1] = max(currentIntervalEnd , nextIntervalEnd)   
        else:
            currentInterval = nextInterval   #if not move to nextInterval
            mergedIntervals.append(currentInterval)  

    return mergedIntervals

intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
print(mergeOverlappingIntervals(intervals))
