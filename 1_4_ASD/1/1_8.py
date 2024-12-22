from linked_list import LinkedList, Node, prepare_test_data


def sum_any_linked_list(list_of_linked_lists: list[LinkedList]) -> list[int]:
    count_linked_list = len(list_of_linked_lists)
    if count_linked_list == 0:
        return []

    result_list = []
    count_last_node = 0
    nodes_list = [node.head for node in list_of_linked_lists]

    while True:
        curr_sum = 0
        for node_index, node in enumerate(nodes_list):
            if node is None:
                return []
            if node.next is None:
                count_last_node += 1
            curr_sum += node.value
            nodes_list[node_index] = node.next
        result_list.append(curr_sum)
        if count_last_node == 0:
            continue
        if count_last_node != count_linked_list:
            return []
        return result_list


def test_base_case():
    assert sum_any_linked_list([prepare_test_data()]) == [1, 2, 3, 2]
    assert sum_any_linked_list([prepare_test_data(), prepare_test_data()]) == [
        2,
        4,
        6,
        4,
    ]
    assert sum_any_linked_list(
        [prepare_test_data(), prepare_test_data(), prepare_test_data()]
    ) == [3, 6, 9, 6]
    assert not sum_any_linked_list([LinkedList()])
    assert not sum_any_linked_list([LinkedList(), LinkedList()])
    assert not sum_any_linked_list([])


def test_not_equal_list_len():
    data = LinkedList()
    data.add_in_tail(Node(1))
    data.add_in_tail(Node(2))
    assert not sum_any_linked_list([LinkedList(), data])
    assert not sum_any_linked_list([prepare_test_data(), data])
