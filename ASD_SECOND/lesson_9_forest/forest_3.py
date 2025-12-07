from ASD_SECOND.lesson_9_forest.forest import SimpleTree, SimpleTreeNode
from ASD_SECOND.lesson_9_forest.forest_2 import SimpleTree as SimpleTree2
from ASD_SECOND.lesson_9_forest.forest_2 import SimpleTreeNode as SimpleTreeNode2


class TestGetCountChildNode:
    def test_get_count_child_nodes(self) -> None:
        root_node = SimpleTreeNode(val=0, parent=None)
        test_tree = SimpleTree(root=root_node)

        test_tree.AddChild(
            parent_node=test_tree.Root,
            new_child=SimpleTreeNode(val=1, parent=None)
        )
        test_tree.AddChild(
            parent_node=test_tree.Root.Children[0],
            new_child=SimpleTreeNode(val=2, parent=None),
        )

        assert test_tree.Count() == 3
        assert test_tree.get_count_child_nodes(main_node=root_node.Children[0], child_count=0) == 1
        assert test_tree.get_count_child_nodes(main_node=root_node, child_count=0) == 2

        test_tree.AddChild(
            parent_node=test_tree.Root.Children[0].Children[0],
            new_child=SimpleTreeNode(val=3, parent=None),
        )
        assert test_tree.get_count_child_nodes(main_node=root_node, child_count=0) == 3
        assert test_tree.Count() == 4

        test_tree.AddChild(
            parent_node=test_tree.Root.Children[0],
            new_child=SimpleTreeNode(val=4, parent=None),
        )
        assert test_tree.get_count_child_nodes(main_node=root_node, child_count=0) == 4


class TestGetBreakList:

    def test_forest_base_case(self) -> None:
        root_node = SimpleTreeNode(val=1, parent=None)
        test_tree = SimpleTree(root=root_node)

        test_tree.AddChild(
            parent_node=test_tree.Root,
            new_child=SimpleTreeNode(val=2, parent=None)
        )

        test_tree.AddChild(
            parent_node=test_tree.Root,
            new_child=SimpleTreeNode(val=3, parent=None)
        )

        test_tree.AddChild(
            parent_node=test_tree.Root,
            new_child=SimpleTreeNode(val=4, parent=None)
        )

        node_val_2 = test_tree.FindNodesByValue(2)[0]

        test_tree.AddChild(
            parent_node=node_val_2,
            new_child=SimpleTreeNode(val=5, parent=None)
        )
        test_tree.AddChild(
            parent_node=node_val_2,
            new_child=SimpleTreeNode(val=6, parent=None)
        )


class TestEvenTrees:
    def test_base_case(self) -> None:
        root_node = SimpleTreeNode(val=1, parent=None)
        test_tree = SimpleTree(root=root_node)

        assert test_tree.EvenTrees() == []

    def test_two_nodes(self) -> None:
        root_node = SimpleTreeNode(val=1, parent=None)
        test_tree = SimpleTree(root=root_node)
        test_tree.AddChild(
            parent_node=test_tree.Root,
            new_child=SimpleTreeNode(val=2, parent=None)
        )

        assert test_tree.EvenTrees() == []

    def test_three_nodes(self) -> None:
        root_node = SimpleTreeNode(val=1, parent=None)
        test_tree = SimpleTree(root=root_node)
        test_tree.AddChild(
            parent_node=test_tree.Root,
            new_child=SimpleTreeNode(val=2, parent=None)
        )
        test_tree.AddChild(
            parent_node=test_tree.Root,
            new_child=SimpleTreeNode(val=3, parent=None)
        )

        assert test_tree.EvenTrees() == []

        root_node = SimpleTreeNode(val=1, parent=None)
        test_tree = SimpleTree(root=root_node)
        test_tree.AddChild(
            parent_node=test_tree.Root,
            new_child=SimpleTreeNode(val=2, parent=None)
        )
        test_tree.AddChild(
            parent_node=test_tree.Root.Children[0],
            new_child=SimpleTreeNode(val=3, parent=None)
        )
        assert test_tree.EvenTrees() == []

    def test_four_nodes_line_tree(self) -> None:
        root_node = SimpleTreeNode(val=1, parent=None)
        test_tree = SimpleTree(root=root_node)

        second_node = SimpleTreeNode(val=2, parent=None)
        test_tree.AddChild(
            parent_node=root_node,
            new_child=second_node
        )

        third_node = SimpleTreeNode(val=3, parent=None)
        test_tree.AddChild(
            parent_node=second_node,
            new_child=third_node
        )

        fourth_node = SimpleTreeNode(val=4, parent=None)
        test_tree.AddChild(
            parent_node=third_node,
            new_child=fourth_node
        )

        assert test_tree.EvenTrees() == [second_node, third_node]

    def test_simple_breaks_list(self) -> None:
        first_node = SimpleTreeNode(val=1, parent=None)
        test_tree = SimpleTree(root=first_node)

        second_node = SimpleTreeNode(val=2, parent=None)
        test_tree.AddChild(
            parent_node=first_node,
            new_child=second_node
        )

        third_node = SimpleTreeNode(val=3, parent=None)
        test_tree.AddChild(
            parent_node=first_node,
            new_child=third_node
        )

        fourth_node = SimpleTreeNode(val=4, parent=None)
        test_tree.AddChild(
            parent_node=third_node,
            new_child=fourth_node
        )

        assert test_tree.EvenTrees() == [first_node, third_node]

    def test_hard_breaks_list(self) -> None:
        first_node = SimpleTreeNode(val=1, parent=None)
        test_tree = SimpleTree(root=first_node)

        second_node = SimpleTreeNode(val=2, parent=None)
        test_tree.AddChild(
            parent_node=first_node,
            new_child=second_node
        )

        third_node = SimpleTreeNode(val=3, parent=None)
        test_tree.AddChild(
            parent_node=first_node,
            new_child=third_node
        )

        fourth_node = SimpleTreeNode(val=4, parent=None)
        test_tree.AddChild(
            parent_node=first_node,
            new_child=fourth_node
        )

        fifth_node = SimpleTreeNode(val=5, parent=None)
        test_tree.AddChild(
            parent_node=second_node,
            new_child=fifth_node
        )

        sixth_node = SimpleTreeNode(val=6, parent=None)
        test_tree.AddChild(
            parent_node=second_node,
            new_child=sixth_node
        )

        seventh_node = SimpleTreeNode(val=7, parent=None)
        test_tree.AddChild(
            parent_node=third_node,
            new_child=seventh_node
        )

        eighth_node = SimpleTreeNode(val=8, parent=None)
        test_tree.AddChild(
            parent_node=fourth_node,
            new_child=eighth_node
        )

        ninth_node = SimpleTreeNode(val=9, parent=None)
        test_tree.AddChild(
            parent_node=eighth_node,
            new_child=ninth_node
        )

        tenth_node = SimpleTreeNode(val=10, parent=None)
        test_tree.AddChild(
            parent_node=eighth_node,
            new_child=tenth_node
        )

        assert test_tree.EvenTrees() == [first_node, third_node, first_node, fourth_node]


class TestBalanceTree:
    def test_base_case(self) -> None:
        first_node = SimpleTreeNode2(val=1, parent=None)
        test_tree = SimpleTree2(root=first_node)

        second_node = SimpleTreeNode2(val=2, parent=None)
        test_tree.AddChild(
            parent_node=first_node,
            new_child=second_node
        )

        third_node = SimpleTreeNode2(val=3, parent=None)
        test_tree.AddChild(
            parent_node=second_node,
            new_child=third_node
        )

        fourth_node = SimpleTreeNode2(val=4, parent=None)
        test_tree.AddChild(
            parent_node=third_node,
            new_child=fourth_node
        )

        test_tree.balance_tree()
        assert first_node.Children == [second_node, third_node]
        assert second_node.Children == [fourth_node]


class TestGetSubTreeCount:
    def test_base_case(self) -> None:
        first_node = SimpleTreeNode2(val=1, parent=None)
        test_tree = SimpleTree2(root=first_node)

        second_node = SimpleTreeNode2(val=2, parent=None)
        test_tree.AddChild(
            parent_node=first_node,
            new_child=second_node
        )

        third_node = SimpleTreeNode2(val=3, parent=None)
        test_tree.AddChild(
            parent_node=second_node,
            new_child=third_node
        )

        fourth_node = SimpleTreeNode2(val=4, parent=None)
        test_tree.AddChild(
            parent_node=second_node,
            new_child=fourth_node
        )

        assert test_tree.get_sub_tree_count(find_subtree_node=second_node) == 0

        five_node = SimpleTreeNode2(val=5, parent=None)
        test_tree.AddChild(
            parent_node=fourth_node,
            new_child=five_node
        )

        assert test_tree.get_sub_tree_count(find_subtree_node=second_node) == 1
