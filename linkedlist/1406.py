import sys

input = sys.stdin.readline


class Dlinkedlist:
    class Node:
        def __init__(self, prev_node=None, item=None, next_node=None):
            self.item = item
            self.prev_node = prev_node
            self.next_node = next_node

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node(prev_node=self.head)
        self.head.next_node = self.tail
        self.cur = self.tail

    def insert(self, p, item):
        t = p.prev_node
        node = self.Node(t, item, p)
        t.next_node = node
        p.prev_node = node

    def delete(self, x):
        x.prev_node.next_node = x.next_node
        x.next_node.prev_node = x.prev_node

    def traverse(self):
        p = self.head.next_node
        while p != self.tail:
            if p.next_node == self.tail:
                print(p.item)
            else:
                print(p.item, end="")
            p = p.next_node


input_str = input().rstrip()
cursor = Dlinkedlist()


for i in input_str:
    cursor.insert(cursor.tail, i)

num = int(input())

for _ in range(num):
    command = input()

    if command[0] == "P":
        cursor.insert(cursor.cur, command[2])

    elif command[0] == "L":
        if cursor.cur.prev_node.prev_node != None:
            cursor.cur = cursor.cur.prev_node

    elif command[0] == "D":
        if cursor.cur.next_node != None:
            cursor.cur = cursor.cur.next_node

    elif command[0] == "B":
        if cursor.cur.prev_node.prev_node != None:
            cursor.delete(cursor.cur.prev_node)


cursor.traverse()
