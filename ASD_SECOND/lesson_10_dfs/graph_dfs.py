class Vertex:

    def __init__(self, val: int):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex: int = size
        self.m_adjacency: list[list] = [[0] * size for _ in range(size)]
        self.vertex: list = [None] * size
        self.stack_to_dfs = []

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

    def _get_list_edge_index(self, current_vertex_i: int) -> list[int | None]:
        return [check_vertex_i for check_vertex_i in range(self.max_vertex) if
                self.IsEdge(current_vertex_i, check_vertex_i)]

    def _recursion_dfs(self, curr_vertex_i: int, vertex_i_to: int) -> list[None | Vertex]:
        self.vertex[curr_vertex_i].Hit = True
        self.stack_to_dfs.append(self.vertex[curr_vertex_i])

        all_i_edge_to_curr_vertex = self._get_list_edge_index(curr_vertex_i)

        if vertex_i_to in all_i_edge_to_curr_vertex:
            self.stack_to_dfs.append(self.vertex[vertex_i_to])
            return self.stack_to_dfs

        non_hit_edge_i_vertex = list(filter(lambda i: not getattr(self.vertex[i], "Hit"), all_i_edge_to_curr_vertex))

        assert len(non_hit_edge_i_vertex) >= 0, "Длина списка не посещенных соседей не может быть отрицательной."
        if len(non_hit_edge_i_vertex) > 0:
            return self._recursion_dfs(curr_vertex_i=non_hit_edge_i_vertex[0], vertex_i_to=vertex_i_to)

        last_from_stack = self.stack_to_dfs.pop()
        if len(self.stack_to_dfs) == 0:
            return []
        return self._recursion_dfs(curr_vertex_i=last_from_stack, vertex_i_to=vertex_i_to)

    def DepthFirstSearch(self, v_from: int, v_to: int) -> list[None | Vertex]:
        [setattr(v, 'Hit', False) for v in self.vertex if v]
        self.stack_to_dfs = []

        if (v_from >= len(self.vertex) or v_to >= len(self.vertex)
                or self.vertex[v_from] is None or self.vertex[v_to] is None):
            return []

        if v_from == v_to:
            self.vertex[v_from].Hit = True
            return [self.vertex[v_from]]

        return self._recursion_dfs(curr_vertex_i=v_from, vertex_i_to=v_to)

