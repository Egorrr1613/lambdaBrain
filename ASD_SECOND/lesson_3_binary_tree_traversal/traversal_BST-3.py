from ASD_SECOND.lesson_3_binary_tree_traversal.traversal_BST import BST, BSTNode
from ASD_SECOND.lesson_3_binary_tree_traversal.traversal_BST_2 import BST as BST_2, BSTNode as BSTNode_2, restore_tree


class TestDeepSearchInEmptyTree:

    def test_deep_search_empty_tree(self):
        test_tree = BST(None)
        assert test_tree.DeepAllNodes(0) == tuple()
        assert test_tree.DeepAllNodes(1) == tuple()
        assert test_tree.DeepAllNodes(2) == tuple()


class TestInOrderDeepSearch:

    def test_deep_search_one_node(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        assert test_tree.DeepAllNodes(0) == (init_node,)

    def test_deep_search_two_left_node_in_order(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=9, val="b")

        all_nodes = test_tree.DeepAllNodes(order=0)

        assert all_nodes[0].NodeKey == 9
        assert all_nodes[1].NodeKey == 10

    def test_deep_search_two_right_node_in_order(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=11, val="b")

        all_nodes = test_tree.DeepAllNodes(order=0)

        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 11

    def test_deep_search_left_right_nodes_in_order(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=8, val="b")

        all_nodes = test_tree.DeepAllNodes(order=0)

        assert all_nodes[0].NodeKey == 5
        assert all_nodes[1].NodeKey == 8
        assert all_nodes[2].NodeKey == 10

    def test_deep_search_random_nodes_in_order(self):
        test_tree = BST(BSTNode(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=8, val="b")
        test_tree.AddKeyValue(key=3, val="c")
        test_tree.AddKeyValue(key=1, val="c")
        test_tree.AddKeyValue(key=2, val="c")
        test_tree.AddKeyValue(key=7, val="c")
        test_tree.AddKeyValue(key=9, val="c")

        all_nodes = test_tree.DeepAllNodes(order=0)
        assert len(all_nodes) == 8
        assert all_nodes[0].NodeKey == 1
        assert all_nodes[1].NodeKey == 2
        assert all_nodes[2].NodeKey == 3
        assert all_nodes[3].NodeKey == 5
        assert all_nodes[4].NodeKey == 7
        assert all_nodes[5].NodeKey == 8
        assert all_nodes[6].NodeKey == 9
        assert all_nodes[7].NodeKey == 10


class TestPostOrderDeepSearch:

    def test_deep_search_empty_tree_post_order(self):
        test_tree = BST(None)
        assert test_tree.DeepAllNodes(order=1) == tuple()

    def test_deep_search_one_node_post_order(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        assert test_tree.DeepAllNodes(1) == (init_node,)

    def test_deep_search_two_left_node_post_order(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=5, val="b")

        all_nodes = test_tree.DeepAllNodes(order=1)

        assert all_nodes[0].NodeKey == 5
        assert all_nodes[1].NodeKey == 10

    def test_deep_search_two_right_node_post_order(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=11, val="b")

        all_nodes = test_tree.DeepAllNodes(order=1)

        assert all_nodes[0].NodeKey == 11
        assert all_nodes[1].NodeKey == 10

    def test_deep_search_left_right_nodes_post_order(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=8, val="b")

        all_nodes = test_tree.DeepAllNodes(order=1)

        assert all_nodes[0].NodeKey == 8
        assert all_nodes[1].NodeKey == 5
        assert all_nodes[2].NodeKey == 10

    def test_deep_search_random_nodes_post_order(self):
        test_tree = BST(BSTNode(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=8, val="b")
        test_tree.AddKeyValue(key=3, val="c")
        test_tree.AddKeyValue(key=1, val="c")
        test_tree.AddKeyValue(key=2, val="c")
        test_tree.AddKeyValue(key=7, val="c")
        test_tree.AddKeyValue(key=9, val="c")

        all_nodes = test_tree.DeepAllNodes(order=1)
        assert len(all_nodes) == 8
        assert all_nodes[0].NodeKey == 2
        assert all_nodes[1].NodeKey == 1
        assert all_nodes[2].NodeKey == 3
        assert all_nodes[3].NodeKey == 7
        assert all_nodes[4].NodeKey == 9
        assert all_nodes[5].NodeKey == 8
        assert all_nodes[6].NodeKey == 5
        assert all_nodes[7].NodeKey == 10


class TestPreOrderDeepSearch:

    def test_deep_search_empty_tree_pre_order(self):
        test_tree = BST(None)
        assert test_tree.DeepAllNodes(2) == tuple()

    def test_deep_search_one_node_pre_order(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        assert test_tree.DeepAllNodes(2) == (init_node,)

    def test_deep_search_two_left_node(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=5, val="b")

        all_nodes = test_tree.DeepAllNodes(order=2)

        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 5

    def test_deep_search_two_right_node(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=11, val="b")

        all_nodes = test_tree.DeepAllNodes(order=2)

        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 11

    def test_deep_search_left_right_nodes(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=8, val="b")

        all_nodes = test_tree.DeepAllNodes(order=2)

        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 5
        assert all_nodes[2].NodeKey == 8

    def test_deep_search_random_nodes(self):
        test_tree = BST(BSTNode(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=8, val="b")
        test_tree.AddKeyValue(key=3, val="c")
        test_tree.AddKeyValue(key=1, val="c")
        test_tree.AddKeyValue(key=2, val="c")
        test_tree.AddKeyValue(key=7, val="c")
        test_tree.AddKeyValue(key=9, val="c")

        all_nodes = test_tree.DeepAllNodes(order=2)
        assert len(all_nodes) == 8
        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 5
        assert all_nodes[2].NodeKey == 3
        assert all_nodes[3].NodeKey == 1
        assert all_nodes[4].NodeKey == 2
        assert all_nodes[5].NodeKey == 8
        assert all_nodes[6].NodeKey == 7
        assert all_nodes[7].NodeKey == 9


class TestWideSearch:
    def test_wide_search_empty_tree(self):
        test_tree = BST(None)
        assert test_tree.WideAllNodes() == tuple()

    def test_wide_search_one_node(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        assert test_tree.WideAllNodes() == (init_node,)

    def test_wide_search_two_left_node(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=9, val="b")

        all_nodes = test_tree.WideAllNodes()
        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 9

    def test_wide_search_two_right_node(self):
        init_node = BSTNode(key=10, val="a", parent=None)
        test_tree = BST(init_node)
        test_tree.AddKeyValue(key=11, val="b")

        all_nodes = test_tree.WideAllNodes()
        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 11

    def test_wide_search_three_node(self):
        test_tree = BST(BSTNode(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=11, val="b")

        all_nodes = test_tree.WideAllNodes()
        assert len(all_nodes) == 3
        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 5
        assert all_nodes[2].NodeKey == 11

    def test_wide_search_seven_node(sefl):
        test_tree = BST(BSTNode(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=20, val="b")
        test_tree.AddKeyValue(key=3, val="b")
        test_tree.AddKeyValue(key=6, val="b")
        test_tree.AddKeyValue(key=11, val="b")
        test_tree.AddKeyValue(key=25, val="b")

        all_nodes = test_tree.WideAllNodes()
        assert len(all_nodes) == 7
        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 5
        assert all_nodes[2].NodeKey == 20
        assert all_nodes[3].NodeKey == 3
        assert all_nodes[4].NodeKey == 6
        assert all_nodes[5].NodeKey == 11
        assert all_nodes[6].NodeKey == 25

    def test_wide_search_random_nodes(self):
        test_tree = BST(BSTNode(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=8, val="b")
        test_tree.AddKeyValue(key=3, val="c")
        test_tree.AddKeyValue(key=1, val="c")
        test_tree.AddKeyValue(key=2, val="c")
        test_tree.AddKeyValue(key=7, val="c")
        test_tree.AddKeyValue(key=9, val="c")

        all_nodes = test_tree.WideAllNodes()
        assert len(all_nodes) == 8
        assert all_nodes[0].NodeKey == 10
        assert all_nodes[1].NodeKey == 5
        assert all_nodes[2].NodeKey == 3
        assert all_nodes[3].NodeKey == 8
        assert all_nodes[4].NodeKey == 1
        assert all_nodes[5].NodeKey == 7
        assert all_nodes[6].NodeKey == 9
        assert all_nodes[7].NodeKey == 2


class TestInvertTree:

    def test_invert_tree_empty_tree(self):
        test_tree = BST_2(None)
        test_tree.inversion_tree()

        assert test_tree.Root is None

    def test_invert_tree(self):
        test_tree = BST_2(BSTNode_2(key=10, val="a", parent=None))
        test_tree.inversion_tree()

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.LeftChild is None
        assert test_tree.Root.RightChild is None

    def test_invert_tree_simple_tree(self):
        test_tree = BST_2(BSTNode_2(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=15, val="b")
        test_tree.inversion_tree()

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.LeftChild.NodeKey == 15
        assert test_tree.Root.RightChild.NodeKey == 5

        assert test_tree.Root.LeftChild.LeftChild is None
        assert test_tree.Root.LeftChild.RightChild is None

        assert test_tree.Root.RightChild.LeftChild is None
        assert test_tree.Root.RightChild.RightChild is None

    def test_inversion_tree(self):
        test_tree = BST_2(BSTNode_2(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=8, val="b")
        test_tree.AddKeyValue(key=3, val="c")
        test_tree.AddKeyValue(key=1, val="c")
        test_tree.AddKeyValue(key=2, val="c")
        test_tree.AddKeyValue(key=7, val="c")
        test_tree.AddKeyValue(key=9, val="c")

        test_tree.inversion_tree()

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.LeftChild is None
        assert test_tree.Root.RightChild.NodeKey == 5

        assert test_tree.Root.RightChild.LeftChild.NodeKey == 8
        assert test_tree.Root.RightChild.RightChild.NodeKey == 3

        assert test_tree.Root.RightChild.RightChild.LeftChild is None
        assert test_tree.Root.RightChild.RightChild.RightChild.NodeKey == 1

        assert test_tree.Root.RightChild.RightChild.RightChild.LeftChild.NodeKey == 2
        assert test_tree.Root.RightChild.RightChild.RightChild.RightChild is None

        assert test_tree.Root.RightChild.LeftChild.RightChild.NodeKey == 7
        assert test_tree.Root.RightChild.LeftChild.LeftChild.NodeKey == 9


class TestFindMaxLeveL:

    def test_find_max_level_empty_tree(self):
        test_tree = BST_2(None)
        assert test_tree.find_max_level() is None

    def test_find_max_level_root_node(self):
        test_tree = BST_2(BSTNode_2(key=10, val="a", parent=None))
        assert test_tree.find_max_level() == 0

    def test_find_max_level_one_left_node(self):
        test_tree = BST_2(BSTNode_2(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")

        assert test_tree.find_max_level() == 0

    def test_find_max_level_one_right_node(self):
        test_tree = BST_2(BSTNode_2(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=51, val="b")

        assert test_tree.find_max_level() == 1

    def test_find_max_level_two_node(self):
        test_tree = BST_2(BSTNode_2(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=51, val="b")
        test_tree.AddKeyValue(key=1, val="b")

        assert test_tree.find_max_level() == 1

    def test_find_max_level(self):
        test_tree = BST_2(BSTNode_2(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=8, val="b")
        test_tree.AddKeyValue(key=3, val="c")
        test_tree.AddKeyValue(key=1, val="c")
        test_tree.AddKeyValue(key=2, val="c")
        test_tree.AddKeyValue(key=7, val="c")
        test_tree.AddKeyValue(key=9, val="c")
        test_tree.AddKeyValue(key=11, val="c")

        assert test_tree.find_max_level() == 3

    def test_find_max_level_2(self):
        test_tree = BST_2(BSTNode_2(key=10, val="a", parent=None))
        test_tree.AddKeyValue(key=5, val="b")
        test_tree.AddKeyValue(key=3, val="b")
        test_tree.AddKeyValue(key=6, val="c")
        test_tree.AddKeyValue(key=20, val="c")
        test_tree.AddKeyValue(key=11, val="c")
        test_tree.AddKeyValue(key=25, val="c")

        assert test_tree.find_max_level() == 2


class TestRestoreTree:

    def test_restore_tree(self):
        prefix_list = [10, 5, 3, 6, 20, 11, 25]
        infix_list = [3, 5, 6, 10, 11, 20, 25]
        test_tree = restore_tree(prefix_list=prefix_list, infix_list=infix_list)

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

        test_tree = restore_tree(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.RightChild.NodeKey == 15
        assert test_tree.Root.LeftChild.NodeKey == 5

    def test_restore_right_list(self):
        prefix_list = [10, 15, 25, 30]
        infix_list = [10, 15, 25, 30]

        test_tree = restore_tree(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.RightChild.NodeKey == 15
        assert test_tree.Root.RightChild.RightChild.NodeKey == 25
        assert test_tree.Root.RightChild.RightChild.RightChild.NodeKey == 30

    def test_restore_left_list(self):
        prefix_list = [10, 5, 0, -5]
        infix_list = [-5, 0, 5, 10]

        test_tree = restore_tree(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.LeftChild.NodeKey == 5
        assert test_tree.Root.LeftChild.LeftChild.NodeKey == 0
        assert test_tree.Root.LeftChild.LeftChild.LeftChild.NodeKey == -5

    def test_restore_one_element_tree(self):
        prefix_list = [10]
        infix_list = [10]

        test_tree = restore_tree(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 10
        assert test_tree.Root.LeftChild is None
        assert test_tree.Root.RightChild is None

    def test_restore_empty_tree(self):
        prefix_list = []
        infix_list = []

        test_tree = restore_tree(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root is None

    def test_restore_tree_negative(self):
        prefix_list = [0, -5, -2, 10, 15]
        infix_list = [-5, -2, 0, 10, 15]

        test_tree = restore_tree(prefix_list=prefix_list, infix_list=infix_list)

        assert test_tree.Root.NodeKey == 0

        assert test_tree.Root.LeftChild.NodeKey == -5
        assert test_tree.Root.LeftChild.RightChild.NodeKey == -2

        assert test_tree.Root.RightChild.NodeKey == 10
        assert test_tree.Root.RightChild.RightChild.NodeKey == 15
