from linked_list import LinkedList, Node, prepare_test_data


def sum_any_linked_list(*args: LinkedList) -> list[int]:
    list_len = args[0].len()
    for linked_list in args:
        if linked_list.len() != list_len:
            return []

    result_list = []
    nodes_list = [node.head for node in args]

    while nodes_list[0] is not None:
        curr_sum = sum([node.value for node in nodes_list])
        result_list.append(curr_sum)
        nodes_list = [node.next for node in nodes_list]

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
