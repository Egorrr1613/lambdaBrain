from ASD_FIRST.lesson_9_associate_list.native_dict_2 import NativeDictionaryBySortedList, NativeDictionaryByByteKeys, \
    EmptySlot


def test_native_dict_by_sort_list():
    n = NativeDictionaryBySortedList()
    n.put(key="asd", value=1231233)
    assert len(n) == 1
    assert n.find("asd") == 1231233

    n.put(key="asdddd", value=14)
    assert n.find("asdddd") == 14

    assert n.find("xxx") is None

    n.put(key="asdddd", value=99)
    assert n.find("asdddd") == 99

    n.delete(key="asdddd")

    assert n.find("asdddd") is None


def test_native_dictionary_by_byte_keys():
    n = NativeDictionaryByByteKeys()

    n.put(key='0b01110', value='abc')
    assert n.find(key='0b01110') == 'abc'

    n.put(key='0b01110', value='abd')
    assert n.find(key='0b01110') == 'abd'

    n.delete('0b01110')
    assert isinstance(n.find(key='0b01110'), EmptySlot)
