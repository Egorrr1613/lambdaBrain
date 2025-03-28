from ASD_FIRST.eight_hash_table.hash_table import HashTable


def test_hash_table_hash_fun():
    hash_t = HashTable(sz=17, stp=3)

    assert hash_t.hash_fun('w') == 0
    assert hash_t.hash_fun('ab') == 8
    assert hash_t.hash_fun('1') == 15
    assert hash_t.hash_fun('zzzzzzzzzzz') == 16

    assert hash_t.hash_fun('a') == 12
    assert hash_t.hash_fun('99') == 12
    assert hash_t.hash_fun('211') == 12
    assert hash_t.hash_fun('124123') == 12
    assert hash_t.hash_fun('yyyyyy') == 12


def test_seek_index():
    hash_t = HashTable(sz=17, stp=3)

    assert hash_t.seek_slot('a') == 12
    hash_t.put('a')
    assert hash_t.seek_slot('a') == 12

    assert hash_t.seek_slot('99') == 15
    hash_t.put('99')
    assert hash_t.seek_slot('99') == 15

    assert hash_t.seek_slot('124123') == 1
    hash_t.put('124123')
    assert hash_t.seek_slot('124123') == 1

    assert hash_t.seek_slot('yyyyyy') == 4
    hash_t.put('yyyyyy')
    assert hash_t.seek_slot('yyyyyy') == 4

    assert hash_t.seek_slot('211') == 7
    hash_t.put('211')
    assert hash_t.seek_slot('211') == 7

    assert hash_t.seek_slot('w') == 0
    hash_t.put('w')
    assert hash_t.seek_slot('w') == 0

    assert hash_t.seek_slot('ww') == 3
    hash_t.put('ww')
    assert hash_t.seek_slot('ww') == 3

    assert hash_t.seek_slot('www') == 6
    hash_t.put('www')
    assert hash_t.seek_slot('www') == 6

    assert hash_t.seek_slot('wwww') == 9
    hash_t.put('wwww')
    assert hash_t.seek_slot('wwww') == 9

    assert hash_t.seek_slot('wwwww') is None


def test_put_1():
    hash_t = HashTable(sz=17, stp=3)

    assert hash_t.put('w') == 0
    assert hash_t.put('227') == 2
    assert hash_t.put('227') == 2
    assert hash_t.put('a') == 12
    assert hash_t.put('a') == 12
    assert hash_t.put('99') == 15
    assert hash_t.put('zzzzzzzzzzz') == 16


def test_put_2():
    """Заполняем хеш таблицу значениями, для которых хеш сумма равна одному и тому же числу (1)"""
    hash_t = HashTable(sz=17, stp=3)

    assert hash_t.put('4') == 1
    assert hash_t.put('43') == 4
    assert hash_t.put('433') == 7
    assert hash_t.put('4333') == 10
    assert hash_t.put('43333') == 13
    assert hash_t.put('433333') == 16
    assert hash_t.put('4333333') is None


def test_find():
    hash_t = HashTable(sz=17, stp=3)

    hash_t.put('w')
    hash_t.put('a')
    hash_t.put('99')
    hash_t.put('124123')
    hash_t.put('214')

    assert hash_t.find('w') == 0
    assert hash_t.find('a') == 12
    assert hash_t.find('99') == 15
    assert hash_t.find('124123') == 1
    assert hash_t.find('214') == 4
    assert hash_t.find('211') is None
