# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[0:i]) == sum(arr[i+1:]):
#             return i
#     return -1
# print(find_even_index([1,2,3,4,3,2,1]))

def find_even_index(arr):
    sum_right = 0
    sum_left = sum(arr)
    for i in range(len(arr)):
        sum_right += arr[i]
        if sum_left == sum_right:
            return i
        sum_left -= arr[i]
    return -1
print(find_even_index([20,10,-80,10,10,15,35]))    