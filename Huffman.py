from collections import Counter

#Priority Queue
def left(i):
    return (2 * i) + 1
def right(i):
    return (2 * i) + 2
def parent(i):
    return (i - 1) >> 1
def build_min_heap(x):
    n = len(x)
    for i in reversed(range(n // 2)):
        sift_down(x, i, n)
def sift_down(list, i, length):
    current = i
    while left(current) < length:
        smallest = current
        if list[left(current)] < list[current]:
            smallest = left(current)
        if right(current) < length and list[right(current)] < list[smallest]:
            smallest = right(current)
        if smallest == current:
            return
        list[current], list[smallest] = list[smallest], list[current]
        current = smallest
def sift_up(x, i):
    p = parent(i)
    while i and x[p] > x[i]:
        x[i], x[p] = x[p], x[i]
        i = p
        p = parent(i)
def extract_min(x):
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

class Node:
    left = None
    right = None
    char = None

    def __lt__(self, other):
        if self.char and other.char:
            return self.char < other.char
        if self.char:
            return True
        else:
            return False
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def set_char(self, char):
        self.char = char
    def walk(self, code, acc):
        if self.left is None and self.right is None:
            code[self.char] = acc or "0"
        if self.left:
            self.left.walk(code, acc + "0")
        if self.right:
            self.right.walk(code, acc + "1")


s = input()

priority_queue = []
def encode_huffman(x):
    for char, freq in Counter(x).items():
        node = Node()
        node.set_char(char)
        priority_queue.append((freq, node))

    build_min_heap(priority_queue)

    while len(priority_queue) > 1:
        freq1, node1 = extract_min(priority_queue)
        freq2, node2 = extract_min(priority_queue)
        insert(priority_queue, (freq1 + freq2, Node(node1, node2)))

    frequency, root_node = extract_min(priority_queue)

    code = {}
    root_node.walk(code, "")

    encoded = "".join([code[ch] for ch in x])
    print(len(code), len(encoded))
    for char in sorted(code):
        print("{}: {}".format(char, code[char]))

    print(encoded)

encode_huffman(s)
