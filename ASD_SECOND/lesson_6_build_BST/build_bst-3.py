from ASD_SECOND.lesson_6_build_BST.build_bst import BalancedBST
from ASD_SECOND.lesson_6_build_BST.build_bst_2 import BalancedBST as BalancedBST_2


class TestGenBalanceTree:
    def test_gen_empty_tree(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[])
        assert not test_tree.Root

    def test_gen_one_el_tree(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[1])
        test_node = test_tree.Root
        assert test_node.NodeKey == 1
        assert not test_node.Parent
        assert not test_node.RightChild
        assert not test_node.LeftChild
        assert test_node.Level == 0

    def test_gen_three_el_tree(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[1, 3, 5])

        root_node = test_tree.Root

        assert not root_node.Parent
        assert root_node.NodeKey == 3

        assert root_node.LeftChild.NodeKey == 1
        assert root_node.LeftChild.Parent.NodeKey == 3

        assert root_node.RightChild.NodeKey == 5
        assert root_node.RightChild.Parent.NodeKey == 3

    def test_gen_three_el_tree_by_non_sort_list(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[5, 1, 3])

        root_node = test_tree.Root

        assert not root_node.Parent
        assert root_node.NodeKey == 3

        assert root_node.LeftChild.NodeKey == 1
        assert root_node.LeftChild.Parent.NodeKey == 3

        assert root_node.RightChild.NodeKey == 5
        assert root_node.RightChild.Parent.NodeKey == 3

    def test_gen_large_tree(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])

        root_node = test_tree.Root

        root_node.Level = 0
        root_node.NodeKey = 8

        root_node.LeftChild.Level = 1
        root_node.LeftChild.NodeKey = 4

        root_node.RightChild.Level = 1
        root_node.RightChild.NodeKey = 12

        root_node.RightChild.RightChild.Level = 2
        root_node.RightChild.RightChild.NodeKey = 14

        root_node.RightChild.LeftChild.Level = 2
        root_node.RightChild.LeftChild.NodeKey = 10

        root_node.LeftChild.RightChild.Level = 2
        root_node.LeftChild.RightChild.NodeKey = 6

        root_node.LeftChild.LeftChild.Level = 2
        root_node.LeftChild.LeftChild.NodeKey = 2

        root_node.RightChild.RightChild.RightChild.Level = 3
        root_node.RightChild.RightChild.RightChild.NodeKey = 15

        root_node.RightChild.RightChild.LeftChild.Level = 3
        root_node.RightChild.RightChild.LeftChild.NodeKey = 13

        root_node.RightChild.LeftChild.RightChild.Level = 3
        root_node.RightChild.LeftChild.RightChild.NodeKey = 11

        root_node.RightChild.LeftChild.LeftChild.Level = 3
        root_node.RightChild.LeftChild.LeftChild.NodeKey = 9

        root_node.LeftChild.RightChild.RightChild.Level = 3
        root_node.LeftChild.RightChild.RightChild.NodeKey = 7

        root_node.LeftChild.RightChild.LeftChild.Level = 3
        root_node.LeftChild.RightChild.LeftChild.NodeKey = 5

        root_node.LeftChild.LeftChild.RightChild.Level = 3
        root_node.LeftChild.LeftChild.RightChild.NodeKey = 3

        root_node.LeftChild.LeftChild.LeftChild.Level = 3
        root_node.LeftChild.LeftChild.LeftChild.NodeKey = 1


class TestIsCorrectTree:
    def test_correct_tree_simple_case(self) -> None:
        test_tree = BalancedBST_2()
        test_tree.GenerateTree(input_list=[1, 3, 5])

        assert test_tree.is_correct_tree()

    def test_correct_tree_negative_case_1(self) -> None:
        test_tree = BalancedBST_2()
        test_tree.GenerateTree(input_list=[1, 3, 5])

        test_tree.Root.LeftChild.NodeKey = 6
        assert not test_tree.is_correct_tree()

    def test_correct_tree_negative_case_2(self) -> None:
        test_tree = BalancedBST_2()
        test_tree.GenerateTree(input_list=[1, 3, 5])

        test_tree.Root.RightChild.NodeKey = -1
        assert not test_tree.is_correct_tree()

    def test_correct_tree_large_tree(self) -> None:
        test_tree = BalancedBST_2()
        test_tree.GenerateTree(input_list=[8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])

        assert test_tree.is_correct_tree()

    def test_correct_tree_large_tree_negative_case(self) -> None:
        test_tree = BalancedBST_2()
        test_tree.GenerateTree(input_list=[8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])

        test_tree.Root.RightChild.RightChild.RightChild.NodeKey = -3

        assert not test_tree.is_correct_tree()


class TestIsBalancedTree:
    def test_is_correct_tree_balance_empty_list(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[])

        assert test_tree.IsBalanced(root_node=test_tree.Root)

    def test_is_correct_tree_balance_one_node(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[5])

        assert test_tree.IsBalanced(root_node=test_tree.Root)

    def test_is_correct_tree_balance(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[1, 3, 5])

        assert test_tree.IsBalanced(root_node=test_tree.Root)

    def test_is_correct_non_balance_tree_1(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[4, 2, 6, 1, 3, 5, 7])

        test_tree.Root.LeftChild = None

        assert not test_tree.IsBalanced(root_node=test_tree.Root)

    def test_is_correct_non_balance_tree_2(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[4, 2, 6, 1, 3, 5, 7])

        test_tree.Root.RightChild = None

        assert not test_tree.IsBalanced(root_node=test_tree.Root)

    def test_is_correct_balance_tree_one_level_1(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[4, 2, 6, 1, 3, 5, 7])

        test_tree.Root.RightChild.RightChild = None
        test_tree.Root.RightChild.LeftChild = None

        assert test_tree.IsBalanced(root_node=test_tree.Root)

    def test_is_correct_balance_tree_one_level_2(self) -> None:
        test_tree = BalancedBST()
        test_tree.GenerateTree(input_list=[4, 2, 6, 1, 3, 5, 7])

        test_tree.Root.LeftChild.RightChild = None
        test_tree.Root.LeftChild.LeftChild = None

        assert test_tree.IsBalanced(root_node=test_tree.Root)