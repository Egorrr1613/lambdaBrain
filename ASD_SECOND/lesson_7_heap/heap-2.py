"""
Задание: №7
Номер задачи из задания: №5
Краткое название: "Эффективный алгоритм поиска в куче элемента по заданному условию"
Сложность: size -  / time -

Рефлексия:

"""


def find_first_index_not_none(input_list) -> int | None:
    for i in range(len(input_list) - 1, -1, -1):
        if input_list[i]:
            return i


def find_first_index_none(input_list) -> int | None:
    for i in range(len(input_list)):
        if input_list[i] is None:
            return i


RIGHT_CHILD = "RIGHT_CHILD"
LEFT_CHILD = "LEFT_CHILD"
PARENT = "PARENT"

calculate_index = {
    RIGHT_CHILD: lambda x: 2 * x + 2,
    LEFT_CHILD: lambda x: 2 * x + 1,
    PARENT: lambda x: (x - 1) // 2,
}


def get_max_by_index(input_list: list, first_index, second_index) -> int:
    list_len = len(input_list)
    if first_index >= list_len and second_index >= list_len:
        return -1

    if first_index < list_len <= second_index and input_list[first_index] is not None:
        return first_index

    if first_index >= list_len > second_index and input_list[second_index] is not None:
        return second_index

    if first_index >= list_len or second_index >= list_len:
        return -1

    if input_list[first_index] is not None and input_list[second_index] is None:
        return first_index

    if input_list[first_index] is None and input_list[second_index] is not None:
        return second_index

    if input_list[first_index] is not None and input_list[second_index] is not None:
        return first_index if input_list[first_index] >= input_list[second_index] else second_index

    return -1


class Heap:

    def __init__(self) -> None:
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def _calculate_tree_len(self, current_dept: int, dept: int) -> int:
        if current_dept == dept:
            return 2 ** current_dept
        return 2 ** current_dept + self._calculate_tree_len(current_dept=current_dept + 1, dept=dept)

    def MakeHeap(self, input_list: list[int], depth: int) -> None:
        heap_len = self._calculate_tree_len(current_dept=0, dept=depth)
        assert heap_len >= len(input_list)
        self.HeapArray = heap_len * [None]
        for element in input_list:
            assert self.Add(key=element), "Элемент был корректно добавлен"

    def _recursion_rebuild_heap_to_down(self, heap: list, current_index: int) -> list:
        left_index = calculate_index[LEFT_CHILD](current_index)
        right_index = calculate_index[RIGHT_CHILD](current_index)

        max_i_by_child = get_max_by_index(input_list=heap, first_index=left_index, second_index=right_index)

        if max_i_by_child == -1:
            return heap
        if heap[current_index] >= heap[max_i_by_child]:
            return heap

        current_value = heap[current_index]
        heap[current_index] = heap[max_i_by_child]
        heap[max_i_by_child] = current_value
        return self._recursion_rebuild_heap_to_down(heap=heap, current_index=max_i_by_child)

    def GetMax(self) -> int:
        if len(self.HeapArray) == 0:
            return -1

        if len(self.HeapArray) == 1:
            return self.HeapArray.pop()

        max_element = self.HeapArray[0]
        index_min_el = find_first_index_not_none(self.HeapArray)
        self.HeapArray[0] = self.HeapArray[index_min_el]
        self.HeapArray[index_min_el] = None

        self.HeapArray = self._recursion_rebuild_heap_to_down(heap=self.HeapArray, current_index=0)

        return max_element

    def _recursion_rebuild_down_to_top(self, heap: list, current_index: int) -> list:
        if current_index == 0:
            return heap

        parent_index = calculate_index[PARENT](current_index)
        if heap[current_index] <= heap[parent_index]:
            return heap
        buffer = heap[current_index]
        heap[current_index] = heap[parent_index]
        heap[parent_index] = buffer
        return self._recursion_rebuild_down_to_top(heap=heap, current_index=parent_index)

    def Add(self, key: int) -> bool:
        index_to_insert = find_first_index_none(input_list=self.HeapArray)
        if index_to_insert == -1 or index_to_insert is None:
            return False
        self.HeapArray[index_to_insert] = key
        self.HeapArray = self._recursion_rebuild_down_to_top(heap=self.HeapArray, current_index=index_to_insert)
        return True

    def _recursion_check_heap(self, current_index: int) -> bool:
        if current_index >= len(self.HeapArray) or self.HeapArray[current_index] is None:
            return True

        left_index = calculate_index[LEFT_CHILD](current_index)
        right_index = calculate_index[RIGHT_CHILD](current_index)

        is_left_in_range = left_index < len(self.HeapArray)
        is_right_in_range = right_index < len(self.HeapArray)

        if is_left_in_range and self.HeapArray[left_index] is not None and self.HeapArray[current_index] < \
                self.HeapArray[left_index]:
            return False

        if is_right_in_range and self.HeapArray[right_index] is not None and self.HeapArray[current_index] < \
                self.HeapArray[right_index]:
            return False

        return self._recursion_check_heap(left_index) and self._recursion_check_heap(right_index)

    def is_correct_heap(self) -> bool:
        if len(self.HeapArray) == 0:
            return True
        return self._recursion_check_heap(current_index=0)

    def _has_value_at_index(self, index: int, len_heap: int):
        return 0 <= index < len_heap and self.HeapArray[index] is not None

    def find_max_el_in_range(self, min_range: int, max_range: int) -> int:
        """
        Задание: №7
        Номер задачи из задания: №4
        Краткое название: "Поиск максимального элемента в заданном диапазоне значений"
        Сложность: size - O(n) / time - O(n)

        Рефлексия:
            Если требуется найти элемент по условию "меньше заданного значения" - то можно пойти от "листов кучи".
            Это удобно, если куча реализованна массивом, так как индексы листов можно элементарно вычислить.

        """

        if self.HeapArray[0] is None:
            return -1

        index_in_find_range = []
        search_index_queue = [0]
        len_heap = len(self.HeapArray)

        while search_index_queue:
            check_index = search_index_queue.pop(0)

            left_child = calculate_index[LEFT_CHILD](check_index)
            if self._has_value_at_index(index=left_child,
                                        len_heap=len_heap):
                search_index_queue.append(left_child)

            right_child = calculate_index[RIGHT_CHILD](check_index)
            if self._has_value_at_index(index=right_child,
                                        len_heap=len_heap):
                search_index_queue.append(right_child)

            if calculate_index[PARENT](check_index) in index_in_find_range:
                break

            if min_range <= self.HeapArray[check_index] <= max_range:
                index_in_find_range.append(check_index)

        if not index_in_find_range:
            return -1

        return max(index_in_find_range, key=lambda i: self.HeapArray[i])

