from doubly_linked_list import Node, LinkedList2, prepare_test_data

def has_loop(input_list: LinkedList2) -> bool:
    check_nodes = []
    if input_list.head is None or input_list.tail is None:
        return False
    if input_list.head is input_list.tail:
        return False

    curr_node = input_list.head
    while curr_node is not None:
        if curr_node in check_nodes:
            return True
        check_nodes.append(curr_node)
        if curr_node.prev is not None and curr_node.prev not in check_nodes:
            return True
        curr_node = curr_node.next
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

