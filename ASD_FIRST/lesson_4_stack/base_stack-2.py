from ASD_FIRST.lesson_4_stack.base_stack import Stack


def is_balance(input_str: str):
    """
    Задание: №4
    Номер задачи из задания: №5/6
    Краткое название: "Функция для определения сбалансирована ли строка из скобок: (), {}, []"
    Сложность: size - O(n)/time - O(n)

    Рефлексия: Задание решил без особых проблем,
        самостоятельно реализовал алгоритм очень близкий к тому
        который приводится в качестве рекомендованного решения.
    """
    stack = Stack()
    reverse_symbol = {")": "(", "}": "{", "]": "["}
    for i in input_str:
        if i in ["(", "{", "["]:
            stack.push(i)
            continue
        if i in [")", "}", "]"] and stack.size() > 0:
            rm_symbol = stack.pop()
            if rm_symbol != reverse_symbol[i]:
                return False
            continue
        return False

    if stack.size() == 0:
        return True
    return False


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self, v):
        super().__init__(v)


class ExpandedStack:
    def __init__(self):
        self.head = DummyNode(None)
        self.tail = self.head

        self.head.next = self.tail
        self.head.prev = self.tail

        self.count_node = 0
        self.min_stack = Stack()
        self.__all_elements_sum__ = 0

    def push(self, value) -> None:
        new_node = Node(value)

        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.count_node += 1
        if isinstance(value, (int, float)):
            self.__all_elements_sum__ += value

        if self.count_node == 1:
            self.min_stack.push(value)
            return

        if value <= self.min_stack.peek():
            self.min_stack.push(value)

    def size(self):
        return self.count_node

    def pop(self):
        if self.count_node == 0:
            return None
        value = self.head.prev.value

        self.head.prev = self.head.prev.prev

        self.count_node -= 1
        if isinstance(value, (int, float)):
            self.__all_elements_sum__ -= value

        if self.min_stack.peek() == value:
            self.min_stack.pop()

        return value

    def peek(self):
        if self.count_node == 0:
            return None
        return self.head.next.value

    def get_min_el(self):
        """
        Задание: №4
        Номер задачи из задания: №7
        Краткое название: "Метод для получения минимального элемента за О(1)"
        Сложность: size - O(1)/time - O(1)

        Рефлексия: Подсказка для решения задания приводится уже в условии: явно предлагается использовать второй стек.
            Самостоятельно понял, что во втором стеке можно хранить набор "минимумов".
            Дальнейшая реализация не составила проблем.
        """
        if self.count_node == 0:
            return None
        return self.min_stack.peek()

    def get_avg(self):
        """
        Задание: №4
        Номер задачи из задания: №8
        Краткое название: "Метод для получения среднего значения всех элементов стека за О(1)"
        Сложность: size - O(1)/time - O(1)

        Рефлексия: По аналогии с 7 задачей сразу появилась идея хранить в стеке дополнительную информацию,
            чтобы потом с минимальной сложностью произвести нужные расчеты. В итоге моя догадка совпала с
            рекомендуемым решением.
        """
        if self.count_node == 0:
            return 0
        return self.__all_elements_sum__ // self.count_node


def calculate_math_expression(stack_with_math_expression: ExpandedStack):
    """
    Задание: №4
    Номер задачи из задания: №9
    Краткое название: "Метод расчета постфиксных выражений"
    Сложность: size - O(n)/time - O(n)

    Рефлексия: Самостоятельно решил задание, избежав ошибки записи двух аргументов в одной строке.
        Однако допустил копипаст операций. После ознакомления с вашими рекомендациями вынес операции над числами
        как лямбды, в отдельный словарь.
        Получилась такая строка: number_stack.push(math_operation[ch](int(a), int(b)))
        Такой прием мне показался крайне удобным и красивым.
        Запомнил его, в дальнейшем буду применять в своем коде.
    """
    number_stack = Stack()

    math_symbol = "+-*="
    math_operation = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }

    for _ in range(stack_with_math_expression.size()):
        ch = stack_with_math_expression.pop()
        if str.isdigit(ch):
            number_stack.push(ch)
            continue

        if ch not in math_symbol:
            return (f"Error, incorrect data in math operation: {ch}",)

        if ch == "=":
            return int(number_stack.pop())

        if number_stack.size() < 2:
            return (
                f"Error, incorrect number_stack size."
                f"For correct calculations there must be more than 1 element in the number_stack."
                f"Current number_stack size: {number_stack.size()}",
            )

        a = number_stack.pop()
        b = number_stack.pop()

        number_stack.push(math_operation[ch](int(a), int(b)))

    return int(number_stack.pop())
