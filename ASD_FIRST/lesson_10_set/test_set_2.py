from ASD_FIRST.lesson_10_set.set_2 import PowerSet, Bag


def test_decart_1():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")
    s1.put("789")

    s2 = PowerSet()
    s2.put("aa")
    s2.put("bb")

    s3 = s1.decart_product(s2)

    assert s3.size() == 6
    assert s3.get("123aa")
    assert s3.get("123bb")
    assert s3.get("456aa")
    assert s3.get("456bb")
    assert s3.get("789aa")
    assert s3.get("789bb")


def test_decart_2():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")
    s1.put("789")

    s2 = PowerSet()

    try:
        s1.decart_product(s2)
    except AssertionError:
        pass
    else:
        assert False, "Throw must be call"

    try:
        s2.decart_product(s1)
    except AssertionError:
        pass
    else:
        assert False, "Throw must be call"


def test_decart_3():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("z")

    s3 = s1.decart_product(s2)

    assert s3.size() == 2
    assert s3.get("123z")
    assert s3.get("456z")


def test_decart_4():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("z")
    s2.put("x")
    s2.put("c")

    s3 = s1.decart_product(s2)

    assert s3.size() == 6
    assert s3.get("123z")
    assert s3.get("456z")
    assert s3.get("123x")
    assert s3.get("456x")
    assert s3.get("123c")
    assert s3.get("456c")


def test_multi_intersection_1():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("z")
    s2.put("x")
    s2.put("c")

    s3 = PowerSet()
    s3.put("777")
    s3.put("888")

    s4 = s1.multi_intersection([s2, s3])

    assert s4.size() == 0


def test_multi_intersection_2():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("z")
    s2.put("x")
    s2.put("12")

    s3 = PowerSet()
    s3.put("777")
    s3.put("456")

    s4 = s1.multi_intersection([s2, s3])

    assert s4.size() == 0


def test_multi_intersection_3():
    s1 = PowerSet()
    s1.put("456")

    s2 = PowerSet()
    s2.put("456")

    s3 = PowerSet()
    s3.put("456")

    s4 = s1.multi_intersection([s2, s3])

    assert s4.size() == 1
    assert s4.get("456") is True


def test_multi_intersection_4():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("z")
    s2.put("x")
    s2.put("12")
    s2.put("456")

    s3 = PowerSet()
    s3.put("777")
    s3.put("456")

    s4 = s1.multi_intersection([s2, s3])

    assert s4.size() == 1
    assert s4.get("456") is True


def test_multi_intersection_5():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("123")
    s2.put("456")

    s3 = PowerSet()
    s3.put("123")
    s3.put("456")

    s4 = s1.multi_intersection([s2, s3])

    assert s4.size() == 2
    assert s4.get("123") is True
    assert s4.get("456") is True


def test_multi_intersection_6():
    s1 = PowerSet()
    s1.put("123")
    s1.put("456")

    s2 = PowerSet()
    s2.put("123")
    s2.put("456")

    s3 = s1.multi_intersection([s2])

    assert s3.size() == 2
    assert s3.get("123") is True
    assert s3.get("456") is True


def test_bug():
    b = Bag()

    b.put("123")
    assert b.get("123") is True
    assert b.count("123") == 1

    b.put("123")
    assert b.count("123") == 2

    b.put("123")
    assert b.count("123") == 3

    b.put("456")
    assert b.count("123") == 3
    assert b.size() == 4

    b.remove("123")
    assert b.count("123") == 2
    assert b.size() == 3

    b.remove("456")
    assert b.size() == 2
    assert b.count("123") == 2
    assert b.count("456") == 0

    b.remove("123")
    assert b.size() == 1
    assert b.count("123") == 1

    b.remove("123")
    assert b.size() == 0
    assert b.count("123") == 0
