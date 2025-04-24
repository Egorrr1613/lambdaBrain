import random
import time

from ASD_FIRST.lesson_10_set.set import PowerSet

COUNT_ELEMENT = 35_000

def get_set_with_random_data(count_el: int) -> PowerSet:
    s = PowerSet()
    for _ in range(count_el):
        s.put(str(random.randint(0, 50_000)))
    return s


def test_size():
    s = get_set_with_random_data(COUNT_ELEMENT)
    t1 = time.time()
    _ = s.size()
    t2 = time.time() - t1
    assert t2 < 2


def test_put():
    s = get_set_with_random_data(COUNT_ELEMENT)
    t1 = time.time()
    s.put('42')
    t2 = time.time() - t1
    assert t2 < 2


def test_get():
    s = get_set_with_random_data(COUNT_ELEMENT)
    s.put('42')
    t1 = time.time()
    s.get('42')
    t2 = time.time() - t1
    assert t2 < 2


def test_remove():
    s = get_set_with_random_data(COUNT_ELEMENT)
    s.put('42')
    t1 = time.time()
    s.remove('42')
    t2 = time.time() - t1
    assert t2 < 2


def test_intersection():
    s = get_set_with_random_data(COUNT_ELEMENT)
    s2 = get_set_with_random_data(COUNT_ELEMENT)

    for _ in range(30_000):
        s2.put(str(random.randint(0, 10_000_000)))
    t1 = time.time()
    s.intersection(s2)
    t2 = time.time() - t1
    assert t2 < 2


def test_union():
    s = get_set_with_random_data(COUNT_ELEMENT)
    s2 = get_set_with_random_data(COUNT_ELEMENT)

    t1 = time.time()
    s.union(s2)
    t2 = time.time() - t1
    assert t2 < 2


def test_difference():
    s = get_set_with_random_data(COUNT_ELEMENT)
    s2 = get_set_with_random_data(COUNT_ELEMENT)

    t1 = time.time()
    s.difference(s2)
    t2 = time.time() - t1
    assert t2 < 2


def test_issubset():
    s = get_set_with_random_data(COUNT_ELEMENT)
    s2 = get_set_with_random_data(COUNT_ELEMENT)

    t1 = time.time()
    s.issubset(s2)
    t2 = time.time() - t1
    assert t2 < 2
