def left(i):
    return (2 * i) + 1

def right(i):
    return (2 * i) + 2

def parent(i):
    return (i - 1) >> 1

def build_max_heap(x):
    n = len(x)
    for i in reversed(range(n // 2)):
        sift_down(x, i, n)

def sift_down(list, i, length):
    current = i
    while left(current) < length:
        largest = current
        if list[left(current)] > list[current]:
            largest = left(current)
        if right(current) < length and list[right(current)] > list[largest]:
            largest = right(current)
        if largest == current:
            return
        list[current], list[largest] = list[largest], list[current]
        current = largest

def sift_up(x, i):
    p = parent(i)
    while i and x[p] < x[i]:
        x[i], x[p] = x[p], x[i]
        i = p
        p = parent(i)

def extract_max(x):
    last = x.pop()
    if x:
        max = x[0]
        x[0] = last
        sift_down(x, 0, len(x))
        return max
    return last

def insert(h, x):
    h.append(x)
    sift_up(h, len(h) - 1)

h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(h)
build_max_heap(h)
print(h)
