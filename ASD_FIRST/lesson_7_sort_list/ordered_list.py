class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc: bool):
        self.head: Node | None = None
        self.tail: Node | None = None

        self.__ascending = asc
        self.count_el = 0

    def compare(self, v1, v2) -> int | tuple[str]:
        if v1 == v2:
            return 0

        if self.__ascending and v1 < v2:
            return -1
        if not self.__ascending and v1 > v2:
            return -1
        if not self.__ascending and v1 < v2:
            return 1
        if self.__ascending and v1 > v2:
            return 1
        return ("Error: Compare error",)

    def add(self, value) -> None | tuple[str]:
        assert isinstance(value, str), "Добавляемые данные должны быть типа str"
        new_node = Node(value)

        if self.count_el == 0:
            self.head = new_node
            self.tail = new_node

            self.count_el += 1
            return None

        if self.count_el == 1:
            compare_result = self.compare(v1=self.tail.value, v2=new_node.value)
            if compare_result in (0, 1):
                self.head = new_node
                new_node.next = self.tail
                self.tail.prev = self.head
            if compare_result == -1:
                self.tail = new_node
                self.head.next = self.tail
                self.tail.prev = self.head
            self.count_el += 1
            return None

        if self.compare(v1=self.tail.value, v2=new_node.value) == -1:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

            self.count_el += 1
            return None

        iter_node = self.head
        while isinstance(iter_node, Node):
            compare_result = self.compare(iter_node.value, new_node.value)

            if compare_result in (0, 1):
                new_node.prev = iter_node.prev
                new_node.next = iter_node

                if iter_node is self.head:
                    self.head = new_node
                else:
                    iter_node.prev.next = new_node
                iter_node.prev = new_node
                self.count_el += 1
                return None

            if compare_result == -1:
                iter_node = iter_node.next
                continue

            return ("Error: Incorrect compare result",)
        return ("Error: Incorrect state",)

    def find(self, val) -> Node | None | tuple[str]:
        iter_node = self.head
        while isinstance(iter_node, Node):
            compare_res = self.compare(val, iter_node.value)
            if compare_res == 0:
                return iter_node
            if compare_res == -1:
                return None
            if compare_res == 1:
                iter_node = iter_node.next
                continue
            return ("Error: Incorrect compare result",)
        return None

    def delete(self, val) -> None:
        if self.head is None or self.compare(v1=self.tail.value, v2=val) == -1:
            return None

        iter_node = self.head
        while isinstance(iter_node, Node):
            compare_res = self.compare(iter_node.value, val)
            if compare_res == 0:

                if iter_node is self.head and iter_node is self.tail:
                    self.head = None
                    self.tail = None
                    self.count_el = 0
                    return None

                if iter_node is self.head:
                    self.head = iter_node.next
                    self.head.prev = None
                    self.count_el -= 1
                    return None

                if iter_node is self.tail:
                    self.tail = iter_node.prev
                    self.tail.next = None
                    self.count_el -= 1
                    return None

                iter_node.prev.next = iter_node.next
                iter_node.next.prev = iter_node.prev

                self.count_el -= 1
                return None
            if compare_res == 1:
                return None
            if compare_res == -1:
                iter_node = iter_node.next
        return None

    def clean(self, asc) -> None:
        self.__ascending = asc
        self.head = None
        self.tail = None
        self.count_el = 0

    def len(self) -> int:
        return self.count_el

    def get_all(self) -> list:
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def get_all_v2(self) -> list:
        node: Node | None = self.head
        res = []
        while isinstance(node, Node):
            if node is self.head:
                prev_node_val = None
            else:
                prev_node_val = node.prev.value
            if node is self.tail:
                next_node_val = None
            else:
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

