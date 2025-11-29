from ASD_SECOND.lesson_8_graph.graph import SimpleGraph
from ASD_SECOND.lesson_8_graph.graph_2 import AdjacencyType, DirectionalGraph


class TestSimpleGraph:

    def test_create_graph(self) -> None:
        test_graph = SimpleGraph(1)

        assert test_graph.m_adjacency == [[0]]
        assert test_graph.vertex == [None]
        assert test_graph.max_vertex == 1

    def test_add_vertex(self) -> None:
        test_graph = SimpleGraph(1)
        test_graph.AddVertex(5)

        assert test_graph.max_vertex == 1
        assert len(test_graph.vertex) == 1
        assert test_graph.vertex[0].Value == 5
        assert test_graph.m_adjacency == [[0]]

    def test_add_edge(self) -> None:
        test_graph = SimpleGraph(1)
        test_graph.AddVertex(5)

        assert test_graph.m_adjacency[0][0] == 0
        assert not test_graph.IsEdge(v1=0, v2=0)

        test_graph.AddEdge(v1=0, v2=0)

        assert test_graph.m_adjacency[0][0] == 1
        assert test_graph.IsEdge(v1=0, v2=0)

    def test_rm_edge(self) -> None:
        test_graph = SimpleGraph(1)

        test_graph.AddVertex(5)
        test_graph.AddEdge(v1=0, v2=0)

        test_graph.RemoveVertex(0)

        assert test_graph.vertex == [None]
        assert test_graph.m_adjacency[0][0] == 0
        assert not test_graph.IsEdge(v1=0, v2=0)


class TestGraph:
    def test_3x3_graph(self) -> None:
        test_graph = SimpleGraph(3)

        test_graph.AddVertex(5)
        test_graph.AddVertex(9)
        test_graph.AddVertex(14)
        test_graph.AddVertex(22)

        assert test_graph.max_vertex == 3
        assert test_graph.vertex[0].Value == 5
        assert test_graph.vertex[1].Value == 9
        assert test_graph.vertex[2].Value == 14
        assert test_graph.m_adjacency == [[0] * 3 for _ in range(3)]

        test_graph.RemoveVertex(0)
        assert test_graph.vertex[0] is None
        assert test_graph.vertex[1].Value == 9
        assert test_graph.vertex[2].Value == 14

        test_graph.RemoveVertex(0)
        assert test_graph.vertex[0] is None
        assert test_graph.vertex[1].Value == 9
        assert test_graph.vertex[2].Value == 14

        test_graph.RemoveVertex(1)
        assert test_graph.vertex[0] is None
        assert test_graph.vertex[1] is None
        assert test_graph.vertex[2].Value == 14

        test_graph.RemoveVertex(2)
        assert test_graph.vertex[0] is None
        assert test_graph.vertex[1] is None
        assert test_graph.vertex[2] is None

    def test_edge_3x3_graph(self) -> None:
        test_graph = SimpleGraph(3)

        test_graph.AddVertex(5)
        test_graph.AddVertex(9)
        test_graph.AddVertex(14)

        assert not test_graph.IsEdge(0, 2)
        test_graph.AddEdge(0, 2)

        expected_matrix = [[0] * 3 for _ in range(3)]
        expected_matrix[0][2] = 1

        assert test_graph.m_adjacency == expected_matrix
        assert test_graph.IsEdge(0, 2)

        test_graph.RemoveEdge(0, 2)
        assert test_graph.m_adjacency == [[0] * 3 for _ in range(3)]
        assert not test_graph.IsEdge(0, 2)

    def test_3x3_graph_edge(self) -> None:
        test_graph = SimpleGraph(3)

        for i in range(3):
            for j in range(3):
                assert not test_graph.IsEdge(i, j)

        test_graph.AddVertex(5)
        for i in range(3):
            for j in range(3):
                assert not test_graph.IsEdge(i, j)

        test_graph.AddVertex(9)
        test_graph.AddVertex(14)
        for i in range(3):
            for j in range(3):
                assert not test_graph.IsEdge(i, j)

        test_graph.AddEdge(0, 2)
        for i in range(3):
            for j in range(3):
                if i == 0 and j == 2:
                    assert test_graph.IsEdge(i, j)
                else:
                    assert not test_graph.IsEdge(i, j)

    def test_incorrect_arg(self) -> None:
        test_graph = SimpleGraph(2)

        test_graph.AddVertex(5)
        test_graph.AddVertex(55)

        test_graph.AddEdge(3, 4)
        for i in range(3):
            for j in range(3):
                assert not test_graph.IsEdge(i, j)

        test_graph.RemoveVertex(5)
        assert len(test_graph.vertex) == 2
        assert test_graph.vertex[0].Value == 5
        assert test_graph.vertex[1].Value == 55


class TestDirectionalGraph:
    def test_edge_1x1_graph(self) -> None:
        test_graph = DirectionalGraph(1)

        test_graph.AddVertex(5)

        assert test_graph.max_vertex == 1
        assert test_graph.m_adjacency == [[AdjacencyType.NO_ADJACENCY]]
        assert not test_graph.IsEdge(v1=0, v2=0)

        test_graph.AddEdge(0, 0)

        assert test_graph.is_cycle()
        assert test_graph.m_adjacency[0][0] == AdjacencyType.SELF_LINK
        assert test_graph.IsEdge(v1=0, v2=0)

    def test_edge_3x3_graph(self) -> None:
        test_graph = DirectionalGraph(3)

        test_graph.AddVertex(5)
        test_graph.AddVertex(9)
        test_graph.AddVertex(14)

        assert not test_graph.IsEdge(0, 2)
        test_graph.AddEdge(0, 2)

        expected_matrix = [[AdjacencyType.NO_ADJACENCY] * 3 for _ in range(3)]
        expected_matrix[0][2] = "0|2"

        assert test_graph.m_adjacency == expected_matrix
        assert test_graph.IsEdge(0, 2)

        test_graph.RemoveEdge(0, 2)
        assert test_graph.m_adjacency == [[AdjacencyType.NO_ADJACENCY] * 3 for _ in range(3)]
        assert not test_graph.IsEdge(0, 2)
