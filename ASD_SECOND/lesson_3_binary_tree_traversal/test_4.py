from ASD_SECOND.lesson_3_binary_tree_traversal.traversal_BST_2 import BST as BST_2, BSTNode as BSTNode_2, restore_tree, \
    restore_tree_2


class TestRestoreTree:

    def test_restore_tree_2(self):
        prefix_list = [10, 5, 3, 6, 20, 11, 25]
        infix_list = [3, 5, 6, 10, 11, 20, 25]
        test_tree = restore_tree_2(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 10

        assert test_tree.Root.LeftChild.NodeKey == 5
        assert test_tree.Root.LeftChild.LeftChild.NodeKey == 3
        assert test_tree.Root.LeftChild.RightChild.NodeKey == 6

        assert test_tree.Root.RightChild.NodeKey == 20
        assert test_tree.Root.RightChild.LeftChild.NodeKey == 11
        assert test_tree.Root.RightChild.RightChild.NodeKey == 25

    def test_restore_simple_tree(self):
        prefix_list = [10, 5, 15]
        infix_list = [5, 10, 15]

        test_tree = restore_tree_2(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.RightChild.NodeKey == 15
        assert test_tree.Root.LeftChild.NodeKey == 5

    def test_restore_right_list(self):
        prefix_list = [10, 15, 25, 30]
        infix_list = [10, 15, 25, 30]

        test_tree = restore_tree_2(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.RightChild.NodeKey == 15
        assert test_tree.Root.RightChild.RightChild.NodeKey == 25
        assert test_tree.Root.RightChild.RightChild.RightChild.NodeKey == 30

    def test_restore_left_list(self):
        prefix_list = [10, 5, 0, -5]
        infix_list = [-5, 0, 5, 10]

        test_tree = restore_tree_2(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.LeftChild.NodeKey == 5
        assert test_tree.Root.LeftChild.LeftChild.NodeKey == 0
        assert test_tree.Root.LeftChild.LeftChild.LeftChild.NodeKey == -5

    def test_restore_one_element_tree(self):
        prefix_list = [10]
        infix_list = [10]

        test_tree = restore_tree_2(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.LeftChild is None
        assert test_tree.Root.RightChild is None

    def test_restore_empty_tree(self):
        prefix_list = []
        infix_list = []

        test_tree = restore_tree_2(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root is None

    def test_restore_tree_negative(self):
        prefix_list = [0, -5, -2, 10, 15]
        infix_list = [-5, -2, 0, 10, 15]

        test_tree = restore_tree_2(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 0

        assert test_tree.Root.LeftChild.NodeKey == -5
        assert test_tree.Root.LeftChild.RightChild.NodeKey == -2

        assert test_tree.Root.RightChild.NodeKey == 10
        assert test_tree.Root.RightChild.RightChild.NodeKey == 15