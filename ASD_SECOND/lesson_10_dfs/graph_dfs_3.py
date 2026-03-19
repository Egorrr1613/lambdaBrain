from ASD_SECOND.lesson_10_dfs.graph_dfs import SimpleGraph, Vertex


class TestDfsGraph:
    def test_dfs_in_empty_graph(self):
        test_graph = SimpleGraph(size=2)

        assert test_graph.DepthFirstSearch(v_from=0, v_to=1) == []

    def test_dfs_from_to_equal_node(self):
        test_graph = SimpleGraph(size=3)

        test_graph.AddVertex(1)
        test_graph.AddVertex(2)

        assert test_graph.DepthFirstSearch(v_from=1, v_to=1) == [test_graph.vertex[1]]
        assert test_graph.vertex[0].Hit is False
        assert test_graph.vertex[1].Hit is True

    def test_graph_simple_path(self):
        test_graph = SimpleGraph(size=3)

        test_graph.AddVertex(1)
        test_graph.AddVertex(2)

        assert test_graph.DepthFirstSearch(v_from=0, v_to=1) == []
        assert test_graph.vertex[0].Hit is True
        assert test_graph.vertex[1].Hit is False

        test_graph.AddEdge(0, 1)

        assert test_graph.DepthFirstSearch(v_from=0, v_to=1) == [test_graph.vertex[0], test_graph.vertex[1]]
        assert test_graph.vertex[0].Hit is True
        assert test_graph.vertex[1].Hit is False

    def test_graph_one_deep_path(self):
        test_graph = SimpleGraph(size=3)

        test_graph.AddVertex(1)
        test_graph.AddVertex(2)
        test_graph.AddVertex(3)

        test_graph.AddEdge(0, 1)
        test_graph.AddEdge(1, 2)

        assert test_graph.DepthFirstSearch(v_from=0, v_to=2) == [test_graph.vertex[0],
                                                                 test_graph.vertex[1],
                                                                 test_graph.vertex[2]]
