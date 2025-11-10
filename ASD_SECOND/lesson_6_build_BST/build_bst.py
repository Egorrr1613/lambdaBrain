class BSTNode:

    def __init__(self, key: int, parent: "BSTNode | None") -> None:
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self) -> None:
        self.Root: BSTNode | None = None  # корень дерева

    def _recursion_create_tree(self, parent_node: BSTNode | None, list_range: list[int], level: int) -> BSTNode | None:
        len_range = len(list_range)
        if len_range == 0:
            return None
        current_middle_index = len_range // 2
        middle_value = list_range[current_middle_index]
        current_node = BSTNode(key=middle_value, parent=parent_node)
        current_node.Level = level
        left_range = list_range[:current_middle_index]
        right_range = list_range[current_middle_index + 1:]

        current_node.LeftChild = self._recursion_create_tree(parent_node=current_node, list_range=left_range,
                                                             level=level + 1)
        if current_node.LeftChild:
            current_node.LeftChild.Parent = current_node

        current_node.RightChild = self._recursion_create_tree(parent_node=current_node, list_range=right_range,
                                                              level=level + 1)
        if current_node.RightChild:
            current_node.RightChild.Parent = current_node

        return current_node

    def GenerateTree(self, input_list: list[int]) -> None:
        list_len = len(input_list)
        if list_len == 0:
            return
        if list_len == 1:
            self.Root = BSTNode(key=input_list[0], parent=None)
            return
        sorted_list = sorted(input_list)
        node_to_recursion = None
        self.Root = self._recursion_create_tree(parent_node=node_to_recursion,
                                                list_range=sorted_list,
                                                level=0)

    def _recursion_find_level(self, current_node: BSTNode, func) -> int:
        if current_node.LeftChild is None and current_node.RightChild is None:
            return current_node.Level

        left_height = self._recursion_find_level(
            current_node.LeftChild, func) if current_node.LeftChild else current_node.Level

        right_height = self._recursion_find_level(
            current_node.RightChild, func) if current_node.RightChild else current_node.Level

        return func(left_height, right_height)

    def IsBalanced(self, root_node: BSTNode | None) -> bool:
        if root_node is None:
            return True

        if not root_node.LeftChild and not root_node.RightChild:
            return True

        max_level = self._recursion_find_level(root_node, max)
        min_level = self._recursion_find_level(root_node, min)

        return abs(max_level - min_level) < 2
