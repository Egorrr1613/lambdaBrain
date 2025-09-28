from ASD_SECOND.lesson_1_tree.tree import SimpleTree, SimpleTreeNode


def set_level_to_node(tree: SimpleTree):
    if tree.Count() == 0:
        return
    recursion_set_level(current_node=tree.Root, current_level=0)



def recursion_set_level(current_node: SimpleTreeNode, current_level: int):
    current_node.Level = current_level
    for child_node in current_node.Children:
        recursion_set_level(current_node=child_node, current_level=current_level+1)



def test_set_level_by_empty_tree():
    test_tree = SimpleTree(None)
    set_level_to_node(test_tree)
    assert test_tree.Root is None

def test_set_level():
    root_node = SimpleTreeNode(val=0, parent=None)
    test_tree = SimpleTree(root=root_node)

    test_tree.AddChild(
        parent_node=test_tree.Root, new_child=SimpleTreeNode(val=1, parent=None)
    )

    left_sub_node = SimpleTreeNode(val=2, parent=None)
    test_tree.AddChild(parent_node=test_tree.Root.Children[0], new_child=left_sub_node)

    right_branch_first_node = SimpleTreeNode(val=3, parent=None)
    test_tree.AddChild(parent_node=test_tree.Root, new_child=right_branch_first_node)

    right_branch_first_sub_node = SimpleTreeNode(val=4, parent=None)
    test_tree.AddChild(
        parent_node=right_branch_first_node, new_child=right_branch_first_sub_node
    )

    right_branch_second_sub_node = SimpleTreeNode(val=5, parent=None)
    test_tree.AddChild(
        parent_node=right_branch_first_node, new_child=right_branch_second_sub_node
    )

    test_tree.AddChild(
        parent_node=right_branch_first_sub_node,
        new_child=SimpleTreeNode(val=6, parent=None),
    )

    set_level_to_node(test_tree)
    assert test_tree.Root.Level == 0
    assert test_tree.Root.Children[0].Level == 1
    assert test_tree.Root.Children[1].Level == 1
    assert right_branch_first_sub_node.Level == 2
    assert right_branch_second_sub_node.Level == 2
    assert right_branch_first_sub_node.Children[0].Level == 3