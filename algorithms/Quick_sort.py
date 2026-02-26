def quick_sort(arr):
    if len(arr) < 2:
        return arr
    supp_el = arr[0]
    less_supp_el = [i for i in arr[1:] if i <= supp_el]
    more_supp_el = [i for i in arr[1:] if i >= supp_el]
    return quick_sort(less_supp_el) + [supp_el] + quick_sort(more_supp_el)