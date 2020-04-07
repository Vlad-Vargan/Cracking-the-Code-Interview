from random import randint

class LinkedListNode():
    def __init__(self, value, nextNode = None, prevNode = None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self, values = None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __str__(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.value))
            node = node.next
        return " -> ".join(nodes)

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length
    
    def add(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_to_beginning(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, nextNode = self.head)
        return self.head

    def add_multiple(self, values):
        for value in values:
            self.add(value)

    def generate(self, n = 10, min_value = 0, max_value = 9):
        self.head = self.tail = None
        for _ in range(n):
            self.add(randint(min_value,max_value))
        return self