from ASD_SECOND.lesson_7_heap.heap import Heap, get_max_by_index
from ASD_SECOND.lesson_7_heap.heap_2 import Heap as Heap_2


class TestMakeHeap:
    def test_empty_input_list(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[], depth=0)
        assert test_heap.HeapArray == [None]

    def test_empty_input_list_with_1_depth(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[], depth=1)
        assert test_heap.HeapArray == [None, None, None]

    def test_empty_input_list_with_2_depth(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[], depth=2)
        assert test_heap.HeapArray == 7 * [None]

    def test_non_empty_list_with_0_depth(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[1], depth=0)
        assert test_heap.HeapArray == [1]

    def test_non_empty_list_with_depth_and_one_el(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[1], depth=1)
        assert test_heap.HeapArray == [1, None, None]

    def test_non_empty_list_with_depth_and_two_el(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[1, 2], depth=1)
        assert test_heap.HeapArray == [2, 1, None]

    def test_non_empty_list_with_depth_and_3_el(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[1, 2, 3], depth=1)
        assert test_heap.HeapArray == [3, 1, 2]


class TestGetMax:
    def test_get_max_empty_heap(self) -> None:
        test_heap = Heap()
        assert test_heap.GetMax() == -1

    def test_non_empty_list_with_depth_and_3_el(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[1, 2, 3], depth=1)
        assert test_heap.GetMax() == 3

        assert test_heap.HeapArray == [2, 1, None]


class TestGetMaxByIndex:
    def test_get_max_1(self) -> None:
        assert get_max_by_index(input_list=[0, 1], first_index=0, second_index=1) == 1

    def test_get_max_2(self) -> None:
        assert get_max_by_index(input_list=[2, 1], first_index=0, second_index=1) == 0

    def test_get_max_all_none(self) -> None:
        assert get_max_by_index(input_list=[None, None], first_index=0, second_index=1) == -1

    def test_get_max_first_none(self) -> None:
        assert get_max_by_index(input_list=[None, 1], first_index=0, second_index=1) == 1

    def test_get_max_second_none(self) -> None:
        assert get_max_by_index(input_list=[1, None], first_index=0, second_index=1) == 0

    def test_get_max_out_first(self) -> None:
        assert get_max_by_index(input_list=[0, -1], first_index=2, second_index=1) == 1

    def test_get_max_out_second(self) -> None:
        assert get_max_by_index(input_list=[0, 1], first_index=0, second_index=2) == 0

    def test_get_max_out_all(self) -> None:
        assert get_max_by_index(input_list=[0, 1], first_index=2, second_index=3) == -1


class TestCheckCorrectHeap:
    def test_empty_heap(self) -> None:
        test_heap = Heap()
        assert test_heap.is_correct_heap()

    def test_one_node_after_add_heap(self) -> None:
        test_heap = Heap()
        test_heap.Add(key=5)
        assert test_heap.HeapArray == []
        assert test_heap.is_correct_heap()

    def test_check_after_correct_make_one_el(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[], depth=0)
        assert test_heap.HeapArray == [None]
        assert test_heap.is_correct_heap()

        assert test_heap.Add(5)
        assert test_heap.is_correct_heap()

    def test_check_after_correct_make_two_el(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[], depth=1)
        assert test_heap.is_correct_heap()

        assert test_heap.Add(5)
        assert test_heap.Add(6)
        assert test_heap.is_correct_heap()

    def test_check_after_correct_make_three_el(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[], depth=1)
        assert test_heap.is_correct_heap()

        assert test_heap.Add(5)
        assert test_heap.Add(6)
        assert test_heap.Add(7)
        assert test_heap.is_correct_heap()

    def test_check_incorrect_root_in_heap_one_depth(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[1, 2, 3], depth=1)

        test_heap.HeapArray[0] = 0
        assert not test_heap.is_correct_heap()

    def test_check_incorrect_left_child_in_heap_one_depth(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[1, 2, 3], depth=1)

        test_heap.HeapArray[1] = 5
        assert not test_heap.is_correct_heap()

    def test_check_incorrect_right_child_in_heap_one_depth(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[1, 2, 3], depth=1)

        test_heap.HeapArray[2] = 5
        assert not test_heap.is_correct_heap()


class TestAdd:
    def test_base_add_in_zero_dept(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[], depth=0)

        assert test_heap.HeapArray == [None]
        assert test_heap.Add(55)
        assert test_heap.HeapArray == [55]

        assert not test_heap.Add(66)
        assert test_heap.HeapArray == [55]

    def test_base_add(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[10, 66, 100], depth=1)

        assert test_heap.HeapArray == [100, 10, 66]
        assert not test_heap.Add(55)
        assert test_heap.HeapArray == [100, 10, 66]

    def test_base_add_2(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[10, 100], depth=1)

        assert test_heap.HeapArray == [100, 10, None]
        assert test_heap.Add(55)
        assert test_heap.HeapArray == [100, 10, 55]

    def test_base_add_3(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[10, 100], depth=1)

        assert test_heap.HeapArray == [100, 10, None]
        assert test_heap.Add(5)
        assert test_heap.HeapArray == [100, 10, 5]

    def test_add_and_rebuild_heap(self) -> None:
        test_heap = Heap()
        test_heap.MakeHeap(input_list=[10, 66, 100], depth=2)

        assert test_heap.HeapArray == [100, 10, 66, None, None, None, None]
        assert test_heap.Add(55)
        assert test_heap.HeapArray == [100, 55, 66, 10, None, None, None]


class TestFindMaxInRange:
    def test_base_get_max_range_0(self) -> None:
        test_heap = Heap_2()
        test_heap.MakeHeap(input_list=[10], depth=0)

        assert test_heap.find_max_el_in_range(min_range=5, max_range=11) == 0
        assert test_heap.find_max_el_in_range(min_range=8, max_range=9) == -1

    def test_base_get_max_range_1(self) -> None:
        test_heap = Heap_2()
        test_heap.MakeHeap(input_list=[10, 66, 100], depth=1)

        assert test_heap.find_max_el_in_range(min_range=5, max_range=11) == 1
        assert test_heap.find_max_el_in_range(min_range=10, max_range=10) == 1

        assert test_heap.find_max_el_in_range(min_range=50, max_range=67) == 2
        assert test_heap.find_max_el_in_range(min_range=66, max_range=66) == 2

        assert test_heap.find_max_el_in_range(min_range=90, max_range=101) == 0


class TestMergeHeap:
    def test_empty_heap_merge(self) -> None:
        test_heap = Heap_2()
        test_heap.MakeHeap(input_list=[], depth=0)

        test_heap_2 = Heap_2()
        test_heap_2.MakeHeap(input_list=[], depth=0)

        test_heap.merge_heap(test_heap_2)

        assert test_heap.HeapArray == [None]
        assert test_heap.is_correct_heap()

    def test_empty_and_not_empty_heap_merge(self) -> None:
        test_heap = Heap_2()
        test_heap.MakeHeap(input_list=[], depth=0)

        test_heap_2 = Heap_2()
        test_heap_2.MakeHeap(input_list=[1, 2, 3], depth=1)

        test_heap.merge_heap(test_heap_2)

        assert test_heap.HeapArray == [3]
        assert test_heap.is_correct_heap()

    def test_not_empty_and_empty_heap_merge(self) -> None:
        test_heap = Heap_2()
        test_heap.MakeHeap(input_list=[1, 2, 3], depth=1)

        test_heap_2 = Heap_2()
        test_heap_2.MakeHeap(input_list=[], depth=0)

        test_heap.merge_heap(test_heap_2)

        assert test_heap.HeapArray == [3, 1, 2]
        assert test_heap.is_correct_heap()

    def test_base_merge(self) -> None:
        test_heap = Heap_2()
        test_heap.MakeHeap(input_list=[10, 66, 100], depth=2)

        test_heap_2 = Heap_2()
        test_heap_2.MakeHeap(input_list=[15, 77, 99], depth=1)

        test_heap.merge_heap(heap_to_merge=test_heap_2)

        assert test_heap.is_correct_heap()
        assert test_heap.HeapArray == [100, 99, 66, 10, 77, 15, None]

    def test_merge_big_heap(self) -> None:
        test_heap = Heap_2()
        test_heap.MakeHeap(input_list=[1, 2, 3], depth=2)

        test_heap_2 = Heap_2()
        test_heap_2.MakeHeap(input_list=[99, 98, 97, 96, 95, 94, 93], depth=2)

        test_heap.merge_heap(test_heap_2)

        assert test_heap.HeapArray == [99, 98, 97, 1, 3, 2, 96]
        assert test_heap.is_correct_heap()
