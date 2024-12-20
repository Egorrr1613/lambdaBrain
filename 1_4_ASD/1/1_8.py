from linked_list import LinkedList, Node, prepare_test_data


def sum_two_linked_list(first_list: LinkedList, second_list: LinkedList) -> list[int]:
    if first_list.len() != second_list.len():
        return []
    first_node, second_node, result_list = first_list.head, second_list.head, []
    while first_node is not None:
        result_list.append(first_node.value + second_node.value)
        first_node, second_node = first_node.next, second_node.next
    return result_list


def test_base_case():
    assert sum_two_linked_list(prepare_test_data(), prepare_test_data()) == [2, 4, 6, 4]
    assert sum_two_linked_list(LinkedList(), LinkedList()) == []


def test_not_equal_list_len():
    data = LinkedList()
    data.add_in_tail(Node(1))
    data.add_in_tail(Node(2))
    assert sum_two_linked_list(LinkedList(), data) == []

