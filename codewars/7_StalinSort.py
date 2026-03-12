def stalin_sort(arr):
    pres = arr[0]
    for i in range(len(arr[1:])):
        if arr[i] < pres:
            arr.pop(arr[i])
print(stalin_sort([5,3,1]))