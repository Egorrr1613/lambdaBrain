from ASD_FIRST.three_lesson.dyn_array import DynArray


class Stack:
    def __init__(self):
        self.stack = DynArray()

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        result = self.stack[self.size() - 1]
        self.stack.delete(self.size() - 1)

        return result

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[self.size() - 1]

