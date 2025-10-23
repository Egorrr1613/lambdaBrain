RIGHT_CHILD = "RIGHT_CHILD"
LEFT_CHILD = "LEFT_CHILD"
PARENT = "PARENT"

calculate_index = {
    RIGHT_CHILD: lambda x: 2 * x + 2,
    LEFT_CHILD: lambda x: 2 * x + 1,
    PARENT: lambda x: (x - 1) // 2,
}


class aBST:

    def _calculate_tree_len(self, current_depth: int, depth: int, tree_len: int) -> int:
        new_tree_len = tree_len + 2**current_depth
        if current_depth == depth:
            return new_tree_len
        return self._calculate_tree_len(
            current_depth=current_depth + 1, depth=depth, tree_len=new_tree_len
        )

    def __init__(self, depth: int):
        tree_size = self._calculate_tree_len(current_depth=0, depth=depth, tree_len=0)
        self.Tree: list[None | int] = [None] * tree_size

    def _recursion_find_key(self, key: int, current_tree_index: int) -> int | None:
        if current_tree_index >= len(self.Tree):
            return None

        current_element = self.Tree[current_tree_index]

        if current_element is None:
            return -current_tree_index

        if key == current_element:
            return current_tree_index

        if key > current_element:
            next_index = calculate_index[RIGHT_CHILD](current_tree_index)
        elif key < current_element:
            next_index = calculate_index[LEFT_CHILD](current_tree_index)
        else:
            assert False, "Некорректное условие"

        return self._recursion_find_key(key=key, current_tree_index=next_index)

    def FindKeyIndex(self, key: int) -> int | None:
        return self._recursion_find_key(key=key, current_tree_index=0)

    def AddKey(self, key):
        if self.Tree[0] is None:
            self.Tree[0] = key
            return 0

        insert_index = self.FindKeyIndex(key=key)
        if insert_index is None:
            return -1
        if insert_index < 0:
            self.Tree[insert_index * -1] = key
            return insert_index * -1
        return insert_index

    def _get_parents_index_list(
        self, node_index: int, parents_index_list: list[int]
    ) -> list:
        if len(parents_index_list) > 0 and parents_index_list[-1] == 0:
            return parents_index_list

        current_parent_index = calculate_index[PARENT](node_index)
        parents_index_list.append(current_parent_index)
        return self._get_parents_index_list(
            node_index=current_parent_index, parents_index_list=parents_index_list
        )

    def WideAllNodes(self) -> tuple[int | None, ...]:
        return tuple(node for node in self.Tree)

    def find_lca(self, first_node_key: int, second_node_key: int) -> int:
        """
        Задание: №4
        Номер задачи из задания: №2
        Краткое название: "Поиск наименьшего общего предка двух узлов"
        Сложность: - size - O(n) / time - O(n)

        Рефлексия:
        """
        first_node_index = self.FindKeyIndex(key=first_node_key)
        second_node_index = self.FindKeyIndex(key=second_node_key)

        if first_node_index is None or first_node_index < 0:
            assert False, f"Ключ {first_node_index} отсутствует в дереве"

        if second_node_index is None or second_node_index < 0:
            assert False, f"Ключ {second_node_index} отсутствует в дереве"

        if first_node_index == 0 or second_node_index == 0:
            assert False, "Для корня нельзя найти общего предка"

        first_node_parent_list = self._get_parents_index_list(
            node_index=first_node_index, parents_index_list=[]
        )
        second_node_parent_list = self._get_parents_index_list(
            node_index=second_node_index, parents_index_list=[]
        )

        common_parents_list = list(
            filter(lambda x: x in second_node_parent_list, first_node_parent_list)
        )
        lca_index = common_parents_list[0]
        return self.Tree[lca_index]
