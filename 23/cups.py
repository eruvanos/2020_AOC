from typing import List


class Node:
    __slots__ = ("number", "ref")

    def __init__(self, number, ref=None):
        self.number = number
        self.ref = None

    def append(self, node: "Node"):
        """
        saves ref to node and returns it
        """
        self.ref = node
        return node

    def __repr__(self):
        return str(self.number)


class Cups:
    def __init__(self, cups: List):
        self.cur = Node(cups[0])
        self.lookup = {cups[0]: self.cur}

        last = self.cur
        for cup in cups[1:]:
            last = last.append(Node(cup, last))
            self.lookup[cup] = last
        last.append(self.cur)

        self.minimal = min(cups)
        self.maximal = max(cups)

        self.picked = []
        self.picked_values = []

    def peek(self):
        cur = self.cur
        return [(cur := cur.ref) for _ in range(3)]

    def pick(self):
        # pick nodes
        self.picked = self.peek()
        self.picked_values = [node.number for node in self.picked]

        # cut them out
        self.cur.ref = self.picked[-1].ref

    def dest(self):
        dest_label = self.cur.number - 1
        if dest_label < self.minimal:
            dest_label = self.maximal

        # resolve picked destination
        while dest_label in self.picked_values:
            dest_label -= 1

            if dest_label < self.minimal:
                dest_label = self.maximal

        return dest_label

    def place(self, dest):
        dest_node = self.lookup[dest]
        self.picked[-1].ref = dest_node.ref
        dest_node.ref = self.picked[0]

    def next(self):
        self.cur = self.cur.ref

    def cups(self, start=None):
        if start:
            start_node = self.lookup[start]
        else:
            start_node = self.cur

        cur = start_node
        result = [cur]
        while (cur := cur.ref) != start_node:
            result.append(cur)

        return result

    def to_str(self):
        def repr(c):
            if c == self.cur:
                return f"({c})"
            else:
                return f"{c}"

        return ",".join(map(repr, self.cups()))

    def __repr__(self):
        return ",".join(map(repr, self.cups()))
