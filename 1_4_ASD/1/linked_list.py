class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item: Node):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        res, node = [], self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all_del=False):
        is_del = False
        if self.head.value == val:
            self.head = self.head.next
            is_del = True
        if self.head is None:
            self.tail = None
            return
        if all_del and is_del:
            self.delete(val, all_del)
            return
        self.__recursion_delete(self.head, val, all_del)
        if self.head.next is None or self.head is None:
            self.tail = self.head

    def __recursion_delete(self, curr_node, val_to_del, all_del):
        if curr_node.next is None:
            return

        is_del = False
        next_node = curr_node.next
        if curr_node.next.value == val_to_del:
            is_del = True
            curr_node.next = curr_node.next.next
            next_node = curr_node
        if all_del is False and is_del:
            return
        self.__recursion_delete(next_node, val_to_del, all_del)

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        l_count, node = 0, self.head
        while node is not None:
            l_count += 1
            node = node.next
        return l_count

    def insert(self, after_node, new_node):
        if after_node is None:
            self.__insert_to_head(new_node)
            return

        found_node = self.find(after_node.value)
        if found_node is None:
            return

        is_new_tail = False
        if found_node is self.tail:
            is_new_tail = True
        buffer_node = found_node.next
        found_node.next = new_node
        new_node.next = buffer_node
        if is_new_tail:
            self.tail = new_node

    def __insert_to_head(self, new_node):
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = self.head


def prepare_test_data():
    data = LinkedList()
    data.add_in_tail(Node(1))
    data.add_in_tail(Node(2))
    data.add_in_tail(Node(3))
    data.add_in_tail(Node(2))
    return data


def test_del_all_param_is_false(capsys):
    a = prepare_test_data()

    a.delete(2, False)
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "1\n3\n2\n"
    assert a.head.value == 1
    assert a.head.next.value == 3
    assert a.head.next.next.value == 2
    assert a.tail.value == 2
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


def test_clean(capsys):
    a = prepare_test_data()

    a.clean()
    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == ""


def test_find_all():
    a = prepare_test_data()

    r = a.find_all(2)
    assert len(r) == 2
    assert r[0].value == 2
    assert r[1].value == 2


def test_len():
    a = prepare_test_data()
    assert a.len() == 4

    a.delete(2, True)
    assert a.len() == 2

    a.clean()
    assert a.len() == 0


def test_insert(capsys):
    a = prepare_test_data()

    a.insert(None, Node(99))
    a.insert(Node(3), Node(5))

    a.print_all_nodes()
    captured = capsys.readouterr()
    assert captured.out == "99\n1\n2\n3\n5\n2\n"
    assert a.head.value == 99
    assert a.head.next.value == 1
    assert a.tail.value == 2


def test_insert_to_empty_list():
    a = LinkedList()
    a.insert(None, Node(9))

    assert a.head.value == 9
    assert a.head.next is None
    assert a.tail.value == 9
    assert a.tail.next is None

    a.insert(Node(9), Node(10))
    assert a.head.value == 9
    assert a.head.next.value == 10

    assert a.tail.value == 10
    assert a.tail.next is None


def test_insert_to_tail():
    a = prepare_test_data()
    a.add_in_tail(Node(8))
    a.insert(Node(8), Node(9))

    assert a.head.value == 1
    assert a.head.next.value == 2
    assert a.tail.value == 9
    assert a.tail.next is None

