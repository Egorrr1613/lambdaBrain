class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc: bool):
        self.head: Node | None = None
        self.tail: Node | None = None

        self.__ascending = asc
        self.count_el = 0

    def compare(self, v1, v2) -> int | tuple[str]:
        if v1 == v2:
            return 0

        if self.__ascending and v1 < v2:
            return -1
        if not self.__ascending and v1 > v2:
            return -1
        if not self.__ascending and v1 < v2:
            return 1
        if self.__ascending and v1 > v2:
            return 1
        return ("Error: Compare error",)

    def add(self, value) -> None | tuple[str]:
        new_node = Node(value)

        if self.count_el == 0:
            self.head = new_node
            self.tail = new_node

            self.count_el += 1
            return None

        if self.count_el == 1:
            compare_result = self.compare(v1=self.tail.value, v2=new_node.value)
            if compare_result in (0, 1):
                self.head = new_node
                new_node.next = self.tail
                self.tail.prev = self.head
            if compare_result == -1:
                self.tail = new_node
                self.head.next = self.tail
                self.tail.prev = self.head
            self.count_el += 1
            return None

        if self.compare(v1=self.tail.value, v2=new_node.value) == -1:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

            self.count_el += 1
            return None

        iter_node = self.head
        while isinstance(iter_node, Node):
            compare_result = self.compare(iter_node.value, new_node.value)

            if compare_result in (0, 1):
                new_node.prev = iter_node.prev
                new_node.next = iter_node

                if iter_node is self.head:
                    self.head = new_node
                else:
                    iter_node.prev.next = new_node
                iter_node.prev = new_node
                self.count_el += 1
                return None

            if compare_result == -1:
                iter_node = iter_node.next
                continue

            return ("Error: Incorrect compare result",)
        return ("Error: Incorrect state",)

    def find(self, val) -> Node | None | tuple[str]:
        iter_node = self.head
        while isinstance(iter_node, Node):
            compare_res = self.compare(val, iter_node.value)
            if compare_res == 0:
                return iter_node
            if compare_res == -1:
                return None
            if compare_res == 1:
                iter_node = iter_node.next
                continue
            return ("Error: Incorrect compare result",)
        return None

    def delete(self, val) -> None:
        if self.head is None or self.compare(v1=self.tail.value, v2=val) == -1:
            return None

        iter_node = self.head
        while isinstance(iter_node, Node):
            compare_res = self.compare(iter_node.value, val)
            if compare_res == 0:

                if iter_node is self.head and iter_node is self.tail:
                    self.head = None
                    self.tail = None
                    self.count_el = 0
                    return None

                if iter_node is self.head:
                    self.head = iter_node.next
                    self.head.prev = None
                    self.count_el -= 1
                    return None

                if iter_node is self.tail:
                    self.tail = iter_node.prev
                    self.tail.next = None
                    self.count_el -= 1
                    return None

                iter_node.prev.next = iter_node.next
                iter_node.next.prev = iter_node.prev

                self.count_el -= 1
                return None
            if compare_res == 1:
                return None
            if compare_res == -1:
                iter_node = iter_node.next
        return None

    def clean(self, asc) -> None:
        self.__ascending = asc
        self.head = None
        self.tail = None
        self.count_el = 0

    def len(self) -> int:
        return self.count_el

    def get_all(self) -> list:
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def get_all_v2(self) -> list:
        node: Node | None = self.head
        res = []
        while isinstance(node, Node):
            if node is self.head:
                prev_node_val = None
            else:
                prev_node_val = node.prev.value
            if node is self.tail:
                next_node_val = None
            else:
                next_node_val = node.next.value
            res.append((prev_node_val, node.value, next_node_val))
            node = node.next
        return res

    def delete_duplicate(self):
        """
        Задание: №7
        Номер задачи из задания: №8
        Краткое название: "Метод удаления всех дубликатов из упорядоченного списка"
        Сложность: size - O(1)/time - O(n)
        """
        if self.count_el < 2:
            return
        current_node = self.head

        while current_node.next is not None:
            compare_result = self.compare(current_node.value, current_node.next.value)
            if compare_result == 0:
                self.delete(current_node.value)
            current_node = current_node.next

    def has_sub_list(self, sublist: "OrderedList") -> bool:
        """
        Задание: №7
        Номер задачи из задания: №10
        Краткое название: "Метод проверки наличия упорядоченного под-списка в списке"
        Сложность: size - O(1)/time - O(n)

        Рефлексия:
            Самостоятельно реализовал через линейный поиск.
            Однако во время написания рефлексии по заданию обратил внимание на свою частую проблему, а именно опять
            в решении было много лишних проверок завязанных на косвенные признаки, вместо явных состояний.
            Решил переписать решение. Выписал на бумагу все явные состояния,
            которые будут возникать по ходу моего алгоритма. Оказалось всего 10 штук комбинаций таких состояний:
                * Очередная нода в основном списке и head в sub_list (None/None, Node/None, Node/None, None/Node)
                * Очередная нода в основном списке и очередная нода из sub_list (None/None, Node/None, Node/None, None/Node)
                * Совпадает ли значения ноды из основного списка и sub_list(True/False)

            Далее переписал основную часть решения, завязав логику алгоритма ТОЛЬКО на комбинации этих состояний,
            прописывая условия поведения под каждое из них.
            Получилось не идеально, но лучше и надежнее чем было.
            И немного короче - 27 строк нового решения против 35 строк старого.
        """
        if sublist.head is None or (self.head is None and sublist.head is None):
            return True
        if self.head is None:
            return False
        if (
            self.compare(v1=sublist.head.value, v2=self.tail.value) == 1
            or sublist.count_el > self.count_el
        ):
            return False
        current_main_node = self.head
        while current_main_node is not None:
            if current_main_node.value != sublist.head.value:
                current_main_node = current_main_node.next
                continue
            compare_node_by_main = current_main_node.next
            compare_sublist_node = sublist.head.next
            while compare_sublist_node is not None:
                if compare_node_by_main is None:
                    return False
                if compare_node_by_main.value != compare_sublist_node.value:
                    current_main_node = current_main_node.next
                    break
                compare_node_by_main = compare_node_by_main.next
                compare_sublist_node = compare_sublist_node.next
            if compare_sublist_node is None:
                return True
        return False

    def get_frequent_element(self):
        """
        Задание: №7
        Номер задачи из задания: №11
        Краткое название: "Метод получения наиболее часто встречающегося элемента"
        Сложность: size - O(n)/time - O(n)

        Рефлексия:
            Самостоятельно решил задание.
            Мое решение получилось довольно близким к тому, которое приводилось в качестве решения.
        """
        if self.head is None:
            return None

        current_node = self.head
        max_val = self.head.value
        count_values = {}

        while current_node is not None:
            if count_values.get(current_node.value) is None:
                count_values[current_node.value] = 1
            else:
                count_values[current_node.value] += 1
            if count_values[max_val] < count_values[current_node.value]:
                max_val = current_node.value
            current_node = current_node.next
        return max_val


def join_two_sorted_lists(
    first_list: OrderedList, second_list: OrderedList, asc: bool
) -> OrderedList:
    """
    Задание: №7
    Номер задачи из задания: №9
    Краткое название: "Алгоритм слияния двух упорядоченных списков в один"
    Сложность: size - O(1)/time - O(n)

    Рефлексия:
        Решил самостоятельно без особых проблем.

    """
    result_list = OrderedList(asc=asc)

    left_node = first_list.head
    right_node = second_list.head

    while left_node or right_node:

        if left_node is None:
            result_list.add(right_node.value)
            right_node = right_node.next
            continue

        if right_node is None:
            result_list.add(left_node.value)
            left_node = left_node.next
            continue

        compare_res = result_list.compare(left_node.value, right_node.value)

        if compare_res == -1:
            result_list.add(left_node.value)
            left_node = left_node.next
            continue

        if compare_res in (0, 1):
            result_list.add(right_node.value)
            right_node = right_node.next
            continue

        assert False, (
            "Обнаружено не корректное состояние. "
            "Исполнение кода не должно было дойти до этого места."
        )

    return result_list
