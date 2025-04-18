from ASD_FIRST.eight_hash_table.hash_table_2 import DynHashTable


def test_dyn_hash_table():
    dh = DynHashTable()

    dh.put("123")

    assert dh.find("123") == 6
    assert dh.find("124") is None


def test_dyn_hash_table_resize():
    dh = DynHashTable()

    dh.put("123")
    dh.put("1234")
    dh.put("1233afa4")
    dh.put("1232asfasf123")
    dh.put("12312asfasf25")
    dh.put("aasfsa")
    dh.put("casfasf")
    dh.put("vasf")
    dh.put("basf")
    dh.put("xafasf")
    dh.put("xafasasdfff")
    dh.put("21")

    assert dh.find("123") == 22
    assert dh.find("124") is None




