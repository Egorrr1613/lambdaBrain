from ASD_FIRST.four_lesson_stack.base_stack import Stack


def is_balance(input_str: str):
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
        self.__element_sum__ = 0

    def push(self, value) -> None:
        new_node = Node(value)

        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.count_node += 1
        if isinstance(value, (int, float)):
            self.__element_sum__ += value

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
            self.__element_sum__ -= value

        if self.min_stack.peek() == value:
            self.min_stack.pop()

        return value

    def peek(self):
        if self.count_node == 0:
            return None
        return self.head.next.value

    def get_min_el(self):
        """Решение 7 дополнительного задания"""
        if self.count_node == 0:
            return None
        return self.min_stack.peek()

    def get_avg(self):
        """Решение 8 дополнительного задания"""
        if self.count_node == 0:
            return 0
        return self.__element_sum__ // self.count_node


def calculate_math_expression(stack_with_math_expression: ExpandedStack):
    """Решение 9 дополнительного задания"""
    number_stack = ExpandedStack()

    math_symbol = "+-*="

    for _ in range(stack_with_math_expression.size()):
        ch = stack_with_math_expression.pop()
        if str.isdigit(ch):
            number_stack.push(ch)
            continue

        if ch not in math_symbol:
            return ("Error",)

        a = number_stack.pop()
        b = number_stack.pop()

        if ch == "+":
            number_stack.push(str(int(a) + int(b)))
            continue

        if ch == "*":
            number_stack.push(str(int(a) * int(b)))
            continue

        if ch == "-":
            number_stack.push(str(int(a) - int(b)))
            continue

        if ch == "=":
            return int(a)

    return int(number_stack.pop())

