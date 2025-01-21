from doubly_linked_list import Node, LinkedList2, prepare_test_data


def has_loop(input_list: LinkedList2) -> bool:
    if input_list.head is None or input_list.tail is None:
        return False
    if input_list.head is input_list.tail:
        return False

    current_node = input_list.head
    for _ in range(input_list.len()):
        current_node = current_node.next

    if current_node is input_list.tail:
        return True
    return False


def test_infinity_loop():
    a = LinkedList2()

    a.add_in_tail(Node(1))
    assert has_loop(a) is False

    a.add_in_tail(Node(2))
    assert has_loop(a) is False

    a.tail.next = a.head
    a.head.prev = a.tail
    assert has_loop(a)


def draft_test():
    b = prepare_test_data()
    assert has_loop(b) is False

    c = LinkedList2()
    c.add_in_tail(Node(1))
    c.add_in_tail(Node(2))
    c.add_in_tail(Node(3))
    c.add_in_tail(Node(4))
    assert has_loop(c) is False

    c.head.next.next.next = c.head
    assert has_loop(c)

    d = LinkedList2()
    assert has_loop(d) is False

    e = LinkedList2()
    e.add_in_tail(Node(1))
    e.add_in_tail(Node(2))
    e.add_in_tail(Node(3))
    e.add_in_tail(Node(4))

    e.head.next.prev = e.head.next.next
    assert has_loop(e)
