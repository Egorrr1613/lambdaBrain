from ASD_FIRST.lesson_12_native_cache.native_cache import NativeCache


def test_native_cache_1():
    c = NativeCache(11)

    c.put(key="123", value="zzz")
    c.put(key="123", value="zzZ")

    assert c.get("123") == "zzZ"
    assert 1 in c.hits


def test_native_cache_2():
    c = NativeCache(11)

    c.put(key="123", value="zzz")
    index = c.__seek_slot__("123")
    assert c.hits[index] == 0
    c.get("123")
    assert c.hits[index] == 1

    c.put(key="124", value="zzz")
    c.get("124")
    c.put(key="125", value="zzz")
    c.get("125")
    c.put(key="126", value="zzz")
    c.get("126")
    c.put(key="127", value="zzz")
    c.get("127")
    c.put(key="128", value="zzz")
    c.get("128")
    c.put(key="129", value="zzz")
    c.get("129")
    c.put(key="129a", value="zzz")
    c.get("129a")
    c.put(key="129b", value="zzz")
    c.get("129b")
    c.put(key="129c", value="zzz")
    c.get("129c")
    c.put(key="129d", value="AAA")

    c.put(key="XXXX", value="new_data")

    assert c.get("129d") is None
    index = c.__seek_slot__("XXXX")
    assert c.hits[index] == 0

