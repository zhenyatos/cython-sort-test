def py_sort(arr, size):
    for i in range(size-1):
        sorted = True
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                sorted = False
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
        if sorted:
            break