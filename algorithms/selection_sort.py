def find_smallest(lst):
    smallest = lst[0]
    smallest_index = 0
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            smallest_index = i
    return smallest_index

def selection_sort(lst):
    new_lst = []
    for i in range(len(lst)):
        smallest = find_smallest(lst)
        new_lst.append(lst.pop(smallest))
    return new_lst
print(selection_sort([5, 3, 6, 2, 10]))