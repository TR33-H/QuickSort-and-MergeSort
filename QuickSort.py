import random
import time

def QuickSort(S):
    if len(S) <= 1:
        return S
    else:
        p = []
        p.append(S[0]) #First Element / Pivot
        S1 = []
        S2 = []
        for numbers in S:
            if numbers < p[0]:
                S1.append(numbers)
            elif numbers > p[0]:
                S2.append(numbers)
        return QuickSort(S1) + p + QuickSort(S2)
    
def RandomQuickSort(S):
    if len(S) <= 1:
        return S
    else:
        p = []
        p.append(random.choice(S)) #First Element / Pivot
        S1 = []
        S2 = []
        for numbers in S:
            if numbers < p[0]:
                S1.append(numbers)
            elif numbers > p[0]:
                S2.append(numbers)
        return QuickSort(S1) + p + QuickSort(S2)



def main():
    backwardsArray25 = []
    i = 2**5
    while i > 0:
        backwardsArray25.append(i)
        i -= 1

    start = time.perf_counter()
    QuickSort(backwardsArray25)
    end = time.perf_counter()
    print("Backwards QuickSort 2 ^ 5 ", end - start)


    random.shuffle(backwardsArray25)
    start = time.perf_counter()
    QuickSort(backwardsArray25)
    end = time.perf_counter()
    print("Random Backwards QuickSort 2 ^ 5 ", end - start)


    even = []
    odd = []
    for i in range(1, 2**5 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven25 = odd + even

    start = time.perf_counter()
    QuickSort(oddThenEven25)
    end = time.perf_counter()
    print("Even then Odd Backwards QuickSort 2 ^ 5 ", end - start)




    backwardsArray26 = []
    i = 2**6
    while i > 0:
        backwardsArray26.append(i)
        i -= 1

    start = time.perf_counter()
    QuickSort(backwardsArray26)
    end = time.perf_counter()
    print("Backwards QuickSort 2 ^ 6 ", end - start)


    random.shuffle(backwardsArray26)
    start = time.perf_counter()
    QuickSort(backwardsArray26)
    end = time.perf_counter()
    print("Random Backwards QuickSort 2 ^ 6 ", end - start)


    even = []
    odd = []
    for i in range(1, 2**6 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven26 = odd + even

    start = time.perf_counter()
    QuickSort(oddThenEven26)
    end = time.perf_counter()
    print("Even then Odd Backwards QuickSort 2 ^ 6 ", end - start)





    backwardsArray27 = []
    i = 2**7
    while i > 0:
        backwardsArray27.append(i)
        i -= 1

    start = time.perf_counter()
    QuickSort(backwardsArray27)
    end = time.perf_counter()
    print("Backwards QuickSort 2 ^ 7 ", end - start)



    random.shuffle(backwardsArray27)
    start = time.perf_counter()
    QuickSort(backwardsArray27)
    end = time.perf_counter()
    print("Random Backwards QuickSort 2 ^ 7 ", end - start)


    even = []
    odd = []
    for i in range(1, 2**7 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven27 = odd + even

    start = time.perf_counter()
    QuickSort(oddThenEven27)
    end = time.perf_counter()
    print("Even then Odd Backwards QuickSort 2 ^ 7 ", end - start)



    backwardsArray28 = []
    i = 2**8
    while i > 0:
        backwardsArray28.append(i)
        i -= 1

    start = time.perf_counter()
    QuickSort(backwardsArray28)
    end = time.perf_counter()
    print("Backwards QuickSort 2 ^ 8 ", end - start)


    random.shuffle(backwardsArray28)
    start = time.perf_counter()
    QuickSort(backwardsArray28)
    end = time.perf_counter()
    print("Random Backwards QuickSort 2 ^ 8 ", end - start)


    even = []
    odd = []
    for i in range(1, 2**8 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven28 = odd + even
    start = time.perf_counter()
    QuickSort(oddThenEven28)
    end = time.perf_counter()
    print("Even then Odd Backwards QuickSort 2 ^ 8 ", end - start)






    backwardsArray29 = []
    i = 2**9
    while i > 0:
        backwardsArray29.append(i)
        i -= 1

    start = time.perf_counter()
    QuickSort(backwardsArray29)
    end = time.perf_counter()
    print("Backwards QuickSort 2 ^ 9 ", end - start)


    random.shuffle(backwardsArray29)
    start = time.perf_counter()
    QuickSort(backwardsArray29) 
    end = time.perf_counter()
    print("Random Backwards QuickSort 2 ^ 9 ", end - start)


    even = []
    odd = []
    for i in range(1, 2**9 + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    oddThenEven29 = odd + even
    start = time.perf_counter()
    QuickSort(oddThenEven29)
    end = time.perf_counter()
    print("Even then Odd Backwards QuickSort 2 ^ 9 ", end - start)


if __name__=="__main__": 
    main() 