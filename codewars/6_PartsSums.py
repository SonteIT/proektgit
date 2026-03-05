def parts_sums(ls):
    current_sum = sum(ls)
    result = [current_sum]
    for x in ls:
        current_sum -= x
        result.append(current_sum)
    return result


print(parts_sums([1, 2, 3, 0, 4, 5]))
