class RelationshipType:
    ROOT = "ROOT"
    LEFT_CHILD = "LEFT_CHILD"
    RIGHT_CHILD = "RIGHT_CHILD"


class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent: BSTNode | None = parent
        self.LeftChild: BSTNode | None = None
        self.RightChild: BSTNode | None = None


class BSTFind:
    def __init__(self):
        self.Node: None | BSTNode = None
        self.NodeHasKey: bool = False
        self.ToLeft: bool = False


class BST:
    def __init__(self, node: BSTNode | None):
        self.Root = node  # корень дерева, или None
        self.count = 1 if type(node) is BSTNode else 0

    def FindNodeByKey(self, key) -> BSTFind:
        if self.Root is None:
            return BSTFind()
        return self._recursion_find(check_node=self.Root, find_key=key)

    def _recursion_find(self, check_node: BSTNode, find_key) -> BSTFind:
        if check_node.NodeKey == find_key:
            find_result = BSTFind()
            find_result.Node = check_node
            find_result.NodeHasKey = True
            return find_result
        next_node_to_check = None
        if check_node.NodeKey < find_key and type(check_node.RightChild) is BSTNode:
            next_node_to_check = check_node.RightChild
        if check_node.NodeKey > find_key and type(check_node.LeftChild) is BSTNode:
            next_node_to_check = check_node.LeftChild
        if next_node_to_check is None:
            current_node_is_find_result = BSTFind()
            current_node_is_find_result.Node = check_node
            current_node_is_find_result.NodeHasKey = False
            current_node_is_find_result.ToLeft = (
                True if check_node.NodeKey > find_key else False
            )
            return current_node_is_find_result
        return self._recursion_find(check_node=next_node_to_check, find_key=find_key)

    def AddKeyValue(self, key, val) -> bool:
        if self.Count() == 0:
            self.Root = BSTNode(key=key, val=val, parent=None)
            self.count = 1
            return True

        bst_find_result = self._recursion_find(check_node=self.Root, find_key=key)

        if bst_find_result.Node is None or bst_find_result.NodeHasKey is True:
            return False

        if bst_find_result.ToLeft:
            bst_find_result.Node.LeftChild = BSTNode(
                key=key, val=val, parent=bst_find_result.Node
            )
        else:
            bst_find_result.Node.RightChild = BSTNode(
                key=key, val=val, parent=bst_find_result.Node
            )
        self.count += 1
        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        if FindMax and FromNode.RightChild is None:
            return FromNode
        if not FindMax and FromNode.LeftChild is None:
            return FromNode
        next_node = FromNode.RightChild if FindMax else FromNode.LeftChild
        return self.FinMinMax(FromNode=next_node, FindMax=FindMax)

    def _is_node_right_child_or_root(self, node: BSTNode) -> str:
        if node is self.Root:
            return RelationshipType.ROOT
        if node.Parent.RightChild is node:
            return RelationshipType.RIGHT_CHILD
        if node.Parent.LeftChild is node:
            return RelationshipType.LEFT_CHILD
        assert False, "Некорректный тип отношений"

    def _get_replacement_node(self, node: BSTNode) -> BSTNode | None:
        if node.LeftChild is None and node.RightChild is None:
            return None
        if node.LeftChild is None and type(node.RightChild) is BSTNode:
            return node.RightChild
        if type(node.LeftChild) is BSTNode and node.RightChild is None:
            return node.LeftChild
        return self.FinMinMax(FromNode=node.RightChild, FindMax=False)

    def _delete_leaf(self, node) -> bool:
        relation = self._is_node_right_child_or_root(node)

        if relation not in [
            RelationshipType.ROOT,
            RelationshipType.LEFT_CHILD,
            RelationshipType.RIGHT_CHILD,
        ]:
            assert False, "Возник необрабатываемый случай при удалении листа"

        if relation == RelationshipType.ROOT:
            self.Root = None
            self.count = 0
            return True

        if relation == RelationshipType.RIGHT_CHILD:
            node.Parent.RightChild = None

        if relation == RelationshipType.LEFT_CHILD:
            node.Parent.LeftChild = None
        self.count -= 1
        return True

    def _delete_single_child_node(self, del_node: BSTNode, replace_node: BSTNode):
        relationship = self._is_node_right_child_or_root(del_node)

        if relationship not in [
            RelationshipType.ROOT,
            RelationshipType.LEFT_CHILD,
            RelationshipType.RIGHT_CHILD,
        ]:
            assert False, "Возник необрабатываемый случай при удалении узла с одним потомком"

        if del_node.RightChild is not replace_node and del_node.LeftChild is not replace_node:
            assert False, "При удалении узла с одной нодой замещающий узел должен быть прямым потомком"

        if relationship == RelationshipType.ROOT:
            replace_node.Parent = None
            self.Root = replace_node
        else:
            replace_node.Parent = del_node.Parent

        if relationship == RelationshipType.LEFT_CHILD:
            del_node.Parent.LeftChild = replace_node

        if relationship == RelationshipType.RIGHT_CHILD:
            del_node.Parent.RightChild = replace_node

        self.count -= 1
        return True

    def _delete_node_with_two_child(self, del_node, replace_node) -> bool:
        relationship = self._is_node_right_child_or_root(del_node)

        if relationship not in [
            RelationshipType.ROOT,
            RelationshipType.LEFT_CHILD,
            RelationshipType.RIGHT_CHILD,
        ]:
            assert False, "Возник необрабатываемый случай при удалении узла с одним потомком"

        if relationship == RelationshipType.ROOT:
            if del_node.RightChild is not replace_node:
                assert False, ("Если удаляем root узел с двумя наследниками, "
                               "один из которых замещающий - то замещающим может быть только правый узел")

            self.Root = replace_node
            replace_node.Parent = None

            replace_node.LeftChild = del_node.LeftChild
            replace_node.LeftChild.Parent = replace_node
            self.count -= 1
            return True

        if relationship == RelationshipType.RIGHT_CHILD:
            del_node.Parent.RightChild = replace_node
        if relationship == RelationshipType.LEFT_CHILD:
            del_node.Parent.LeftChild = replace_node

        if del_node.RightChild is replace_node:
            assert replace_node.LeftChild is None, "у замещающего узла левый потомок должен быть None"
            replace_node.Parent = del_node.Parent
            replace_node.LeftChild = del_node.LeftChild
            replace_node.LeftChild.Parent = replace_node
            self.count -= 1
            return True

        assert replace_node.Parent.LeftChild is replace_node, "Узел для замещения может быть только левым потомком"
        replace_node.Parent.LeftChild = None
        replace_node.Parent = del_node.Parent
        replace_node.LeftChild = del_node.LeftChild
        del_node.LeftChild.Parent = replace_node
        replace_node.RightChild = del_node.RightChild
        del_node.RightChild.Parent = replace_node
        self.count -= 1
        return True

    def DeleteNodeByKey(self, key) -> bool:
        find_result_node = self.FindNodeByKey(key)
        if not find_result_node.NodeHasKey:
            return False

        node_to_del = find_result_node.Node
        node_to_replace = self._get_replacement_node(node=node_to_del)

        # Если удаляем "лист", то есть у node_to_del нет "детей"
        if node_to_del.RightChild is None and node_to_del.LeftChild is None:
            assert (
                    node_to_replace is None
            ), "Если удаляем 'лист', тогда node_to_replace всегда должен быть None"
            return self._delete_leaf(node=node_to_del)

        # Если удаляем узел с одним потомком
        if node_to_del.RightChild is None or node_to_del.LeftChild is None:
            return self._delete_single_child_node(
                del_node=node_to_del, replace_node=node_to_replace
            )

        # Если удаляем узел с двумя потомками
        if type(node_to_del.RightChild) is BSTNode and type(node_to_del.LeftChild) is BSTNode:
            return self._delete_node_with_two_child(del_node=node_to_del, replace_node=node_to_replace)

    def Count(self):
        return self.count

    def WideAllNodes(self) -> tuple[BSTNode | None]:
        if self.Root is None:
            return tuple()
        search_queue = []
        if self.Root.LeftChild:
            search_queue.append(self.Root.LeftChild)
        if self.Root.RightChild:
            search_queue.append(self.Root.RightChild)

        all_nodes = [self.Root] + search_queue[:]
        while search_queue:
            check_node = search_queue.pop(0)
            if check_node.LeftChild:
                search_queue.append(check_node.LeftChild)
                all_nodes.append(check_node.LeftChild)
            if check_node.RightChild:
                search_queue.append(check_node.RightChild)
                all_nodes.append(check_node.RightChild)
        return tuple(all_nodes)

    def _recursion_deep_in_order(self, current_node: BSTNode, all_nodes: list[BSTNode]) -> list[BSTNode]:
        if current_node.LeftChild:
            self._recursion_deep_in_order(current_node=current_node.LeftChild, all_nodes=all_nodes)
        all_nodes.append(current_node)
        if current_node.RightChild:
            self._recursion_deep_in_order(current_node=current_node.RightChild, all_nodes=all_nodes)
        return all_nodes

    def _recursion_deep_post_order(self, current_node: BSTNode, all_nodes: list[BSTNode]) -> list[BSTNode]:
        if current_node.LeftChild:
            self._recursion_deep_post_order(current_node=current_node.LeftChild, all_nodes=all_nodes)
        if current_node.RightChild:
            self._recursion_deep_post_order(current_node=current_node.RightChild, all_nodes=all_nodes)
        all_nodes.append(current_node)
        return all_nodes

    def _recursion_deep_pre_order(self, current_node: BSTNode, all_nodes: list[BSTNode]) -> list[BSTNode]:
        all_nodes.append(current_node)
        if current_node.LeftChild:
            self._recursion_deep_pre_order(current_node=current_node.LeftChild, all_nodes=all_nodes)
        if current_node.RightChild:
            self._recursion_deep_pre_order(current_node=current_node.RightChild, all_nodes=all_nodes)
        return all_nodes

    def DeepAllNodes(self, order: int) -> tuple[BSTNode | None]:
        if order not in [0, 1, 2]:
            assert False, "Не корректный параметр order"

        if self.Root is None:
            return tuple()

        if order == 0:
            return tuple(self._recursion_deep_in_order(current_node=self.Root, all_nodes=[]))
        if order == 1:
            return tuple(self._recursion_deep_post_order(current_node=self.Root, all_nodes=[]))
        if order == 2:
            return tuple(self._recursion_deep_pre_order(current_node=self.Root, all_nodes=[]))

    def _recursion_inversion_tree_pre_order(self, current_node: BSTNode):
        buffer = current_node.RightChild

        current_node.RightChild = current_node.LeftChild
        current_node.LeftChild = buffer

        if current_node.RightChild:
            self._recursion_inversion_tree_pre_order(current_node=current_node.RightChild)
        if current_node.LeftChild:
            self._recursion_inversion_tree_pre_order(current_node=current_node.LeftChild)

    def inversion_tree(self):
        """
        Задание: №3
        Номер задачи из задания: №3
        Краткое название: "Инвертировать бинарное дерево"
        Сложность: size - O(n) / time - O(n)

        Рефлексия:
            В своем решении естественно выбрал DFS.
            In order вариант быстро отбросил.
            Сам реализовал через pre-order, потому что казалось не существенным,
                в каком порядке двигаться.
            Когда продумывал конкретно свое решение с такой схемой -
                не выявил рисков из-за того, что родительские узлы перевернуты, а дочерние еще нет.
            Возможно проблемы с такой схемой начинаются при распараллеливании.
        """
        if self.Root is None:
            return
        self._recursion_inversion_tree_pre_order(current_node=self.Root)

    def _recursion_find_level_with_max_sum(self, parent_node: BSTNode, levels_sum: dict, level) -> dict:

        current_level_sum = 0

        if parent_node.LeftChild:
            current_level_sum += parent_node.LeftChild.NodeKey
        if parent_node.RightChild:
            current_level_sum += parent_node.RightChild.NodeKey

        levels_sum[level] = levels_sum.get(level, 0) + current_level_sum

        if parent_node.LeftChild:
            self._recursion_find_level_with_max_sum(parent_node=parent_node.LeftChild, levels_sum=levels_sum,
                                                    level=level + 1)
        if parent_node.RightChild:
            self._recursion_find_level_with_max_sum(parent_node=parent_node.RightChild, levels_sum=levels_sum,
                                                    level=level + 1)
        return levels_sum

    def find_max_level(self) -> int | None:
        """
        Задание: №3
        Номер задачи из задания: №4
        Краткое название: "Найти уровень в дереве, на котором сумма значений узлов максимальна"
        Сложность: size - O(n) / time - O(n)

        Рефлексия:
            Была идея переиспользовать метод обхода в ширину, но отказался от нее по двум причинам:
                А) Временная сложность вычисления сумм уровней для массива узлов остается такой же, как и при обходе в ширину.
                Б) Показалось, что в рамках обучения можно еще раз реализовать логику обхода в ширину с дополнительным условием.

            Конечно понимаю, что лучше переиспользовать существующий код чем дублировать новый.
        """
        if self.Root is None:
            return

        all_levels_and_sum = self._recursion_find_level_with_max_sum(parent_node=self.Root,
                                                                     levels_sum={0: self.Root.NodeKey},
                                                                     level=1)

        max_level = 0
        for level_num, level_sum in all_levels_and_sum.items():
            if all_levels_and_sum[max_level] < level_sum:
                max_level = level_num
        return max_level


def _build_tree(pref_list: list[int], inf_list: list[int]):
    if not pref_list or not inf_list:
        return None

    root_key = pref_list[0]
    root = BSTNode(key=root_key, val=None, parent=None)

    root_index = inf_list.index(root_key)

    left_inf = inf_list[:root_index]
    right_inf = inf_list[root_index + 1:]

    left_pref = pref_list[1:1 + len(left_inf)]
    right_pref = pref_list[1 + len(left_inf):]

    root.LeftChild = _build_tree(left_pref, left_inf)
    root.RightChild = _build_tree(right_pref, right_inf)
    return root


def restore_tree(prefix_list: list[int], infix_list: list[int]) -> BST:
    """
    Задание: №3
    Номер задачи из задания: №5
    Краткое название: "Функция для восстановления оригинального дерева"
    Сложность: size - O(n) / time - O(n)

    Рефлексия:
        В методе restore_tree реализовал логику восстановления BST дерева по двум массивам.
        Далее понял, что как будто бы можно восстановить BST дерево и по одному массиву, если это префиксный массив.
        Исходя из условия задания "Объясните, почему обязательно нужны оба обхода для однозначного построения дерева" -
            очень долго думал и искал варианты BST дерева, которое не удается однозначно восстановить по одному префиксному массиву.

        В итоге реализовал второй метод restore_tree_2, который восстанавливал дерево только по префиксному массиву,
            используя создание BST дерева и добавление узлов через стандартный интерфейс класса (AddKeyValue).
        Покрыл такую схему различными тестами (в файле test_4), пытаясь найти случай некорректного восстановления дерева.
        В итоге стал подозревать, что действительно для восстановления достаточно только одного префиксного массива.
        Случай, когда допустимы ключи с одинаковыми значениями не рассматривал.

        По итогу убедился, что действительно восстановление по одному массиву для дерева без повторяющихся узлов корректно работает.
    """
    if len(prefix_list) != len(infix_list):
        assert False, "Префиксный и инфиксный массив должны быть одинаковой длинны"

    if len(prefix_list) == 0 and len(infix_list) == 0:
        return BST(None)

    if not prefix_list or not infix_list:
        assert False, "Не корректные входные данные"

    return BST(_build_tree(prefix_list, infix_list))


def restore_tree_2(prefix_list: list[int], infix_list: list[int]) -> BST:
    """
    Задание: -
    Номер задачи из задания: -
    Краткое название: -
    Сложность: size - O(n) / time - O(n)

    Рефлексия:
    """
    if len(prefix_list) == 0:
        return BST(None
                   )
    copy_pref_list = prefix_list[:]

    root_key = copy_pref_list.pop(0)
    restoring_tree = BST(node=BSTNode(key=root_key, val=None, parent=None))

    for node_key in copy_pref_list:
        restoring_tree.AddKeyValue(key=node_key, val=None)

    return restoring_tree
