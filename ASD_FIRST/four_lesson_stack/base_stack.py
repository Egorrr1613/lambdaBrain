from ASD_FIRST.three_lesson.dyn_array import DynArray
"""В динамическом массиве не реализованы методы для поиска элемента по индексу. """

from ASD_FIRST.two_lesson.one_dummy_node_list import LinkedList2
"""Не использую связный список, потому что в реализованном интерфейсе удаление доступно 
только для первого с головы элемента. Кажется что при текущем дизайне связного списка удобно 
внести удаление из хвоста, не обращаясь к "приватным" полям не получится.  """


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