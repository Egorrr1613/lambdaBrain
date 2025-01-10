class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item: Node) -> None:
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self) -> None:
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def get_all_nodes(self) -> list:
        node = self.head
        res = []
        while node is not None:
            prev_node = node.prev if node is self.head else node.prev.value
            next_node = None if node.next is None else node.next.value
            res.append((prev_node, node.value, next_node))
            node = node.next
        return res

    def find(self, val) -> Node | None:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> list:
        node = self.head
        res = []
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, is_all=False) -> None:
        curr_node = self.head
        while True:
            if curr_node is None:
                break
            if not (curr_node.value == val):
                curr_node = curr_node.next
                continue

            if curr_node is self.head and curr_node is self.tail:
                self.head = None
                self.tail = None
                return

            if curr_node is self.head:
                self.head = curr_node.next
                self.head.prev = None

                curr_node = curr_node.next
                if is_all:
                    continue
                return

            if curr_node is self.tail:
                self.tail = curr_node.prev
                self.tail.next = None

                curr_node = curr_node.next
                if is_all:
                    continue
                return

            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
            curr_node = curr_node.next
            if not is_all:
                return

    def clean(self) -> None:
        self.head = None
        self.tail = None

    def len(self) -> int:
        l_count, node = 0, self.head
        while node is not None:
            l_count += 1
            node = node.next
        return l_count

    def insert(self, after_node, new_node) -> None:
        if after_node is None and self.len() == 0:
            self.add_in_head(new_node)
            return
        if after_node is None and self.len() > 0:
            self.add_in_tail(new_node)
            return

        if after_node is None:
            return

        curr_node = self.head

        while curr_node is not None:
            if curr_node.value == after_node.value:
                break
            curr_node = curr_node.next

        if curr_node is None:
            return

        if curr_node is self.head:
            new_node.prev = None
            new_node.next = self.head

            self.head.prev = new_node
            self.head = new_node
            return

        if curr_node is self.tail:
            buffer = self.tail
            self.tail = new_node

            buffer.next = self.tail
            self.tail.prev = buffer
            self.tail.next = None
            return

        new_node.prev = curr_node
        new_node.next = curr_node.next
        new_node.next.prev = new_node
        new_node.prev.next = new_node

    def add_in_head(self, new_node) -> None:
        new_node.prev = None

        if self.head is None:
            self.head = new_node
            self.head.next = None
            self.tail = self.head
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


def prepare_test_data():
    data = LinkedList2()
    data.add_in_tail(Node(1))
    data.add_in_tail(Node(2))
    data.add_in_tail(Node(3))
    data.add_in_tail(Node(2))
    return data


def test_find():
    test_list = prepare_test_data()
    assert test_list.find(5) is None

    node_3 = test_list.find(3)
    assert node_3.value == 3
    assert node_3.next.value == 2


def test_find_all():
    test_list = prepare_test_data()
    find_all_list = test_list.find_all(2)
    assert len(find_all_list) == 2
    assert find_all_list[0].next.value == 3
    assert find_all_list[1].next is None


def test_del_all_param_is_false():
    a = prepare_test_data()

    a.delete(2, False)

    assert a.get_all_nodes() == [(None, 1, 3), (1, 3, 2), (3, 2, None)]
    assert a.head.value == 1
    assert a.head.next.value == 3
    assert a.head.next.next.value == 2
    assert a.tail.value == 2
    assert a.tail.next is None
    assert a.len() == 3


def test_del_single_el_in_list():
    a = LinkedList2()
    a.add_in_tail(Node(2))

    a.delete(2, True)

    assert a.get_all_nodes() == []
    assert a.head is None
    assert a.tail is None
    assert a.len() == 0


def test_del_all_el_in_two_el_list():
    a = LinkedList2()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(2))

    a.delete(2, True)
    assert a.get_all_nodes() == []
    assert a.head is None
    assert a.tail is None
    assert a.len() == 0


def test_del_2_el_all_param():
    a = LinkedList2()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(2))

    a.delete(2, True)

    assert a.get_all_nodes() == [(None, 1, None)]
    assert a.head.value == 1
    assert a.head.next is None
    assert a.tail.value == 1
    assert a.tail.next is None
    assert a.len() == 1


def test_del_el_from_head(capsys):
    a = LinkedList2()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(3))
    a.add_in_tail(Node(4))

    a.delete(2, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "3\n4\n"
    assert a.head.value == 3
    assert a.head.next.value == 4
    assert a.tail.value == 4
    assert a.tail.next is None
    assert a.len() == 2


def test_del_any_el_from_head(capsys):
    a = LinkedList2()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(3))
    a.add_in_tail(Node(4))

    a.delete(2, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "3\n4\n"
    assert a.head.value == 3
    assert a.head.next.value == 4
    assert a.tail.value == 4
    assert a.tail.next is None


def test_del_el_from_tail(capsys):
    a = LinkedList2()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(3))

    a.delete(3, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "2\n1\n"
    assert a.head.value == 2
    assert a.head.next.value == 1
    assert a.tail.value == 1
    assert a.tail.next is None


def test_del_no_match(capsys):
    a = prepare_test_data()

    a.delete(28, False)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\n2\n"
    assert a.head.value == 1
    assert a.head.next.value == 2
    assert a.head.next.next.value == 3
    assert a.tail.value == 2
    assert a.tail.next is None


def test_single_el_after_del():
    a = LinkedList2()
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(3))

    a.delete(5, False)
    assert [(None, 3, None)] == a.get_all_nodes()
    assert a.head.value == 3
    assert a.head.next is None
    assert a.head.prev is None
    assert a.tail.value == 3
    assert a.tail.next is None
    assert a.tail.prev is None


def test_del_all_param_is_true(capsys):
    a = prepare_test_data()

    a.delete(2, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "1\n3\n"

    a.delete(1, True)
    assert a.head.value == 3
    assert a.head.next is None
    assert a.tail.value == 3
    assert a.tail.next is None

    a.delete(3, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert a.head is None
    assert a.tail is None


def test_del_all_param_is_true_bound_case(capsys):
    a = prepare_test_data()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(2))

    a.delete(2, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "1\n3\n"

    a.delete(3, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "1\n"
    assert a.head.value == 1
    assert a.head.next is None
    assert a.tail.value == 1
    assert a.tail.next is None


def test_all_param_is_true_one_deleted_el(capsys):
    a = prepare_test_data()

    a.delete(1, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "2\n3\n2\n"


def test_del_any_el_from_tail(capsys):
    a = prepare_test_data()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(2))

    a.delete(2, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "1\n3\n"
    assert a.head.value == 1
    assert a.head.next.value == 3
    assert a.tail.value == 3
    assert a.tail.next is None


def test_insert_to_head():
    a = prepare_test_data()
    a.add_in_head(Node(10))
    a.add_in_head(Node(9))

    assert [
        (None, 9, 10),
        (9, 10, 1),
        (10, 1, 2),
        (1, 2, 3),
        (2, 3, 2),
        (3, 2, None),
    ] == a.get_all_nodes()


def test_clean():
    a = prepare_test_data()
    a.clean()
    assert a.get_all_nodes() == []


def test_insert_to_head_in_empty_list():
    a = LinkedList2()
    a.add_in_head(Node(5))
    assert [(None, 5, None)] == a.get_all_nodes()

    a.add_in_head(Node(4))
    assert [(None, 4, 5), (4, 5, None)] == a.get_all_nodes()

    a.add_in_head(Node(3))
    assert [(None, 3, 4), (3, 4, 5), (4, 5, None)] == a.get_all_nodes()


def test_base_insert():
    a = LinkedList2()
    a.insert(after_node=None, new_node=Node(1))
    assert a.head.value == 1
    assert a.head.prev is None
    assert a.head.next is None

    assert a.tail.value == 1
    assert a.tail.prev is None
    assert a.tail.next is None

    a.insert(after_node=None, new_node=Node(2))
    assert a.head.value == 1
    assert a.head.prev is None
    assert a.head.next.value == 2

    assert a.tail.value == 2
    assert a.tail.prev.value == 1
    assert a.tail.next is None

    a.insert(after_node=Node(1), new_node=Node(0))
    assert a.head.value == 0
    assert a.head.prev is None
    assert a.head.next.value == 1

    assert a.tail.value == 2
    assert a.tail.prev.value == 1
    assert a.tail.next is None

    assert [(None, 0, 1), (0, 1, 2), (1, 2, None)] == a.get_all_nodes()

    a.insert(after_node=Node(1), new_node=Node(1))
    assert [(None, 0, 1), (0, 1, 1), (1, 1, 2), (1, 2, None)] == a.get_all_nodes()

    a.insert(after_node=Node(22), new_node=Node(1))
    assert [(None, 0, 1), (0, 1, 1), (1, 1, 2), (1, 2, None)] == a.get_all_nodes()

    a.delete(1)
    assert [(None, 0, 1), (0, 1, 2), (1, 2, None)] == a.get_all_nodes()

    a.insert(after_node=Node(1), new_node=Node(99))
    assert [(None, 0, 1), (0, 1, 99), (1, 99, 2), (99, 2, None)] == a.get_all_nodes()

