class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self, v):
        super().__init__(v)


class OrderedList:
    __ascending: bool

    def __init__(self, asc: bool):
        self.head = DummyNode(None)
        self.tail = self.head

        self.head.next = self.tail
        self.head.prev = self.tail

        self.__ascending = asc
        self.count_el = 0

    def compare(self, v1, v2):
        if v1 == v2:
            return 0

        if self.__ascending and v1 < v2:
            return -1
        if not self.__ascending and v1 < v2:
            return 1

        if self.__ascending and v1 > v2:
            return 1
        if not self.__ascending and v1 > v2:
            return -1
        return ("Error: Compare error",)

    def add(self, value):
        new_node = Node(value)

        if type(self.head.next) is DummyNode:
            self.head.next = new_node
            self.head.prev = new_node
            new_node.next = self.tail
            new_node.prev = self.head

            self.count_el += 1
            return None

        if self.compare(v1=self.tail.prev.value, v2=new_node.value) == -1:
            new_node.next = self.tail
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            self.tail.prev = new_node

            self.count_el += 1
            return None

        current_node = self.head.next
        while type(current_node) is not DummyNode:
            compare_result = self.compare(current_node.value, new_node.value)

            if compare_result in (0, 1):
                new_node.prev = current_node.prev
                new_node.next = current_node

                current_node.prev.next = new_node
                current_node.prev = new_node
                self.count_el += 1
                return None

            if compare_result == -1:
                current_node = current_node.next
                continue

            return ("Error: Incorrect compare result",)
        return ("Error: Incorrect state",)

    def find(self, val) -> Node | None | tuple:
        iter_node = self.head.next
        while type(iter_node) is Node:
            compare_res = self.compare(iter_node, val)
            if compare_res == 0:
                return iter_node
            if compare_res == -1:
                return None
            if compare_res == 1:
                iter_node = iter_node.next
                continue
            return ("Error: Incorrect compare result",)
        return None

    def delete(self, val) -> None | tuple:
        if type(self.head.next) is DummyNode:
            return None

        if self.compare(v1=self.tail.prev.value, v2=val) == -1:
            return None

        iter_node = self.head.next
        while type(iter_node) is Node:
            compare_res = self.compare(iter_node.value, val)
            if compare_res == 0:
                iter_node.prev.next = iter_node.next
                iter_node.next.prev = iter_node.prev
                self.count_el -= 1
                return None
            if compare_res == -1:
                iter_node = iter_node.next
                continue
            if compare_res == 1:
                return None
            return ("Error: Incorrect compare result",)
        return None

    def clean(self, asc):
        self.__ascending = asc
        self.head.next = self.tail
        self.head.prev = self.tail
        self.count_el = 0

    def len(self):
        return self.count_el

    def get_all(self):
        r = []
        node = self.head.next
        while type(node) is Node:
            r.append(node.value)
            node = node.next
        return r

    def get_all_v2(self) -> list:
        node = self.head.next
        res = []
        while type(node) is Node:
            prev_node_val = node.prev.value
            next_node_val = node.next.value
            res.append((prev_node_val, node.value, next_node_val))
            node = node.next
        return res


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2) -> int | tuple:
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 == v2:
            return 0

        if self._OrderedList__ascending and v1 < v2:
            return -1
        if not self._OrderedList__ascending and v1 < v2:
            return 1

        if self._OrderedList__ascending and v1 > v2:
            return 1
        if not self._OrderedList__ascending and v1 > v2:
            return -1
        return ("Error: Compare error",)

