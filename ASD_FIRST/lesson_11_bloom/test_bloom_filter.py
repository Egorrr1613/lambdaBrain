from ASD_FIRST.lesson_11_bloom.bloom_filter import BloomFilter


def test_empty_bloom():
    bloom_filter = BloomFilter(32)
    assert not bloom_filter.is_value("124")


def test_bloom_hash_func():
    bloom_filter = BloomFilter(32)
    assert bin(bloom_filter.hash1("123")) == '0b10000000000000000000000'
    assert bin(bloom_filter.hash2("123")) == '0b1000000000000000000'


def test_add():
    bloom_filter = BloomFilter(32)
    bloom_filter.add("123")

    assert bloom_filter.is_value("123")
    assert not bloom_filter.is_value("124")
    assert not bloom_filter.is_value("122")


def test_filter_state_1():
    bloom_filter = BloomFilter(32)
    bloom_filter.add("123")
    assert bin(bloom_filter.byte_array) == '0b10001000000000000000000'

    bloom_filter.add("123")
    assert bin(bloom_filter.byte_array) == '0b10001000000000000000000'


def test_filter_state_2():
    bloom_filter = BloomFilter(32)
    bloom_filter.add("123")
    bloom_filter.add("567")
    bloom_filter.add("123213123")
    assert bin(bloom_filter.byte_array) == '0b10001010000000000000100'


def test_add_2():
    bloom_filter = BloomFilter(32)
    bloom_filter.add("0123456789")
    bloom_filter.add("1234567890")
    bloom_filter.add("2345678901")
    bloom_filter.add("3456789012")
    bloom_filter.add("4567890123")
    bloom_filter.add("5678901234")
    bloom_filter.add("6789012345")
    bloom_filter.add("7890123456")
    bloom_filter.add("8901234567")
    bloom_filter.add("9012345678")
    bloom_filter.add("0123456789")

    assert bin(bloom_filter.byte_array) == '0b101000000000000010000000100000'
    assert bloom_filter.is_value("0123456789")
    assert not bloom_filter.is_value("1123456789")


def test_add_3():
    bloom_filter = BloomFilter(32)
    bloom_filter.add("0123456789")
    assert bloom_filter.is_value("0123456789")
    assert bloom_filter.is_value("8901234567")  # коллизия

    bloom_filter.add("9012345678")
    bloom_filter.add("8901234567")
    assert bloom_filter.is_value("8901234567")

    bloom_filter.add("7890123456")
    bloom_filter.add("6789012345")
    bloom_filter.add("5678901234")
    bloom_filter.add("4567890123")
    bloom_filter.add("3456789012")
    bloom_filter.add("2345678901")
    bloom_filter.add("1234567890")

    assert not bloom_filter.is_value("124")
    assert not bloom_filter.is_value("122")
