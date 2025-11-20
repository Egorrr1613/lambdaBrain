RIGHT_CHILD = "RIGHT_CHILD"
LEFT_CHILD = "LEFT_CHILD"
PARENT = "PARENT"

calculate_index = {
    RIGHT_CHILD: lambda x: 2 * x + 2,
    LEFT_CHILD: lambda x: 2 * x + 1,
    PARENT: lambda x: (x - 1) // 2,
}


def GenerateBBSTArray(input_list: list[int]) -> list[int]:
    len_tree = len(input_list)
    if len_tree in (0, 1):
        return input_list

    sort_input_list = sorted(input_list)

    tree_list: list[int | None] = [None] * len_tree
    _recursion_generate_tree(sorted_list=sort_input_list,
                             list_to_tree=tree_list,
                             len_tree=len_tree,
                             current_index_in_tree=0)
    return tree_list


def _recursion_generate_tree(sorted_list: list[int],
                             list_to_tree: list[None | int],
                             len_tree: int,
                             current_index_in_tree: int) -> None:
    if not sorted_list:
        return

    middle_element_index = len_tree // 2
    left_sublist = sorted_list[:middle_element_index]
    right_sublist = sorted_list[middle_element_index + 1:]

    list_to_tree[current_index_in_tree] = sorted_list[middle_element_index]

    _recursion_generate_tree(sorted_list=left_sublist,
                             list_to_tree=list_to_tree,
                             len_tree=len(left_sublist),
                             current_index_in_tree=calculate_index[LEFT_CHILD](current_index_in_tree))

    _recursion_generate_tree(sorted_list=right_sublist,
                             list_to_tree=list_to_tree,
                             len_tree=len(right_sublist),
                             current_index_in_tree=calculate_index[RIGHT_CHILD](current_index_in_tree))

