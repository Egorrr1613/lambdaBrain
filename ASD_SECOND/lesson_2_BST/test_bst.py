from ASD_SECOND.lesson_2_BST.bst import BST, BSTNode


def test_bst_create():
    test_tree = BST(node=None)
    assert test_tree.Count() == 0

    test_tree.AddKeyValue(key=88, val=77)
    assert test_tree.Count() == 1
    assert test_tree.Root.NodeKey == 88
    assert test_tree.Root.NodeValue == 77

    test_tree = BST(node=BSTNode(key=88, val=77, parent=None))
    assert test_tree.Count() == 1
    assert test_tree.Root.NodeKey == 88
    assert test_tree.Root.NodeValue == 77


def test_bst_find_node():
    empty_tree = BST(node=None)
    find_empty_tree = empty_tree.FindNodeByKey(1)
    assert find_empty_tree.Node is None
    assert find_empty_tree.NodeHasKey is False
    assert find_empty_tree.ToLeft is False

    root_node = BSTNode(key=88, val=77, parent=None)
    test_tree = BST(node=root_node)
    assert test_tree.Count() == 1
    assert test_tree.Root.NodeKey == 88
    assert test_tree.Root.NodeValue == 77

    find_result = test_tree.FindNodeByKey(88)
    assert find_result.Node is root_node
    assert find_result.NodeHasKey is True
    assert find_result.ToLeft is False

    find_non_exist_right = test_tree.FindNodeByKey(111)
    assert find_non_exist_right.Node is root_node
    assert find_non_exist_right.NodeHasKey is False
    assert find_non_exist_right.ToLeft is False

    find_non_exist_left = test_tree.FindNodeByKey(11)
    assert find_non_exist_left.Node is root_node
    assert find_non_exist_left.NodeHasKey is False
    assert find_non_exist_left.ToLeft is True


def test_add_node():
    test_tree = BST(BSTNode(key=1, val="aa", parent=None))
    assert test_tree.Count() == 1
    assert test_tree.FindNodeByKey(key=0).NodeHasKey is False
    assert test_tree.FindNodeByKey(key=2).NodeHasKey is False

    test_tree.AddKeyValue(key=0, val="bbb")
    assert test_tree.Root.RightChild is None
    assert type(test_tree.Root.LeftChild) is BSTNode
    assert test_tree.Root.LeftChild.NodeKey == 0
    assert test_tree.Root.LeftChild.NodeValue == "bbb"
    assert test_tree.Count() == 2
    assert test_tree.FindNodeByKey(key=0).NodeHasKey is True
    assert test_tree.FindNodeByKey(key=2).NodeHasKey is False

    test_tree.AddKeyValue(key=2, val="ccc")
    assert type(test_tree.Root.RightChild) is BSTNode
    assert test_tree.Root.RightChild.NodeKey == 2
    assert test_tree.Root.RightChild.NodeValue == "ccc"
    assert test_tree.Count() == 3
    assert test_tree.FindNodeByKey(key=0).NodeHasKey is True
    assert test_tree.FindNodeByKey(key=2).NodeHasKey is True


def test_find_min_max_node():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.AddKeyValue(key=-2, val="bb")
    test_tree.AddKeyValue(key=-8, val="ccc")
    test_tree.AddKeyValue(key=6, val="dddd")
    test_tree.AddKeyValue(key=7, val="eeeee")
    test_tree.AddKeyValue(key=3, val="ffff")
    test_tree.AddKeyValue(key=4, val="ggg")
    test_tree.AddKeyValue(key=2, val="hh")
    test_tree.AddKeyValue(key=10, val="i")

    max_node = test_tree.Root.RightChild.RightChild.RightChild

    assert (
        test_tree.FinMinMax(FromNode=test_tree.Root, FindMax=False)
        is test_tree.Root.LeftChild.LeftChild
    )
    assert test_tree.FinMinMax(FromNode=test_tree.Root, FindMax=True) is max_node

    assert (
        test_tree.FinMinMax(FromNode=test_tree.Root.RightChild, FindMax=True)
        is max_node
    )
    assert (
        test_tree.FinMinMax(FromNode=test_tree.Root.RightChild, FindMax=False)
        is test_tree.Root.RightChild.LeftChild.LeftChild
    )


def test_del_node():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.AddKeyValue(key=-2, val="bb")
    test_tree.AddKeyValue(key=-8, val="ccc")
    test_tree.AddKeyValue(key=6, val="dddd")
    test_tree.AddKeyValue(key=7, val="eeeee")
    test_tree.AddKeyValue(key=3, val="ffff")
    test_tree.AddKeyValue(key=4, val="ggg")
    test_tree.AddKeyValue(key=2, val="hh")
    test_tree.AddKeyValue(key=10, val="i")
    assert test_tree.Count() == 9

    assert test_tree.DeleteNodeByKey(5) is False

    assert test_tree.DeleteNodeByKey(10) is True
    assert test_tree.FindNodeByKey(10).NodeHasKey is False
    assert test_tree.Root.RightChild.RightChild.RightChild is None
    assert test_tree.Count() == 8

    assert test_tree.DeleteNodeByKey(6) is True
    assert test_tree.FindNodeByKey(6).NodeHasKey is False
    assert test_tree.Root.RightChild.NodeKey == 7
    assert test_tree.Count() == 7
    assert test_tree.Root.RightChild.RightChild is None
    assert test_tree.Root.RightChild.LeftChild.NodeKey == 3


def test_del_node_2():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.AddKeyValue(key=-2, val="bb")
    test_tree.AddKeyValue(key=-8, val="ccc")
    test_tree.AddKeyValue(key=6, val="dddd")
    test_tree.AddKeyValue(key=3, val="ffff")
    test_tree.AddKeyValue(key=4, val="ggg")
    test_tree.AddKeyValue(key=2, val="hh")
    assert test_tree.Count() == 7

    assert test_tree.DeleteNodeByKey(6) is True
    assert test_tree.Root.RightChild.NodeKey == 3
    assert test_tree.Root.RightChild.RightChild.NodeKey == 4
    assert test_tree.Root.RightChild.LeftChild.NodeKey == 2


def test_del_node_3():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.AddKeyValue(key=-2, val="b")
    test_tree.AddKeyValue(key=-8, val="c")
    test_tree.AddKeyValue(key=6, val="d")
    test_tree.AddKeyValue(key=3, val="e")
    test_tree.AddKeyValue(key=4, val="f")
    test_tree.AddKeyValue(key=2, val="g")
    test_tree.AddKeyValue(key=10, val="h")
    test_tree.AddKeyValue(key=15, val="i")
    test_tree.AddKeyValue(key=8, val="j")
    test_tree.AddKeyValue(key=7, val="k")
    test_tree.AddKeyValue(key=9, val="l")

    assert test_tree.DeleteNodeByKey(6) is True
    assert test_tree.Root.RightChild.NodeKey == 7
    assert test_tree.Root.RightChild.LeftChild.NodeKey == 3
    assert test_tree.Root.RightChild.RightChild.NodeKey == 10
    assert test_tree.FindNodeByKey(8).Node.LeftChild is None


def test_del_node_4():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.AddKeyValue(key=6, val="b")
    test_tree.AddKeyValue(key=5, val="c")

    test_tree.DeleteNodeByKey(6)
    assert test_tree.Count() == 2
    assert test_tree.Root.NodeKey == 1
    assert test_tree.Root.RightChild.NodeKey == 5
    assert test_tree.Root.RightChild.RightChild is None
    assert test_tree.Root.RightChild.LeftChild is None
    assert test_tree.Root.RightChild.Parent.NodeKey == 1


def test_del_node_5():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.AddKeyValue(key=6, val="b")
    test_tree.AddKeyValue(key=15, val="c")

    test_tree.DeleteNodeByKey(6)
    assert test_tree.Count() == 2
    assert test_tree.Root.NodeKey == 1
    assert test_tree.Root.RightChild.NodeKey == 15
    assert test_tree.Root.RightChild.RightChild is None
    assert test_tree.Root.RightChild.LeftChild is None
    assert test_tree.Root.RightChild.Parent.NodeKey == 1


def test_del_node_6():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.AddKeyValue(key=6, val="b")
    test_tree.AddKeyValue(key=15, val="c")

    assert test_tree.DeleteNodeByKey(1)
    assert test_tree.Root.NodeKey == 6
    assert test_tree.Root.RightChild.NodeKey == 15


def test_del_node_7():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.AddKeyValue(key=6, val="b")
    test_tree.AddKeyValue(key=0, val="c")

    assert test_tree.DeleteNodeByKey(1)
    assert test_tree.Root.NodeKey == 6
    assert test_tree.Root.RightChild is None
    assert test_tree.Root.LeftChild.NodeKey == 0


def test_del_node_and_tree_stay_empty():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.DeleteNodeByKey(1)

    assert test_tree.Root is None
    assert test_tree.Count() == 0


def test_del_node_last_child():
    test_tree = BST(BSTNode(key=1, val="a", parent=None))
    test_tree.AddKeyValue(key=6, val="b")
    test_tree.AddKeyValue(key=0, val="c")


def test_del_leaf_from_left_subtree():
    test_tree = BST(BSTNode(key=3, val="a", parent=None))
    test_tree.AddKeyValue(key=6, val="b")
    test_tree.AddKeyValue(key=0, val="c")
    test_tree.AddKeyValue(key=-2, val="c")

    assert test_tree.DeleteNodeByKey(-2)
    assert test_tree.Root.LeftChild.LeftChild is None
    assert test_tree.Root.LeftChild.NodeKey == 0

    assert test_tree.DeleteNodeByKey(0)
    assert test_tree.Root.LeftChild is None
    assert test_tree.Root.NodeKey == 3


def test_del_root_node_with_one_child():
    test_tree = BST(BSTNode(key=10, val="a", parent=None))
    test_tree.AddKeyValue(key=5, val="b")
    test_tree.AddKeyValue(key=8, val="c")
    test_tree.AddKeyValue(key=2, val="c")

    assert test_tree.DeleteNodeByKey(10)
    assert test_tree.Root.NodeKey == 5
    assert test_tree.Root.LeftChild.NodeKey == 2
    assert test_tree.Root.RightChild.NodeKey == 8


def test_del_left_sub_node_with_one_child():
    test_tree = BST(BSTNode(key=10, val="a", parent=None))
    test_tree.AddKeyValue(key=5, val="b")
    test_tree.AddKeyValue(key=2, val="c")

    assert test_tree.DeleteNodeByKey(5)
    assert test_tree.Root.NodeKey == 10
    assert test_tree.Root.LeftChild.NodeKey == 2
    assert test_tree.Root.LeftChild.LeftChild is None


def test_del_left_sub_node_with_two_child():
    test_tree = BST(BSTNode(key=10, val="a", parent=None))
    test_tree.AddKeyValue(key=5, val="b")
    test_tree.AddKeyValue(key=8, val="b")
    test_tree.AddKeyValue(key=3, val="c")
    test_tree.AddKeyValue(key=1, val="c")
    test_tree.AddKeyValue(key=2, val="c")

    assert test_tree.DeleteNodeByKey(5)
    assert test_tree.Root.LeftChild.NodeKey == 8
    assert test_tree.Root.LeftChild.RightChild is None
    assert test_tree.Root.LeftChild.LeftChild.NodeKey == 3


def test_del_left_sub_node_with_two_child_2():
    test_tree = BST(BSTNode(key=10, val="a", parent=None))
    test_tree.AddKeyValue(key=5, val="b")
    test_tree.AddKeyValue(key=8, val="b")
    test_tree.AddKeyValue(key=3, val="c")
    test_tree.AddKeyValue(key=1, val="c")
    test_tree.AddKeyValue(key=2, val="c")
    test_tree.AddKeyValue(key=7, val="c")
    test_tree.AddKeyValue(key=9, val="c")

    assert test_tree.DeleteNodeByKey(5)
    assert test_tree.Root.LeftChild.NodeKey == 7
    assert test_tree.Root.LeftChild.RightChild.NodeKey == 8
    assert test_tree.Root.LeftChild.LeftChild.NodeKey == 3
    assert test_tree.Root.LeftChild.LeftChild.Parent.NodeKey == 7
    assert test_tree.Root.LeftChild.RightChild.Parent.NodeKey == 7
    assert test_tree.Root.LeftChild.RightChild.LeftChild is None
