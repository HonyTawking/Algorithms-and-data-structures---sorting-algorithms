# Heap sort
def Create_heap(array, n, i):
    highest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        highest = l
    if r < n and array[highest] < array[r]:
        highest = r
    if highest != i:
        array[i], array[highest] = array[highest], array[i]
        Create_heap(array, n, highest)

def HS(array):
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        Create_heap(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        Create_heap(array, i, 0)
    return array

# Merge sort
def fusion(array, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = array[low + i]
    for j in range(0, n2):
        R[j] = array[mid + 1 + j]
    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def MS(array, low, high):
    if low < high:
        mid = low+(high-low) // 2
        MS(array, low, mid)
        MS(array, mid + 1, high)
        fusion(array, low, mid, high)
    return array

# Quick sort with pivot on the right site of an array
def Partition(array, left, right):
    i = left - 1
    pivot = array[right]
    j = right + 1
    while True:
        i+=1
        while (array[i] < pivot):
            i+=1
        j-=1
        while (array[j] > pivot):
            j-=1
        if i>=j:
            if j == right:
                j -= 1
            return j
        array[i], array[j] = array[j], array[i]

def QS(array, left, right):
    if left < right:
        s = Partition(array, left, right)
        QS(array, left, s)
        QS(array, s+1, right)
    return array

# Quick sort with pivot in the middle of an array
def Partition2(array, left, right):
    i = left - 1
    pivot = array[(left+right)//2]
    j = right + 1
    while True:
        i+=1
        while (array[i] < pivot):
            i+=1
        j-=1
        while (array[j] > pivot):
            j-=1
        if i>=j:
            return j
        array[i], array[j] = array[j], array[i]

def QS2(array, left, right):
    if left < right:
        s = Partition2(array, left, right)
        QS2(array, left, s)
        QS2(array, s+1, right)
    return array

# Insertion sort
def IS(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j+1] = key
    return array

# Selection sort
def SS(array):
    for i in range(len(array)-1):
        minimum = i
        for j in range(i, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[minimum], array[i] = array[i], array[minimum]

# Bubble sort
def BS(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Counting sort
def CS(array):
    auxiliary_arr = [0]*max(array)
    for i in range(len(array)):
        auxiliary_arr[array[i]-1] += 1
    for i in range(1, max(array)):
        auxiliary_arr[i] += auxiliary_arr[i-1]
    # print(array)
    # print("-----")
    # print(auxiliary_arr)
    result = [0]* len(array)
    # print(result)
    for i in range(len(array)-1, -1, -1):
        result[auxiliary_arr[array[i]-1]-1] = array[i]
        auxiliary_arr[array[i]-1] -= 1
        # print(result)
    return result