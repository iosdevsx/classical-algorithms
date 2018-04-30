def insertion_sort(x):
    for j in range(1, len(x)):
        key = x[j]
        i = j - 1
        while i >= 0 and key < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = key

l = [5,4,3,2,1]
print(l)
insertion_sort(l)
print(l)