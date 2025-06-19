from doubly_linked_list import Node, LinkedList2, prepare_test_data


def bubble_node_sort(current_node: Node, start_node: Node, stop_node: Node) -> None:
    while start_node is not stop_node:
        while current_node is not stop_node:
            next_node = current_node.next
            if current_node.value > current_node.next.value:
                buffer_val = current_node.value
                current_node.value = next_node.value
                next_node.value = buffer_val
            current_node = next_node
        stop_node = stop_node.prev
        current_node = start_node


def sort_linked_list(input_list: LinkedList2) -> None:
    if input_list.head is None or input_list.tail is None:
        return
    bubble_node_sort(input_list.head, input_list.head, input_list.tail)


def test_base_sort():
    a = prepare_test_data()
    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 1, 2), (1, 2, 2), (2, 2, 3), (2, 3, None)]


def test_sort_empty_list():
    a = LinkedList2()
    sort_linked_list(a)
    assert not a.get_all_nodes()


def test_sort_one_el_list():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 1, None)]


def test_sort_two_el_list():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(0))
    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 0, 1), (0, 1, None)]


def test_sort_two_el_list_no_need_sort():
    a = LinkedList2()
    a.add_in_tail(Node(0))
    a.add_in_tail(Node(1))
    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 0, 1), (0, 1, None)]


def test_sort_any_el_list():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(0))
    a.add_in_tail(Node(-1))
    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, -1, 0), (-1, 0, 1), (0, 1, None)]

    b = LinkedList2()
    b.add_in_tail(Node(3))
    b.add_in_tail(Node(2))
    b.add_in_tail(Node(1))
    sort_linked_list(b)
    assert b.get_all_nodes() == [(None, 1, 2), (1, 2, 3), (2, 3, None)]


def test_no_need_sort_any_el_list():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(1))

    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 1, 1), (1, 1, 1), (1, 1, None)]


def test_no_need_sort_any_el_list_2():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(3))

    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 1, 2), (1, 2, 3), (2, 3, None)]
