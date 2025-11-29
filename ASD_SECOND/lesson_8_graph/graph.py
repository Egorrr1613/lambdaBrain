class Vertex:

    def __init__(self, val: int):
        self.Value = val


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex: int = size
        self.m_adjacency: list[list] = [[0] * size for _ in range(size)]
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
            self.RemoveEdge(v1=v, v2=relation_index)
        self.vertex[v] = None

    def IsEdge(self, v1: int, v2: int) -> bool:
        if not self._is_index_in_adjacency(i_to_check_1=v1, i_to_check_2=v2):
            return False

        return bool(self.m_adjacency[v1][v2])

    def AddEdge(self, v1: int, v2: int) -> None:
        if not self._is_index_in_adjacency(i_to_check_1=v1, i_to_check_2=v2):
            return

        self.m_adjacency[v1][v2] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if not self._is_index_in_adjacency(i_to_check_1=v1, i_to_check_2=v2):
            return

        self.m_adjacency[v1][v2] = 0
