import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from one_dummy_node_list import LinkedList2, Node, prepare_test_data


def has_loop(input_list: LinkedList2) -> bool:
    if input_list.head is None or input_list.tail is None:
        return False

    start_head_node = input_list.head.next
    start_tail_node = input_list.tail.prev

    for _ in range(input_list.len()):
        start_head_node = start_head_node.next
        start_tail_node = start_tail_node.prev

    if start_head_node is not input_list.tail or start_tail_node is not input_list.head:
        return True

    return False


def test_loop_in_tail_from_head():
    a = LinkedList2()

    a.add_in_tail(Node(1))
    assert has_loop(a) is False

    a.add_in_tail(Node(2))
    assert has_loop(a) is False

    a.tail.next = a.head
    a.head.prev = a.tail
    assert not has_loop(a)


def test_loop_in_no_loop_list():
    b = prepare_test_data()
    assert has_loop(b) is False


def test_has_loop():
    c = LinkedList2()
    c.add_in_tail(Node(1))
    c.add_in_tail(Node(2))
    c.add_in_tail(Node(3))
    c.add_in_tail(Node(4))
    assert has_loop(c) is False

    c.head.next.next = c.head
    assert has_loop(c)

    d = LinkedList2()
    assert has_loop(d) is False


def test_loop_if_prev_link_is_loop():
    e = LinkedList2()
    e.add_in_tail(Node(1))
    e.add_in_tail(Node(2))
    e.add_in_tail(Node(3))
    e.add_in_tail(Node(4))

    e.head.next.prev = e.head.next.next
    assert has_loop(e)


def test_has_loop_2():
    e = LinkedList2()
    e.add_in_tail(Node(1))
    e.add_in_tail(Node(2))
    e.add_in_tail(Node(3))
    e.add_in_tail(Node(4))

    e.tail.prev.next = e.head.next
    assert has_loop(e)


def test_has_loop_3():
    e = LinkedList2()
    e.add_in_tail(Node(1))
    e.add_in_tail(Node(2))
    e.add_in_tail(Node(3))
    e.add_in_tail(Node(4))

    e.tail.prev = e.head.next
    assert has_loop(e)
