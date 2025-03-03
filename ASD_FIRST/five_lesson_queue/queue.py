class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self, v):
        super().__init__(v)


class Queue:
    def __init__(self):
        self.head = DummyNode(None)
        self.tail = self.head

        self.head.next = self.tail
        self.head.prev = self.tail

        self.tail.prev = self.head
        self.tail.next = self.head
        self.count_node = 0

    def enqueue(self, value) -> None:
        new_node = Node(value)
        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.count_node += 1

    def dequeue(self):
        if self.count_node == 0:
            return None
        result = self.head.next.value

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

        self.count_node -= 1
        return result

    def size(self) -> int:
        return self.count_node
