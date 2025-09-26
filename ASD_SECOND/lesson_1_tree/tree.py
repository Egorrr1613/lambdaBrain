class SimpleTreeNode:

    def __init__(self, val, parent: "SimpleTreeNode | None"):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children: list = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root: SimpleTreeNode | None):
        self.Root: SimpleTreeNode | None = root
        self.count_node = 1 if type(root) is SimpleTreeNode else 0

    def AddChild(self, parent_node: SimpleTreeNode | None, new_child: SimpleTreeNode):
        if self.Root is None and parent_node is None:
            new_child.Parent = None
            self.Root = new_child
            self.count_node += 1
            return
        if self.Root is None or parent_node is None:
            return
        parent_node.Children.append(new_child)
        new_child.Parent = parent_node
        self.count_node += 1

    def DeleteNode(self, node_to_delete: SimpleTreeNode):
        if node_to_delete is self.Root:
            return
        if node_to_delete.Parent is None:
            return
        try:
            child_index_in_parent = node_to_delete.Parent.Children.index(node_to_delete)
        except ValueError:
            return
        node_to_delete.Parent.Children.pop(child_index_in_parent)
        node_to_delete.Parent = None
        self.count_node -= 1

    def GetAllNodes(self) -> list[SimpleTreeNode]:
        if self.Count() == 0 or self.Root is None:
            return []
        if self.Count() == 1:
            return [self.Root]
        result = self._recursion_get_all_node(
            all_find_nodes=[self.Root], node_children_check=self.Root
        )
        return result

    def _recursion_get_all_node(
        self, all_find_nodes, node_children_check: SimpleTreeNode
    ) -> list:
        if len(node_children_check.Children) == 0:
            return []
        children_nodes = []
        for child_node in node_children_check.Children:
            children_nodes.append(child_node)
            children_nodes += self._recursion_get_all_node(
                all_find_nodes=[], node_children_check=child_node
            )
        return all_find_nodes + children_nodes

    def FindNodesByValue(self, val):
        if self.Count() == 0:
            return []
        result_nodes = []
        return self._recursion_find_nodes(
            collected_nodes=result_nodes, node_to_check=self.Root, find_val=val
        )

    def _recursion_find_nodes(self, collected_nodes, node_to_check, find_val) -> list:
        if node_to_check.NodeValue == find_val:
            collected_nodes.append(node_to_check)
        for sub_node in node_to_check.Children:
            self._recursion_find_nodes(
                collected_nodes=collected_nodes,
                node_to_check=sub_node,
                find_val=find_val,
            )
        return collected_nodes

    def MoveNode(self, original_node: SimpleTreeNode, new_parent: SimpleTreeNode):
        if type(original_node.Parent) is SimpleTreeNode:
            try:
                child_index_in_parent = original_node.Parent.Children.index(
                    original_node
                )
            except ValueError:
                return
            original_node.Parent.Children.pop(child_index_in_parent)

        original_node.Parent = new_parent
        new_parent.Children.append(original_node)

    def Count(self):
        return self.count_node

    def LeafCount(self):
        if self.Root is None:
            return 0
        if self.Count() == 1:
            return 1
        return self._recursion_leaf_count(current_node=self.Root)

    def _recursion_leaf_count(self, current_node: SimpleTreeNode) -> int:
        if len(current_node.Children) == 0:
            return 1
        result = 0
        for check_node in current_node.Children:
            result += self._recursion_leaf_count(check_node)
        return result

