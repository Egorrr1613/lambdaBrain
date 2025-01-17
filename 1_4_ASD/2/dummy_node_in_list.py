class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
        self.is_dummy = False


class DummyNode(Node):
    def __init__(self, v):
        super().__init__(v)
        self.is_dummy = True

class LinkedList2:
    def __init__(self):
        self.head = DummyNode(None)
        self.tail = DummyNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item: Node) -> None:
        item.prev = self.tail.prev
        item.next = self.tail

        self.tail.prev.next = item
        self.tail.prev = item

    def print_all_nodes(self) -> None:
        node = self.head.next
        while node.is_dummy is False:
            print(node.value)
            node = node.next

    def get_all_nodes(self) -> list:
        node = self.head.next
        res = []
        while node.is_dummy is False:
            prev_node_val = node.prev.value
            next_node_val = node.next.value
            res.append((prev_node_val, node.value, next_node_val))
            node = node.next
        return res

    def find(self, val) -> Node | None:
        node = self.head.next
        while node.is_dummy is False:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> list:
        node = self.head.next
        res = []
        while node.is_dummy is False:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, is_all=False) -> None:
        curr_node = self.head.next
        while curr_node.is_dummy is False:
            if not (curr_node.value == val):
                curr_node = curr_node.next
                continue

            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
            curr_node = curr_node.next
            if not is_all:
                return

    def clean(self) -> None:
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self) -> int:
        l_count, node = 0, self.head.next
        while node.is_dummy is False:
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

        curr_node = self.find(after_node.value)
        if curr_node is None:
            return

        new_node.prev = curr_node
        new_node.next = curr_node.next
        new_node.next.prev = new_node
        new_node.prev.next = new_node

    def add_in_head(self, new_node) -> None:
        new_node.prev = self.head
        new_node.next = self.head.next

        self.head.next.prev = new_node
        self.head.next = new_node


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
    assert find_all_list[1].next.is_dummy is True


def test_del_all_param_is_false():
    a = prepare_test_data()

    a.delete(2, False)

    assert a.get_all_nodes() == [(None, 1, 3), (1, 3, 2), (3, 2, None)]
    assert a.head.next.value == 1
    assert a.head.next.next.value == 3
    assert a.head.next.next.next.value == 2
    assert a.tail.prev.value == 2
    assert a.tail.prev.next.value is None
    assert a.len() == 3


def test_del_single_el_in_list():
    a = LinkedList2()
    a.add_in_tail(Node(2))

    a.delete(2, True)

    assert a.get_all_nodes() == []
    assert a.head.next.value is None
    assert a.tail.prev.value is None
    assert a.len() == 0


def test_del_all_el_in_two_el_list():
    a = LinkedList2()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(2))

    a.delete(2, True)
    assert a.get_all_nodes() == []
    assert a.head.next.value is None
    assert a.tail.prev.value is None
    assert a.len() == 0


def test_del_2_el_all_param():
    a = LinkedList2()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(2))

    a.delete(2, True)

    assert a.get_all_nodes() == [(None, 1, None)]
    assert a.head.next.value == 1
    assert a.head.next.next.value is None
    assert a.tail.prev.value == 1
    assert a.tail.prev.next.next is None
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
    assert a.head.next.value == 3
    assert a.head.next.next.value == 4
    assert a.tail.prev.value == 4
    assert a.tail.prev.next.value is None
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
    assert a.head.next.value == 3
    assert a.head.next.next.value == 4
    assert a.tail.prev.value == 4
    assert a.tail.prev.next.value is None


def test_del_el_from_tail(capsys):
    a = LinkedList2()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(3))

    a.delete(3, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "2\n1\n"
    assert a.head.next.value == 2
    assert a.head.next.next.value == 1
    assert a.tail.prev.value == 1
    assert a.tail.prev.next.value is None


def test_del_no_match(capsys):
    a = prepare_test_data()

    a.delete(28, False)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\n2\n"
    assert a.head.next.value == 1
    assert a.head.next.next.value == 2
    assert a.head.next.next.next.value == 3
    assert a.tail.prev.value == 2
    assert a.tail.prev.next.value is None


def test_single_el_after_del():
    a = LinkedList2()
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(3))

    a.delete(5, False)
    assert [(None, 3, None)] == a.get_all_nodes()
    assert a.head.next.value == 3
    assert a.head.next.next.value is None
    assert a.head.next.prev.value is None
    assert a.tail.prev.value == 3
    assert a.tail.prev.next.value is None


def test_del_all_param_is_true(capsys):
    a = prepare_test_data()

    a.delete(2, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "1\n3\n"

    a.delete(1, True)
    assert a.head.next.value == 3
    assert a.head.next.next.value is None
    assert a.tail.prev.value == 3
    assert a.tail.next is None

    a.delete(3, True)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert a.head.next.value is None
    assert a.tail.prev.value is None


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
    assert a.head.next.value == 1
    assert a.head.next.next.value is None
    assert a.tail.prev.value == 1
    assert a.tail.prev.next.value is None


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
    assert a.head.next.value == 1
    assert a.head.next.next.value == 3
    assert a.tail.prev.value == 3
    assert a.tail.prev.next.value is None


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
    assert a.head.next.value == 1
    assert a.head.next.prev.value is None
    assert a.head.next.next.value is None

    assert a.tail.prev.value == 1
    assert a.tail.prev.prev.value is None
    assert a.tail.prev.next.value is None
    assert [(None, 1, None)] == a.get_all_nodes()


    a.insert(after_node=None, new_node=Node(2))
    assert a.head.next.value == 1
    assert a.head.next.prev.value is None
    assert a.head.next.next.value == 2

    assert a.tail.prev.value == 2
    assert a.tail.prev.prev.value == 1
    assert a.tail.prev.next.value is None
    assert [(None, 1, 2), (1, 2, None)] == a.get_all_nodes()


    a.insert(after_node=Node(1), new_node=Node(0))
    assert a.head.next.next.value == 0
    assert a.head.next.prev.value is None
    assert a.head.next.value == 1

    assert a.tail.prev.value == 2
    assert a.tail.prev.prev.prev.value == 1
    assert a.tail.prev.next.value is None
    assert [(None, 1, 0), (1, 0, 2), (0, 2, None)] == a.get_all_nodes()

    a.insert(after_node=Node(1), new_node=Node(1))
    assert [(None, 1, 1), (1, 1, 0), (1, 0, 2), (0, 2, None)] == a.get_all_nodes()

    a.insert(after_node=Node(22), new_node=Node(1))
    assert [(None, 1, 1), (1, 1, 0), (1, 0, 2), (0, 2, None)] == a.get_all_nodes()

    a.delete(1)
    assert [(None, 1, 0), (1, 0, 2), (0, 2, None)] == a.get_all_nodes()

    a.insert(after_node=Node(1), new_node=Node(99))
    assert [(None, 1, 99), (1, 99, 0), (99, 0, 2), (0, 2, None)] == a.get_all_nodes()


def test_base_insert_2():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(4))

    a.insert(Node(2), Node(3))

    assert a.get_all_nodes() == [(None, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, None)]


def test_base_insert_bound_case():
    a = LinkedList2()

    a.insert(None, Node(1))
    assert a.get_all_nodes() == [(None, 1, None)]

    a.insert(None, Node(3))
    assert a.get_all_nodes() == [(None, 1, 3), (1, 3, None)]

    a.insert(Node(1), Node(2))
    assert a.get_all_nodes() == [(None, 1, 2), (1, 2, 3), (2, 3, None)]

    a.insert(None, Node(4))
    assert a.get_all_nodes() == [(None, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, None)]

