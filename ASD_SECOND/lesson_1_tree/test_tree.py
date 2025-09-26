from ASD_SECOND.lesson_1_tree.tree import SimpleTree, SimpleTreeNode


def test_tree_create_and_add_root_node():
    test_tree = SimpleTree(None)
    assert test_tree.Root is None
    test_tree.AddChild(parent_node=SimpleTreeNode(val=99, parent=None), new_child=SimpleTreeNode(val=5, parent=None))
    assert test_tree.Root is None
    assert test_tree.Count() == 0

    test_tree.AddChild(parent_node=None, new_child=SimpleTreeNode(val=5, parent=None))
    assert type(test_tree.Root) is SimpleTreeNode
    assert test_tree.Root.NodeValue == 5
    assert len(test_tree.Root.Children) == 0
    assert test_tree.Count() == 1


def test_add_node():
    test_tree = SimpleTree(root=SimpleTreeNode(val=0, parent=None))
    assert test_tree.Count() == 1

    test_tree.AddChild(parent_node=test_tree.Root, new_child=SimpleTreeNode(val=1, parent=None))
    assert len(test_tree.Root.Children) == 1
    assert test_tree.Root.NodeValue == 0
    assert test_tree.Root.Children[0].NodeValue == 1
    assert test_tree.Root.Children[0].Parent == test_tree.Root
    assert test_tree.Count() == 2

    """Некорректное добавление узла в дерево"""
    test_tree.AddChild(parent_node=None, new_child=SimpleTreeNode(val=2, parent=None))
    assert len(test_tree.Root.Children) == 1
    assert test_tree.Count() == 2


def test_delete_node():
    root_node = SimpleTreeNode(val=0, parent=None)
    test_tree = SimpleTree(root=root_node)

    test_tree.AddChild(parent_node=test_tree.Root, new_child=SimpleTreeNode(val=1, parent=None))
    test_tree.AddChild(parent_node=test_tree.Root.Children[0], new_child=SimpleTreeNode(val=2, parent=None))
    assert len(test_tree.Root.Children) == 1
    assert len(test_tree.Root.Children[0].Children) == 1
    assert test_tree.Count() == 3

    test_tree.DeleteNode(test_tree.Root.Children[0].Children[0])
    assert len(test_tree.Root.Children) == 1
    assert len(test_tree.Root.Children[0].Children) == 0
    assert test_tree.Count() == 2

    test_tree.DeleteNode(test_tree.Root.Children[0])
    assert len(test_tree.Root.Children) == 0
    assert test_tree.Count() == 1

    test_tree.DeleteNode(test_tree.Root)
    assert test_tree.Root is root_node
    assert test_tree.Count() == 1


def test_get_all_nodes_list():
    root_node = SimpleTreeNode(val=0, parent=None)
    test_tree = SimpleTree(root=root_node)
    assert test_tree.GetAllNodes() == [root_node]

    test_tree.AddChild(parent_node=test_tree.Root, new_child=SimpleTreeNode(val=1, parent=None))
    test_tree.AddChild(parent_node=test_tree.Root.Children[0], new_child=SimpleTreeNode(val=2, parent=None))
    all_nodes = test_tree.GetAllNodes()
    assert len(all_nodes) == 3
    assert root_node in all_nodes
    assert root_node.Children[0] in all_nodes
    assert root_node.Children[0].Children[0] in all_nodes

    right_branch_first_node = SimpleTreeNode(val=3, parent=None)
    test_tree.AddChild(parent_node=test_tree.Root, new_child=right_branch_first_node)
    all_nodes = test_tree.GetAllNodes()
    assert len(all_nodes) == 4
    assert root_node in all_nodes
    assert root_node.Children[0] in all_nodes
    assert root_node.Children[1] in all_nodes
    assert root_node.Children[0].Children[0] in all_nodes

    right_branch_first_sub_node = SimpleTreeNode(val=4, parent=None)
    right_branch_second_sub_node = SimpleTreeNode(val=5, parent=None)
    test_tree.AddChild(parent_node=right_branch_first_node, new_child=right_branch_first_sub_node)
    test_tree.AddChild(parent_node=right_branch_first_node, new_child=right_branch_second_sub_node)
    all_nodes = test_tree.GetAllNodes()
    assert len(all_nodes) == 6
    assert root_node in all_nodes
    assert root_node.Children[0] in all_nodes
    assert root_node.Children[1] in all_nodes
    assert right_branch_first_node in all_nodes
    assert right_branch_first_sub_node in all_nodes
    assert right_branch_second_sub_node in all_nodes


def test_find_nodes():
    root_node = SimpleTreeNode(val=0, parent=None)
    test_tree = SimpleTree(root=root_node)
    assert test_tree.FindNodesByValue(99) == []

    test_tree.AddChild(parent_node=test_tree.Root, new_child=SimpleTreeNode(val=1, parent=None))
    test_tree.AddChild(parent_node=test_tree.Root.Children[0], new_child=SimpleTreeNode(val=2, parent=None))

    right_branch_first_node = SimpleTreeNode(val=3, parent=None)
    test_tree.AddChild(parent_node=test_tree.Root, new_child=right_branch_first_node)

    right_branch_first_sub_node = SimpleTreeNode(val=4, parent=None)
    test_tree.AddChild(parent_node=right_branch_first_node, new_child=right_branch_first_sub_node)

    right_branch_second_sub_node = SimpleTreeNode(val=5, parent=None)
    test_tree.AddChild(parent_node=right_branch_first_node, new_child=right_branch_second_sub_node)

    assert test_tree.FindNodesByValue(4) == [right_branch_first_sub_node]
    assert test_tree.FindNodesByValue(99) == []

    node_to_find = SimpleTreeNode(val=4, parent=None)
    test_tree.AddChild(parent_node=right_branch_first_sub_node, new_child=node_to_find)

    assert test_tree.FindNodesByValue(4) == [right_branch_first_sub_node, node_to_find]
    assert test_tree.FindNodesByValue(0) == [root_node]
    assert test_tree.FindNodesByValue(3) == [right_branch_first_node]


def test_move_node():
    root_node = SimpleTreeNode(val=0, parent=None)
    test_tree = SimpleTree(root=root_node)

    test_tree.AddChild(parent_node=test_tree.Root, new_child=SimpleTreeNode(val=1, parent=None))

    left_sub_node = SimpleTreeNode(val=2, parent=None)
    test_tree.AddChild(parent_node=test_tree.Root.Children[0], new_child=left_sub_node)

    right_branch_first_node = SimpleTreeNode(val=3, parent=None)
    test_tree.AddChild(parent_node=test_tree.Root, new_child=right_branch_first_node)

    right_branch_first_sub_node = SimpleTreeNode(val=4, parent=None)
    test_tree.AddChild(parent_node=right_branch_first_node, new_child=right_branch_first_sub_node)

    right_branch_second_sub_node = SimpleTreeNode(val=5, parent=None)
    test_tree.AddChild(parent_node=right_branch_first_node, new_child=right_branch_second_sub_node)

    test_tree.AddChild(parent_node=right_branch_first_sub_node, new_child=SimpleTreeNode(val=6, parent=None))

    test_tree.MoveNode(original_node=right_branch_first_node, new_parent=left_sub_node)

    assert len(left_sub_node.Children) == 1
    assert left_sub_node.Children[0] is right_branch_first_node
    assert left_sub_node.Children[0].NodeValue == 3
    assert len(left_sub_node.Children[0].Children) == 2


def test_leaf_count():
    root_node = SimpleTreeNode(val=0, parent=None)
    test_tree = SimpleTree(root=root_node)

    test_tree.AddChild(parent_node=test_tree.Root, new_child=SimpleTreeNode(val=1, parent=None))

    left_sub_node = SimpleTreeNode(val=2, parent=None)
    test_tree.AddChild(parent_node=test_tree.Root.Children[0], new_child=left_sub_node)

    right_branch_first_node = SimpleTreeNode(val=3, parent=None)
    test_tree.AddChild(parent_node=test_tree.Root, new_child=right_branch_first_node)

    right_branch_first_sub_node = SimpleTreeNode(val=4, parent=None)
    test_tree.AddChild(parent_node=right_branch_first_node, new_child=right_branch_first_sub_node)

    right_branch_second_sub_node = SimpleTreeNode(val=5, parent=None)
    test_tree.AddChild(parent_node=right_branch_first_node, new_child=right_branch_second_sub_node)

    test_tree.AddChild(parent_node=right_branch_first_sub_node, new_child=SimpleTreeNode(val=6, parent=None))

    assert test_tree.LeafCount() == 3

    test_tree.MoveNode(original_node=right_branch_first_node, new_parent=left_sub_node)
    assert test_tree.LeafCount() == 2
