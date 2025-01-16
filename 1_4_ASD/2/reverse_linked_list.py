from doubly_linked_list import Node, LinkedList2, prepare_test_data


def reverse_linked_list(input_list: LinkedList2) -> None:
    if input_list.head is None or input_list.tail is None:
        return
    if input_list.head is input_list.tail:
        return

    current_node = input_list.tail
    input_list.head, input_list.tail = input_list.tail, input_list.head
    while current_node is not None:
        current_node.next, current_node.prev = current_node.prev, current_node.next
        current_node = current_node.next
    return


def test_reverse_empty_list():
    a = LinkedList2()
    reverse_linked_list(a)

    assert a.get_all_nodes() == []
    assert a.head is None
    assert a.tail is None


def test_reverse_one_el_in_list():
    a = LinkedList2()
    a.add_in_tail(Node(1))

    reverse_linked_list(a)
    assert a.get_all_nodes() == [(None, 1, None)]

    assert a.head.next is None
    assert a.head.prev is None
    assert a.head.value == 1

    assert a.tail.next is None
    assert a.tail.prev is None
    assert a.tail.value == 1
    assert a.head is a.tail


def test_reverse_two_el_in_list():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(2))

    reverse_linked_list(a)

    assert a.get_all_nodes() == [(None, 2, 1), (2, 1, None)]
    assert a.head.value == 2
    assert a.head.next.value == 1
    assert a.head.prev is None

    assert a.tail.value == 1
    assert a.tail.prev.value == 2
    assert a.tail.next is None


def test_reverse_base_case():
    a = prepare_test_data()
    reverse_linked_list(a)

    assert a.get_all_nodes() == [(None, 2, 3), (2, 3, 2), (3, 2, 1), (2, 1, None)]

    assert a.head.value == 2
    assert a.head.next.value == 3
    assert a.head.prev is None

    assert a.tail.value == 1
    assert a.tail.prev.value == 2
    assert a.tail.next is None
