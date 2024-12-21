from linked_list import LinkedList, Node, prepare_test_data


def sum_any_linked_list(*args: LinkedList) -> list[int]:
    list_len = args[0].len()
    for linked_list in args:
        if linked_list.len() != list_len:
            return []

    result_list = []
    nodes_list = [node.head for node in args]

    for _ in range(list_len):
        current_sum = 0
        for node_index, node in enumerate(nodes_list):
            current_sum += node.value
            nodes_list[node_index] = node.next
        result_list.append(current_sum)

    return result_list


def test_base_case():
    assert sum_any_linked_list(prepare_test_data()) == [1, 2, 3, 2]
    assert sum_any_linked_list(prepare_test_data(), prepare_test_data()) == [2, 4, 6, 4]
    assert sum_any_linked_list(
        prepare_test_data(), prepare_test_data(), prepare_test_data()
    ) == [3, 6, 9, 6]
    assert not sum_any_linked_list(LinkedList(), LinkedList())


def test_not_equal_list_len():
    data = LinkedList()
    data.add_in_tail(Node(1))
    data.add_in_tail(Node(2))
    assert not sum_any_linked_list(LinkedList(), data)
