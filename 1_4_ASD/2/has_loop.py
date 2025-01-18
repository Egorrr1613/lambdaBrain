from doubly_linked_list import Node, LinkedList2, prepare_test_data

def has_loop(input_list: LinkedList2) -> bool:
    if input_list.head is None or input_list.tail is None:
        return False
    if input_list.head is input_list.tail:
        return False

    first_node = input_list.head
    second_node = input_list.head
    while first_node is not None and first_node.next is not None:
        first_node = first_node.next.next
        second_node = second_node.next
        if second_node == first_node:
            return True

    first_node = input_list.tail
    second_node = input_list.tail
    while first_node is not None and first_node.prev is not None:
        first_node = first_node.prev.prev
        second_node = second_node.prev
        if second_node == first_node:
            return True

    return False

def test_check_loop():
    a = LinkedList2()

    a.add_in_tail(Node(1))
    assert has_loop(a) is False

    a.add_in_tail(Node(2))
    assert has_loop(a) is False

    a.tail.next = a.head
    a.head.prev = a.tail
    assert has_loop(a)

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

