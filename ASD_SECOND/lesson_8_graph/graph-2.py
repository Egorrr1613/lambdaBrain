"""
Задание: №8
Номер задачи из задания: №2
Краткое название: "Реализация направленного графа, представленного матрицей смежности.
                    Добавлен метод проверки на цикличность графа"
Сложность: Без оценки

Рефлексия:
    При разборе рекомендаций понял, что все сделал не правильно.
    Переписал на рекомендуемый вариант.
    Кажется нужно было вовремя отбрасывать слишком сложные варианты и подумать еще.
    Кажется, что до ассиметричной матрицы смежности мог бы додуматься сам.
    Тогда и финальное решение было бы ближе к правильному.
"""


class Vertex:

    def __init__(self, val: int):
        self.Value = val
        self.hit = False


class DirectionalGraph:

    def __init__(self, size: int):
        self.max_vertex: int = size
        self.m_adjacency: list[list] = [[0] * size for _ in range(size)]
        self.vertex: list = [None] * size

    def _is_valid_index(self, checked_i: int) -> bool:
        return 0 <= checked_i < len(self.vertex) and self.vertex[checked_i] is not None

    def AddVertex(self, v: int) -> None:
        if None not in self.vertex:
            return
        empty_index = self.vertex.index(None)
        self.vertex[empty_index] = Vertex(val=v)

    def RemoveVertex(self, v: int) -> None:
        if not self._is_valid_index(v):
            return
        for i in range(len(self.vertex)):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0
        self.vertex[v] = None

    def IsEdge(self, v1: int, v2: int) -> bool:
        if not self._is_valid_index(v1) or not self._is_valid_index(v2):
            return False
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int) -> None:
        if not self._is_valid_index(v1) or not self._is_valid_index(v2):
            return
        self.m_adjacency[v1][v2] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if not self._is_valid_index(v1) or not self._is_valid_index(v2):
            return
        self.m_adjacency[v1][v2] = 0

    def is_cycle(self) -> bool:
        if not self.vertex:
            return False

        recursion_stack = [False] * len(self.vertex)

        def _recursion_dfs(v: int) -> bool:
            if recursion_stack[v]:
                return True

            if self.vertex[v].hit:
                return False

            self.vertex[v].hit = True
            recursion_stack[v] = True

            for i in range(len(self.vertex)):
                if self.m_adjacency[v][i] == 1:
                    if _recursion_dfs(i):
                        return True

            recursion_stack[v] = False
            return False

        for check_vertex_i in range(len(self.vertex)):
            if self.vertex[check_vertex_i] is not None and not self.vertex[check_vertex_i].hit:
                if _recursion_dfs(check_vertex_i):
                    return True

        return False
