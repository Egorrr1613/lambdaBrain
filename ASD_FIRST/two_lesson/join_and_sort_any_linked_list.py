from doubly_linked_list import Node, LinkedList2, prepare_test_data
from sort_linked_list import sort_linked_list

def join_and_sort_any_linked_list(first_l: LinkedList2, second_l: LinkedList2) -> LinkedList2:
    sort_linked_list(first_l)
    sort_linked_list(second_l)

    first_list_curr_node = first_l.head
    second_list_curr_node = second_l.head
    result_list = LinkedList2()

    while (first_list_curr_node is not None) or (second_list_curr_node is not None):
        if first_list_curr_node is None:
            result_list.add_in_tail(Node(second_list_curr_node.value))
            second_list_curr_node = second_list_curr_node.next
            continue

        if second_list_curr_node is None:
            result_list.add_in_tail(Node(first_list_curr_node.value))
            first_list_curr_node = first_list_curr_node.next
            continue

        if first_list_curr_node.value < second_list_curr_node.value:
            result_list.add_in_tail(Node(first_list_curr_node.value))
            first_list_curr_node = first_list_curr_node.next
            continue

        if first_list_curr_node.value >= second_list_curr_node.value:
            result_list.add_in_tail(Node(second_list_curr_node.value))
            second_list_curr_node = second_list_curr_node.next
            continue

        assert False, "Обнаруженно не корректное состояние. Исполнение кода не должно было дойти до этого места."

    return result_list

def test_double_list_join_and_sort():
    a = prepare_test_data()
    b = prepare_test_data()

    c = join_and_sort_any_linked_list(a, b)

    assert c.get_all_nodes() == [(None, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2),
                                 (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, None)]


def test_double_empty_list_join_and_sort():
    a = LinkedList2()
    b = LinkedList2()

    c = join_and_sort_any_linked_list(a, b)

    assert c.get_all_nodes() == []


def test_double_empty_and_not_empty_list_join_and_sort():
    a = LinkedList2()
    b = LinkedList2()
    b.add_in_tail(Node(5))
    b.add_in_tail(Node(6))

    c = join_and_sort_any_linked_list(a, b)

    assert c.get_all_nodes() == [(None, 5, 6), (5, 6, None)]


def test_double_join_diff_len_list():
    a = prepare_test_data()
    b = LinkedList2()
    b.add_in_tail(Node(99))
    b.add_in_tail(Node(2))
    b.add_in_tail(Node(-4))

    c = join_and_sort_any_linked_list(a, b)

    assert c.get_all_nodes() == [(None, -4, 1), (-4, 1, 2), (1, 2, 2), (2, 2, 2),
                                 (2, 2, 3), (2, 3, 99), (3, 99, None)]