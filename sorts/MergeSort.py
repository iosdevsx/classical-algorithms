def merge(x, left_part, right_part):
    i, j, k = 0, 0, 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            x[k] = left_part[i]
            i += 1
        else:
            x[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        x[k] = left_part[i]
        k += 1
        i += 1
    while j < len(right_part):
        x[k] = right_part[j]
        j += 1
        k += 1

def merge_sort(x):
    if len(x) > 1:
        mid = len(x) // 2
        left_part = x[:mid]
        right_part = x[mid:]
        merge_sort(left_part)
        merge_sort(right_part)
        merge(x, left_part, right_part)

l = [x for x in reversed(range(1, 11))]
print(l)
merge_sort(l)
print(l)
