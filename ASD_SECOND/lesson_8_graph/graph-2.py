class AdjacencyType:
    MUTUALLY = "MUTUALLY"
    NO_ADJACENCY = "NO_ADJACENCY"
    SELF_LINK = "SELF_LINK"


class Vertex:

    def __init__(self, val: int):
        self.Value = val


def _coordinate_to_str(v1: int, v2: int) -> str:
    return str(v1) + "|" + str(v2)


class DirectionalGraph:

    def __init__(self, size: int):
        self.max_vertex: int = size
        self.m_adjacency: list[list] = [[AdjacencyType.NO_ADJACENCY] * size for _ in range(size)]
        self.vertex: list = [None] * size

    def _is_index_in_adjacency(self, i_to_check_1: int, i_to_check_2: int) -> bool:
        if i_to_check_1 >= len(self.vertex) or i_to_check_2 >= len(self.vertex):
            return False
        return self.vertex[i_to_check_1] is not None or self.vertex[i_to_check_2] is not None

    def AddVertex(self, v: int) -> None:
        if None not in self.vertex:
            return
        empty_index = self.vertex.index(None)
        self.vertex[empty_index] = Vertex(val=v)

    def RemoveVertex(self, v: int) -> None:
        if v >= len(self.vertex):
            return
        for relation_index, _ in enumerate(self.m_adjacency[v]):
            self._remove_all_edge(v1=v, v2=relation_index)
        self.vertex[v] = None

    def IsEdge(self, v1: int, v2: int) -> bool:
        if not self._is_index_in_adjacency(i_to_check_1=v1, i_to_check_2=v2):
            return False

        return (self.m_adjacency[v1][v2] == AdjacencyType.MUTUALLY or
                self.m_adjacency[v1][v2] == _coordinate_to_str(v1, v2) or
                self.m_adjacency[v1][v2] == AdjacencyType.SELF_LINK)

    def AddEdge(self, v1: int, v2: int) -> None:
        if (not self._is_index_in_adjacency(i_to_check_1=v1, i_to_check_2=v2)
                or self.m_adjacency[v1][v2] == AdjacencyType.MUTUALLY):
            return

        if v1 == v2:
            self.m_adjacency[v1][v2] = AdjacencyType.SELF_LINK
            return

        if self.m_adjacency[v1][v2] == _coordinate_to_str(v1=v2, v2=v1):
            self.m_adjacency[v1][v2] = AdjacencyType.MUTUALLY
            return

        new_adjacency = _coordinate_to_str(v1, v2)
        assert self.m_adjacency[v1][v2] in [AdjacencyType.NO_ADJACENCY,
                                            new_adjacency], "Некорректное состояние матрицы"
        self.m_adjacency[v1][v2] = new_adjacency

    def _remove_all_edge(self, v1: int, v2: int) -> None:
        if not self._is_index_in_adjacency(i_to_check_1=v1, i_to_check_2=v2):
            return

        self.m_adjacency[v1][v2] = AdjacencyType.NO_ADJACENCY

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if (not self._is_index_in_adjacency(i_to_check_1=v1, i_to_check_2=v2) or
                self.m_adjacency[v1][v2] == _coordinate_to_str(v1=v2, v2=v1) or
                self.m_adjacency[v1][v2] == AdjacencyType.NO_ADJACENCY):
            return

        if v1 == v2:
            self.m_adjacency[v1][v2] = AdjacencyType.NO_ADJACENCY
            return

        if self.m_adjacency[v1][v2] == _coordinate_to_str(v1, v2):
            self.m_adjacency[v1][v2] = AdjacencyType.NO_ADJACENCY
            return

        if self.m_adjacency[v1][v2] == AdjacencyType.MUTUALLY:
            self.m_adjacency[v1][v2] = _coordinate_to_str(v1=v2, v2=v1)
            return

        raise AssertionError("Не корректное состояние матрицы")

    def is_cycle(self) -> bool:
        for i in range(self.max_vertex):
            for j in range(self.max_vertex):
                if self.m_adjacency[i][j] == AdjacencyType.SELF_LINK:
                    return True
        return False
