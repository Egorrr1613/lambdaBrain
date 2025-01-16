import ctypes

import pytest


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError("Incorrect index")
        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        for i_range in range(self.count, i, -1):
            self.array[i_range] = self.array[i_range - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        self.__getitem__(i)

        if (self.capacity > 16) and (self.count - 1 < self.capacity // 2):
            self.capacity = max(16, int(self.capacity / 1.5))

        for loop_i in range(i, self.count - 1):
            self.array[loop_i] = self.array[loop_i + 1]

        self.count -= 1
        self.resize(self.capacity)

    def get_list_elements(self):
        return list(self.array._objects.values())


def prepare_test_data(len_array: int) -> DynArray:
    da = DynArray()
    for i in range(len_array):
        da.append(i)
    return da


def test_insert():
    da = prepare_test_data(len_array=8)
    da.insert(i=4, itm=99)

    assert len(da) == 9
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 1, 2, 3, 99, 4, 5, 6, 7]


def test_insert_resize():
    da = prepare_test_data(len_array=15)
    da.insert(i=4, itm=15)
    da.insert(i=4, itm=16)
    da.insert(i=4, itm=17)
    da.insert(i=4, itm=18)
    da.insert(i=4, itm=19)

    assert len(da) == 20
    assert da.capacity == 32
    assert da.get_list_elements() == [
        0,
        1,
        2,
        3,
        19,
        18,
        17,
        16,
        15,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ]


def test_insert_incorrect_index():
    da = prepare_test_data(len_array=2)
    with pytest.raises(IndexError):
        da.insert(i=-1, itm=99)

    with pytest.raises(IndexError):
        da.insert(i=3, itm=99)

    assert len(da) == 2
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 1]


def test_insert_bound_index():
    da = prepare_test_data(len_array=2)
    da.insert(i=0, itm=99)
    da.insert(i=2, itm=98)

    assert len(da) == 4
    assert da.capacity == 16
    assert da.get_list_elements() == [99, 0, 98, 1]


def test_insert_to_empty_list():
    da = DynArray()

    da.insert(i=0, itm=99)
    assert len(da) == 1
    assert da.capacity == 16
    assert da.get_list_elements() == [99]

    da.insert(i=1, itm=98)
    assert len(da) == 2
    assert da.capacity == 16
    assert da.get_list_elements() == [99, 98]


def test_delete():
    da = prepare_test_data(3)
    da.delete(1)

    assert len(da) == 2
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 2]


def test_delete_empty_array():
    da = DynArray()
    with pytest.raises(IndexError):
        da.delete(0)

    assert len(da) == 0
    assert da.capacity == 16
    assert da.array._objects is None


def test_delete_incorrect_index():
    da = prepare_test_data(9)
    with pytest.raises(IndexError):
        da.delete(14)

    assert len(da) == 9
    assert da.capacity == 16


def test_delete_resize():
    da = prepare_test_data(len_array=17)
    assert len(da) == 17
    assert da.capacity == 32

    da.delete(8)
    assert len(da) == 16
    assert da.capacity == 32

    da.delete(8)
    assert len(da) == 15
    assert da.capacity == 21

    for _ in range(4):
        da.delete(1)
    assert len(da) == 11
    assert da.capacity == 21

    da.delete(1)
    assert len(da) == 10
    assert da.capacity == 21

    da.delete(1)
    assert len(da) == 9
    assert da.capacity == 16
    assert da.get_list_elements() == [0, 7, 10, 11, 12, 13, 14, 15, 16]
