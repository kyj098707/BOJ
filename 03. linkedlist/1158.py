import sys

input = sys.stdin.readline


class DLL:
    class Node:
        def __init__(self, prev, item, link):
            self.item = item
            self.next = link
            self.prev = prev

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(self.head, None, None)
        self.head.next = self.tail
        self.cur = self.head
        self.cnt = 0

    def delete(self, x):

        x.prev.next = x.next
        x.next.prev = x.prev
        self.cnt = self.cnt - 1

    def insert(self, p, item):
        t = p.prev
        node = self.Node(t, item, p)
        t.next = node
        p.prev = node
        self.cnt = self.cnt + 1

    def __str__():
        return


n, k = map(int, input().split())
if n == 1 and k == 1:
    print("<1>")
else:
    dll = DLL()
    for num in range(1, n + 1):
        dll.insert(dll.tail, num)

    while dll.head.next != dll.tail:
        for _ in range(k):
            dll.cur = dll.cur.next
            if dll.cur == dll.tail:
                dll.cur = dll.head.next

        if dll.cnt == n:
            print(f"<{dll.cur.item},", end="")
        elif dll.cnt == 1:
            print(f" {dll.cur.item}>")
        else:
            print(f" {dll.cur.item},", end="")
        dll.delete(dll.cur)
