class BSTNode:

    def __init__(self, key: int, parent: "BSTNode | None") -> None:
        self.NodeKey = key
        self.Parent: BSTNode | None = parent
        self.LeftChild: BSTNode | None = None
        self.RightChild: BSTNode | None = None
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
        """
        Задание: №6
        Номер задачи из задания: №3
        Краткое название: "Метод определения сбалансированности дерева"
        Сложность: - size - O(n) / time - O(n)

        Рефлексия:
            Я вычисляю максимальную и минимальную высоту, относительно корня дерева.
            Кажется что если дерево где-то не является сбалансированным -
                тогда разница между наиболее высоким и наиболее коротким поддеревом будет составлять больше 1.
            И в таком случае, если считать длины относительно корня - то эта разница будет точно выявленная,
                без необходимости рекурсивной проверки высот поддеревьев.
            Думаю, что я прав, так как моделировал разные НЕ сбалансированные деревья
                и в каждом случае мой вариант проверки срабатывал корректно.
        """
        if root_node is None:
            return True

        if not root_node.LeftChild and not root_node.RightChild:
            return True

        max_level = self._recursion_find_level(root_node, max)
        min_level = self._recursion_find_level(root_node, min)
        return (max_level - min_level) < 2

    def is_correct_tree(self) -> bool:
        """
        Задание: №6
        Номер задачи из задания: №2
        Краткое название: "Метод для проверки корректного заполнения бинарного дерева"
        Сложность: - size - O(n) / time - O(n)

        Рефлексия:
            В рекомендованном решении предлагается использовать рекурсию для корректного распределения значений.
            Была идея реализовать так же, однако мне понравился алгоритм обхода в ширину с использованием очереди.
            Хотел закрепить и запомнить его, поэтому решил чуть модифицировать такой алгоритм для решения этой задачи.
        """
        if self.Root is None:
            return True
        search_queue = [self.Root]
        is_correct_tree = True

        while search_queue:
            check_node = search_queue.pop(0)
            if check_node.LeftChild:
                search_queue.append(check_node.LeftChild)
                is_correct_tree = check_node.NodeKey > check_node.LeftChild.NodeKey
            if check_node.RightChild:
                search_queue.append(check_node.RightChild)
                is_correct_tree = bool(check_node.NodeKey <= check_node.RightChild.NodeKey and is_correct_tree)
            if not is_correct_tree:
                return False

        return True
