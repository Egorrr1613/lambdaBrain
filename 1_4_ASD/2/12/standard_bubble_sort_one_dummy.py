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
            next_node = current_node.next
            if current_node.value > next_node.value:
                input_list.delete_by_node(node_to_del=current_node)
                input_list.insert_by_node(
                    after_node=next_node, node_to_insert=current_node
                )
                swapped = True
            else:
                current_node = next_node
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


def test_bubble_any_equal_big_node_1():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(3))

    sort_linked_list(a)
    assert a.get_all_nodes() == [
        (None, 1, 2),
        (1, 2, 3),
        (2, 3, 5),
        (3, 5, 5),
        (5, 5, 5),
        (5, 5, None),
    ]


def test_bubble_any_equal_big_node_2():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(3))

    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 1, 2), (1, 2, 3), (2, 3, 5), (3, 5, None)]

    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(3))

    sort_linked_list(a)
    assert a.get_all_nodes() == [
        (None, 1, 2),
        (1, 2, 3),
        (2, 3, 5),
        (3, 5, 5),
        (5, 5, 5),
        (5, 5, None),
    ]


def test_bubble_any_equal_big_node_3():
    a = LinkedList2()
    a.add_in_tail(Node(1))
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(5))
    a.add_in_tail(Node(2))
    a.add_in_tail(Node(3))
    a.add_in_tail(Node(5))

    sort_linked_list(a)
    assert a.get_all_nodes() == [
        (None, 1, 2),
        (1, 2, 3),
        (2, 3, 5),
        (3, 5, 5),
        (5, 5, 5),
        (5, 5, None),
    ]
