import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from one_dummy_node_list import Node, LinkedList2, prepare_test_data


def sort_linked_list(input_list: LinkedList2) -> None:
    count_step = input_list.len() - 1
    swapped = True
    while swapped:
        current_node = input_list.head.next

        swapped = False
        for _ in range(count_step):
            if current_node.value > current_node.next.value:
                node_prev_change = current_node.prev
                node_after_change = current_node.next.next

                node_prev_change.next = current_node.next
                node_after_change.prev = current_node

                node_moved_back = current_node.next

                current_node.next = node_moved_back.next
                node_moved_back.prev = current_node.prev

                node_moved_back.next = current_node
                current_node.prev = node_moved_back
                swapped = True
            else:
                current_node = current_node.next
        count_step -= 1


def test_sort_2_el():
    a = LinkedList2()
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(1))
    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 1, 2), (1, 2, None)]



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


def test_no_need_sort_one_el_lin_tail():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(3))
    a.add_in_tail(Node(2))

    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 1, 2), (1, 2, 2), (2, 2, 3), (2, 3, None)]
