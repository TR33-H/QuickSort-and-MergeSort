import math
import time
import random

def MergeSort(X):
    MergeSortHelper(X, 0, len(X) - 1)

def MergeSortHelper(x, left, right):
    if left < right:
        middle = (left + right) // 2
        MergeSortHelper(x, left, middle)
        MergeSortHelper(x, middle + 1, right)
        Merge(x, left, right)
    else:
        return

def Merge(X, left, right):
    i = left
    middle = (left + right) // 2
    k = left
    what = 0
    rhat = 0
    leftCopy = X[i:middle + 1]
    rightCopy = X[middle + 1:right+1]

    while what < len(leftCopy) and rhat < len(rightCopy):
        if leftCopy[what] <= rightCopy[rhat]:
            X[k] = leftCopy[what]
            what += 1
        else:
            X[k] = rightCopy[rhat]
            rhat += 1
        
        k +=1

    while what < len(leftCopy):
        X[k] = leftCopy[what]
        what +=1
        k +=1
    while rhat < len(rightCopy):
        X[k] = rightCopy[rhat]
        rhat += 1
        k +=1






    
    


def main():

    #2^5
    backwardsArray25 = []
    i = 2**5
    while i > 0:
        backwardsArray25.append(i)
        i -= 1

    start = time.perf_counter()
    MergeSort(backwardsArray25)
    end = time.perf_counter()
    print("Backwards MergeSort 2 ^ 5: ", end - start )
    

    #random shuffle
    random.shuffle(backwardsArray25)
    start = time.perf_counter()
    MergeSort(backwardsArray25)
    end = time.perf_counter()
    print("Random Backwards MergeSort 2 ^ 5: ", end - start )


    #Even Then Odd
    even = []
    odd = []
    for i in range(1, 2**5 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven25 = odd + even
    start = time.perf_counter()
    MergeSort(oddThenEven25)
    end = time.perf_counter()
    print("Odd Then Even Backwards MergeSort 2 ^ 5: ", end - start )


    #2^6
    backwardsArray26 = []
    i = 2**6
    while i > 0:
        backwardsArray26.append(i)
        i -= 1

    start = time.perf_counter()
    MergeSort(backwardsArray26)
    end = time.perf_counter()
    print("Backwards MergeSort 2 ^ 6: ", end - start )

    #random shuffle
    random.shuffle(backwardsArray26)
    start = time.perf_counter()
    MergeSort(backwardsArray26)
    end = time.perf_counter()
    print("Random Backwards MergeSort 2 ^ 6: ", end - start )

    #Even Then Odd
    even = []
    odd = []
    for i in range(1, 2**6 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven26 = odd + even
    start = time.perf_counter()
    MergeSort(oddThenEven26)
    end = time.perf_counter()
    print("Odd Then Even Backwards MergeSort 2 ^ 6: ", end - start )


    #2^7
    backwardsArray27 = []
    i = 2**7
    while i > 0:
        backwardsArray27.append(i)
        i -= 1

    start = time.perf_counter()
    MergeSort(backwardsArray27)
    end = time.perf_counter()
    print("Backwards MergeSort 2 ^ 7: ", end - start )

    #random shuffle
    random.shuffle(backwardsArray27)
    start = time.perf_counter()
    MergeSort(backwardsArray27)
    end = time.perf_counter()
    print("Random Backwards MergeSort 2 ^ 7: ", end - start )

    #Even Then Odd
    even = []
    odd = []
    for i in range(1, 2**7 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven27 = odd + even
    start = time.perf_counter()
    MergeSort(oddThenEven27)
    end = time.perf_counter()
    print("Odd Then Even Backwards MergeSort 2 ^ 7: ", end - start )



    #2^8
    backwardsArray28 = []
    i = 2**8
    while i > 0:
        backwardsArray28.append(i)
        i -= 1

    start = time.perf_counter()
    MergeSort(backwardsArray28)
    end = time.perf_counter()
    print("Backwards MergeSort 2 ^ 8: ", end - start )

    #random shuffle
    random.shuffle(backwardsArray28)
    start = time.perf_counter()
    MergeSort(backwardsArray28)
    end = time.perf_counter()
    print("Random Backwards MergeSort 2 ^ 8: ", end - start )

    #Even Then Odd
    even = []
    odd = []
    for i in range(1, 2**8 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven28 = odd + even
    start = time.perf_counter()
    MergeSort(oddThenEven28)
    end = time.perf_counter()
    print("Odd Then Even Backwards MergeSort 2 ^ 8: ", end - start )


    #2^9
    backwardsArray29 = []
    i = 2**9
    while i > 0:
        backwardsArray29.append(i)
        i -= 1

    start = time.perf_counter()
    MergeSort(backwardsArray29)
    end = time.perf_counter()
    print("Backwards MergeSort 2 ^ 9: ", end - start )

    #random shuffle
    random.shuffle(backwardsArray29)
    start = time.perf_counter()
    MergeSort(backwardsArray29)
    end = time.perf_counter()
    print("Random Backwards MergeSort 2 ^ 9: ", end - start )

    #Even Then Odd
    even = []
    odd = []
    for i in range(1, 2**9 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven29 = odd + even
    start = time.perf_counter()
    MergeSort(oddThenEven29)
    end = time.perf_counter()
    print("Odd Then Even Backwards MergeSort 2 ^ 9: ", end - start )



if __name__=="__main__": 
    main() 