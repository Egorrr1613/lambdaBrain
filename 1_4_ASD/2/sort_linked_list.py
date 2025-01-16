from doubly_linked_list import Node, LinkedList2, prepare_test_data


def sort_linked_list(input_list: LinkedList2) -> None:
    if input_list.head is None or input_list.tail is None:
        return

    nodes_dict: dict[int, list[Node]] = {}
    current_node = input_list.head
    while current_node is not None:
        if nodes_dict.get(current_node.value):
            nodes_dict[current_node.value].append(current_node)
        else:
            nodes_dict[current_node.value] = [current_node]
        current_node = current_node.next

    sorted_values = sorted(list(nodes_dict.keys()))
    prev_node = None
    for val in sorted_values:
        for iter_node in nodes_dict[val]:
            if prev_node is None:
                iter_node.prev = prev_node
                prev_node = iter_node
                continue
            prev_node.next = iter_node
            iter_node.prev = prev_node
            prev_node = iter_node

    input_list.head = nodes_dict[sorted_values[0]][0]
    input_list.tail = nodes_dict[sorted_values[-1]][-1]
    input_list.tail.next = None


def test_base_sort():
    a = prepare_test_data()
    sort_linked_list(a)
    assert a.get_all_nodes() == [(None, 1, 2), (1, 2, 2), (2, 2, 3), (2, 3, None)]


def test_sort_empty_list():
    a = LinkedList2()
    sort_linked_list(a)
    assert a.get_all_nodes() == []


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
