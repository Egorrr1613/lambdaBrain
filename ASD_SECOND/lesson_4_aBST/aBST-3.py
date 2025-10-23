from ASD_SECOND.lesson_4_aBST.aBST import aBST
from ASD_SECOND.lesson_4_aBST.aBST_2 import aBST as aBST_2


class TestCreateBst:

    def test_calculate_len(self):
        assert aBST(0)._calculate_tree_len(current_depth=0, depth=0, tree_len=0) == 1
        assert aBST(0)._calculate_tree_len(current_depth=0, depth=1, tree_len=0) == 3
        assert aBST(0)._calculate_tree_len(current_depth=0, depth=2, tree_len=0) == 7
        assert aBST(0)._calculate_tree_len(current_depth=0, depth=3, tree_len=0) == 15

    def test_abst_create(self):
        test_tree = aBST(0)
        assert test_tree.Tree == [None]

        test_tree = aBST(1)
        assert test_tree.Tree == [None, None, None]

        test_tree = aBST(2)
        assert test_tree.Tree == [None] * 7

        test_tree = aBST(3)
        assert test_tree.Tree == [None] * 15


class TestFindInAbst:

    def test_find_in_empty_abst(self):
        test_tree = aBST(0)

        assert test_tree.FindKeyIndex(8) == 0

    def test_find_none_in_abst(self):
        test_tree = aBST(2)
        test_tree.Tree = [1, -2, 3, -4, -1, 2, 7]

        assert test_tree.FindKeyIndex(0) is None
        assert test_tree.FindKeyIndex(8) is None

    def test_find_node(self):
        test_tree = aBST(2)
        test_tree.Tree = [1, -2, 3, -4, -1, 2, 7]

        assert test_tree.FindKeyIndex(1) == 0
        assert test_tree.FindKeyIndex(-2) == 1
        assert test_tree.FindKeyIndex(3) == 2
        assert test_tree.FindKeyIndex(-4) == 3
        assert test_tree.FindKeyIndex(-1) == 4
        assert test_tree.FindKeyIndex(2) == 5
        assert test_tree.FindKeyIndex(7) == 6

    def test_find_node_by_insert(self):
        test_tree = aBST(2)
        test_tree.Tree = [1, -2, 3, -4, None, None, None]

        assert test_tree.FindKeyIndex(-1) == -4
        assert test_tree.FindKeyIndex(2) == -5
        assert test_tree.FindKeyIndex(7) == -6

    def test_find_in_right_list_abst(self):
        test_tree = aBST(3)

        test_tree.AddKey(1)
        test_tree.AddKey(2)
        test_tree.AddKey(3)

        assert test_tree.FindKeyIndex(1) == 0
        assert test_tree.FindKeyIndex(2) == 2
        assert test_tree.FindKeyIndex(3) == 6
        assert test_tree.FindKeyIndex(4) == -14
        assert test_tree.FindKeyIndex(5) == -14


class TestInsertAbst:

    def test_insert_in_empty_tree(self):
        test_tree = aBST(0)

        assert test_tree.AddKey(5) == 0
        assert test_tree.FindKeyIndex(5) == 0
        assert test_tree.Tree == [5]

    def test_insert_as_right_list_abst(self):
        test_tree = aBST(2)

        assert test_tree.AddKey(1) == 0
        assert test_tree.AddKey(2) == 2
        assert test_tree.AddKey(2) == 2
        assert test_tree.AddKey(3) == 6
        assert test_tree.AddKey(4) == -1

        assert test_tree.Tree == [1, None, 2, None, None, None, 3]


class TestWideSearch:
    def test_wide_search_empty_tree(self):
        test_tree = aBST(0)
        assert test_tree.WideAllNodes() == (None,)

    def test_wide_search_one_node(self):
        test_tree = aBST(0)
        test_tree.AddKey(10)
        assert test_tree.WideAllNodes() == (10,)

    def test_wide_search_two_left_node(self):
        test_tree = aBST(1)
        test_tree.AddKey(key=10)
        test_tree.AddKey(key=9)

        all_nodes = test_tree.WideAllNodes()
        assert all_nodes == (10, 9, None)

    def test_wide_search_two_right_node(self):
        test_tree = aBST(1)
        test_tree.AddKey(key=10)
        test_tree.AddKey(key=11)

        all_nodes = test_tree.WideAllNodes()
        assert all_nodes == (10, None, 11)

    def test_wide_search_three_node(self):
        test_tree = aBST(1)
        test_tree.AddKey(key=10)
        test_tree.AddKey(key=5)
        test_tree.AddKey(key=11)

        all_nodes = test_tree.WideAllNodes()
        assert all_nodes == (10, 5, 11)

    def test_wide_search_seven_node(self):
        test_tree = aBST(2)
        test_tree.AddKey(key=10)
        test_tree.AddKey(key=5)
        test_tree.AddKey(key=20)
        test_tree.AddKey(key=3)
        test_tree.AddKey(key=6)
        test_tree.AddKey(key=11)
        test_tree.AddKey(key=25)

        all_nodes = test_tree.WideAllNodes()

        assert all_nodes == (10, 5, 20, 3, 6, 11, 25)

    def test_wide_search_random_nodes(self):
        test_tree = aBST(5)
        test_tree.AddKey(key=10)
        test_tree.AddKey(key=5)
        test_tree.AddKey(key=8)
        test_tree.AddKey(key=3)
        test_tree.AddKey(key=1)
        test_tree.AddKey(key=2)
        test_tree.AddKey(key=7)
        test_tree.AddKey(key=9)

        all_nodes = test_tree.WideAllNodes()
        assert all_nodes == (
            10,
            5,
            None,
            3,
            8,
            None,
            None,
            1,
            None,
            7,
            9,
            None,
            None,
            None,
            None,
            None,
            2,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        )


class TestFindLca:

    def test_find_when_lca_root(self):
        test_tree = aBST_2(1)
        test_tree.AddKey(key=10)
        test_tree.AddKey(key=5)
        test_tree.AddKey(key=15)

        lca = test_tree.find_lca(first_node_key=5, second_node_key=15)
        assert lca == 10

    def test_find_lca_1(self):
        test_tree = aBST_2(2)
        test_tree.AddKey(key=10)
        test_tree.AddKey(key=5)
        test_tree.AddKey(key=20)
        test_tree.AddKey(key=3)
        test_tree.AddKey(key=6)
        test_tree.AddKey(key=11)
        test_tree.AddKey(key=25)

        assert test_tree.find_lca(first_node_key=11, second_node_key=25) == 20
        assert test_tree.find_lca(first_node_key=6, second_node_key=11) == 10
        assert test_tree.find_lca(first_node_key=3, second_node_key=6) == 5
        assert test_tree.find_lca(first_node_key=3, second_node_key=25) == 10
