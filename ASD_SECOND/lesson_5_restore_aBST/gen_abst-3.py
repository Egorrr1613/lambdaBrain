from ASD_SECOND.lesson_5_restore_aBST.gen_abst import GenerateBBSTArray
from ASD_SECOND.lesson_5_restore_aBST.gen_abst_2 import delete_element


class TestGenerateTree:
    def test_gen_empty_tree(self) -> None:
        assert not GenerateBBSTArray([])

    def test_gen_tree_one_el(self) -> None:
        assert GenerateBBSTArray([5]) == [5]

    def test_gen_simple_tree(self) -> None:
        test_array = [3, 1, 2]
        assert GenerateBBSTArray(input_list=test_array) == [2, 1, 3]

    def test_gen_tree_2(self) -> None:
        test_array = [1, 2, 3, 4, 5, 6, 7]
        assert GenerateBBSTArray(input_list=test_array) == [4, 2, 6, 1, 3, 5, 7]

    def test_gen_tree_3(self) -> None:
        test_array = list(range(1, 16))
        assert (GenerateBBSTArray(input_list=test_array) ==
                [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])


class TestDeleteAndBalanceTree:

    def test_del_and_balance_non_element(self) -> None:
        assert delete_element(binary_search_tree_list=[2, 1, 3], key_to_delete=8) is None

    def test_del_and_balance_one_el_tree(self) -> None:
        assert delete_element(binary_search_tree_list=[1], key_to_delete=1) == [None]

    def test_del_and_balance_simple_node(self) -> None:
        assert delete_element(binary_search_tree_list=[2, 1, 3], key_to_delete=1) == [3, 2, None]

    def test_del_and_balance_simple_node_2(self) -> None:
        assert delete_element(binary_search_tree_list=[2, 1, 3], key_to_delete=3) == [2, 1, None]

    def test_del_one_node_and_need_balance_tree(self) -> None:
        """В этом кейсе проверяю корректность ребалансировки дерева при удалении листа"""
        assert (delete_element(binary_search_tree_list=[5, 3, 6, 2, 4, None, None], key_to_delete=6) ==
                [4, 3, 5, 2, None, None, None])

    def test_del_one_node_and_no_rebalance_tree(self) -> None:
        assert (delete_element(binary_search_tree_list=[5, 3, 6, 2, 4, None, 7], key_to_delete=7) ==
                [4, 3, 6, 2, None, 5, None])

    def test_rebalance_if_delete_root_tree(self) -> None:
        assert (delete_element(binary_search_tree_list=[4, 2, 6, 1, 3, 5, 7], key_to_delete=4) ==
                [5, 2, 7, 1, 3, 6, None])

