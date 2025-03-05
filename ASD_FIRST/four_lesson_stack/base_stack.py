import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i is self.count:
            self.append(itm=itm)
            return

        self.__getitem__(i)

        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        for i_range in range(self.count, i, -1):
            self.array[i_range] = self.array[i_range - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        self.__getitem__(i)

        if (self.capacity > 16) and (self.count - 1 < self.capacity // 2):
            self.capacity = max(16, int(self.capacity / 1.5))

        for loop_i in range(i, self.count - 1):
            self.array[loop_i] = self.array[loop_i + 1]

        self.count -= 1
        self.resize(self.capacity)

    def get_list_elements(self):
        return list(self.array._objects.values())


class Stack:
    def __init__(self):
        self.stack = DynArray()

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        result = self.stack[self.size() - 1]
        self.stack.delete(self.size() - 1)

        return result

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[self.size() - 1]


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self, v):
        super().__init__(v)


class ReverseStack:
    """Задание 2: Вариант стека в котором голова списка реализована как верхушка стека"""
    def __init__(self):
        self.head = DummyNode(None)
        self.tail = self.head

        self.head.next = self.tail
        self.head.prev = self.tail

        self.tail.prev = self.head
        self.tail.next = self.head
        self.count_node = 0

    def push(self, value) -> None:
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

        self.count_node += 1

    def size(self):
        return self.count_node

    def pop(self):
        if self.count_node == 0:
            return None
        result = self.head.next.value

        self.head.next = self.head.next.next

        self.count_node -= 1
        return result


    def peek(self):
        if self.count_node == 0:
            return None
        return self.head.next.value

