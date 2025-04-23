from ASD_FIRST.lesson_10_set.set import PowerSet


def test_set_put():
    s = PowerSet()
    assert s.size() == 0
    assert s.get("123") is False

    s.put("123")
    assert s.get("123") is True
    assert s.size() == 1

    s.put("123")
    assert s.get("123") is True
    assert s.size() == 1


def test_set_remove():
    s = PowerSet()
    s.put("123")

    s.remove("123")
    assert s.get("123") is False
    assert s.size() == 0

    s.remove("1234")
    assert s.get("1234") is False
    assert s.size() == 0


def test_intersection_1():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("123")
    s2.put("567")

    s3 = s1.intersection(s2)
    assert s3.size() == 1
    assert s3.get("123")


def test_intersection_2():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("467")
    s2.put("567")

    s3 = s1.intersection(s2)
    assert s3.size() == 0


def test_union_1():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("789")
    s2.put("987")

    s3 = s1.union(s2)
    assert s3.size() == 4
    assert s3.get("123")
    assert s3.get("456")
    assert s3.get("789")
    assert s3.get("987")


def test_union_2():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()

    s3 = s1.union(s2)
    assert s3.size() == 2
    assert s3.get("123")
    assert s3.get("456")


def test_difference_1():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("123")
    s2.put("456")

    s3 = s1.difference(s2)
    assert s3.size() == 0


def test_difference_2():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("123")
    s2.put("987")

    s3 = s1.difference(s2)
    assert s3.size() == 1
    assert s3.get("456")


def test_issubset_1():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")
    s1.put("789")

    s2 = PowerSet()
    s2.put("123")
    s2.put("789")

    assert s1.issubset(s2)


def test_issubset_2():
    s1 = PowerSet()
    s1.put("123")
    s1.put("789")

    s2 = PowerSet()
    s2.put("123")
    s2.put("456")
    s2.put("789")

    assert s1.issubset(s2) is False


def test_issubset_3():
    s1 = PowerSet()
    s1.put("123")
    s1.put("789")

    s2 = PowerSet()

    assert s1.issubset(s2)


def test_issubset_4():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")
    s1.put("789")

    s2 = PowerSet()
    s2.put("123")
    s2.put("456")
    s2.put("789")

    assert s1.issubset(s2)


def test_equals_1():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")
    s1.put("789")

    s2 = PowerSet()
    s2.put("123")
    s2.put("456")
    s2.put("789")

    assert s1.equals(s2)


def test_equals_2():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")
    s1.put("789")

    s2 = PowerSet()

    assert s1.equals(s2) is False


def test_equals_3():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")
    s1.put("789")

    s2 = PowerSet()
    s2.put("123")
    s2.put("789")

    assert s1.equals(s2) is False
