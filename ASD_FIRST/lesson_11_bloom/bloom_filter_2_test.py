from ASD_FIRST.lesson_11_bloom.bloom_filter_2 import sum_any_blume, index_el_to_unicode_char
from ASD_FIRST.lesson_11_bloom.bloom_filter_2 import decode_bloom_filter
from ASD_FIRST.lesson_11_bloom.bloom_filter_2 import BloomFilterWithDelete
from ASD_FIRST.lesson_11_bloom.bloom_filter import BloomFilter


def test_sum_any_blume():
    v1 = "123"
    b1 = BloomFilter(32)
    b1.add(v1)

    v2 = "12312"
    b2 = BloomFilter(32)
    b2.add(v2)

    v3 = "zxczxczxc"
    b3 = BloomFilter(32)
    b3.add(v3)

    b4 = sum_any_blume([b1, b2, b3])

    assert b4.is_value(v1)
    assert b4.is_value(v2)
    assert b4.is_value(v3)


def test_bloom_filter_delete_1():
    bloom_filter = BloomFilterWithDelete(32)
    bloom_filter.add("123")

    assert list(bloom_filter.byte_array) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                             0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert bloom_filter.delete("123")
    assert list(bloom_filter.byte_array) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert not bloom_filter.delete("777")


def test_bloom_filter_delete_2():
    bloom_filter = BloomFilterWithDelete(32)

    bloom_filter.add("0123456789")
    bloom_filter.add("1234567890")
    assert list(bloom_filter.byte_array) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]

    bloom_filter.add("2345678901")
    assert list(bloom_filter.byte_array) == [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0,
                                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
    bloom_filter.add("3456789012")
    bloom_filter.add("4567890123")
    bloom_filter.add("5678901234")
    bloom_filter.add("6789012345")
    bloom_filter.add("7890123456")
    bloom_filter.add("8901234567")
    bloom_filter.add("9012345678")
    bloom_filter.add("0123456789")
    assert list(bloom_filter.byte_array) == [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0,
                                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0]


def test_bloom_filter_delete_3():
    test_value = "0123456789"
    collision_value = "8901234567"
    bloom_filter = BloomFilterWithDelete(32)

    bloom_filter.add(test_value)
    assert bloom_filter.is_value(test_value)
    assert bloom_filter.is_value(collision_value), "Для коллизии ожидается ложно положительное срабатывание проверки на наличие в структуре"
    assert bloom_filter.delete(collision_value), "Удаление элемента, являющегося коллизией должно быть успешно выполнено"
    assert not bloom_filter.is_value(test_value), "После удаления коллизии оригинальный элемент должен отсутствовать"

def test_index_el_to_unicode_char_test():
    assert index_el_to_unicode_char(index=0, len_final_str=2, char_set_size=3, end_unicode_index=123) == [0, 0]
    assert index_el_to_unicode_char(index=1, len_final_str=2, char_set_size=3, end_unicode_index=123) == [0, 1]
    assert index_el_to_unicode_char(index=2, len_final_str=2, char_set_size=3, end_unicode_index=123) == [0, 2]
    assert index_el_to_unicode_char(index=3, len_final_str=2, char_set_size=3, end_unicode_index=123) == [1, 0]
    assert index_el_to_unicode_char(index=5, len_final_str=2, char_set_size=3, end_unicode_index=123) == [1, 2]


def test_bloom_filter_decode_data():
    b = BloomFilter(32)
    b.add("3")

    decoded_data = decode_bloom_filter(b_filter=b, expected_data_len=1)
    assert "3" in decoded_data


def test_bloom_filter_decode_data_2():
    b = BloomFilter(32)
    b.add("33")

    decoded_data = decode_bloom_filter(b_filter=b, expected_data_len=2)
    assert "33" in decoded_data