import sys

input = sys.stdin.readline


class DLL:
    class Node:
        def __init__(self, prev, data, link):
            self.prev = prev
            self.data = data
            self.next = link

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(self.head, None, None)
        self.head.next = self.tail
        self.cur = self.tail

    def insert(self, p, data):
        t = p.prev
        node = self.Node(t, data, p)
        t.next = node
        p.prev = node

    def delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def traverse(self):
        p = self.head.next
        while p.next != None:
            if p.next == self.tail:
                print(p.data)
            else:
                print(p.data, end="")
            p = p.next


n = int(input())


for _ in range(n):
    dll = DLL()
    command = input().rstrip()

    for c in command:
        if c == "<":
            if dll.cur.prev != dll.head:
                dll.cur = dll.cur.prev
        elif c == ">":
            if dll.cur.next != None:
                dll.cur = dll.cur.next
        elif c == "-":
            if dll.cur.prev != dll.head:
                dll.delete(dll.cur.prev)
        else:
            dll.insert(dll.cur, c)
    dll.traverse()
