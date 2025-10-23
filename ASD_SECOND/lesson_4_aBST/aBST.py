RIGHT_CHILD = "RIGHT_CHILD"
LEFT_CHILD = "LEFT_CHILD"
PARENT = "PARENT"

calculate_index = {
    RIGHT_CHILD: lambda x: 2 * x + 2,
    LEFT_CHILD: lambda x: 2 * x + 1,
    PARENT: lambda x: (x - 1) / 2,
}


class aBST:

    def _calculate_tree_len(self, current_depth: int, depth: int, tree_len: int) -> int:
        new_tree_len = tree_len + 2 ** current_depth
        if current_depth == depth:
            return new_tree_len
        return self._calculate_tree_len(
            current_depth=current_depth + 1, depth=depth, tree_len=new_tree_len
        )

    def __init__(self, depth: int) -> None:
        tree_size = self._calculate_tree_len(current_depth=0, depth=depth, tree_len=0)
        self.Tree: list[None | int] = [None] * tree_size

    def _recursion_find_key(self, key: int, current_tree_index: int) -> int | None:
        if current_tree_index >= len(self.Tree):
            return None

        current_node = self.Tree[current_tree_index]
        if current_node is None:
            return -current_tree_index

        if key == current_node:
            return current_tree_index

        if key > current_node:
            next_index = calculate_index[RIGHT_CHILD](current_tree_index)
        elif key < current_node:
            next_index = calculate_index[LEFT_CHILD](current_tree_index)
        else:
            raise AssertionError("Некорректное условие")

        return self._recursion_find_key(key=key, current_tree_index=next_index)

    def FindKeyIndex(self, key: int) -> int | None:
        return self._recursion_find_key(key=key, current_tree_index=0)

    def AddKey(self, key: int) -> int:
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

    def WideAllNodes(self) -> tuple[int | None, ...]:
        return tuple(node for node in self.Tree)
