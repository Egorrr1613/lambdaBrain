class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

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

    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node

    def is_correct_tree(self) -> bool:
        """
        Задание: №6
        Номер задачи из задания: №2
        Краткое название: "Метод для проверки корректного заполнения бинарного дерева"
        Сложность: - size - O(n) / time - O(n)

        Рефлексия:

        """
        if self.Root is None:
            return True
        search_queue = [self.Root]
        is_correct_tree = True

        while search_queue:
            check_node = search_queue.pop(0)
            if check_node.LeftChild:
                search_queue.append(check_node.LeftChild)
                is_correct_tree = True if check_node.NodeKey > check_node.LeftChild.NodeKey else False
            if check_node.RightChild:
                search_queue.append(check_node.RightChild)
                is_correct_tree = True if check_node.NodeKey <= check_node.RightChild.NodeKey and is_correct_tree else False
            if not is_correct_tree:
                return False

        return True
