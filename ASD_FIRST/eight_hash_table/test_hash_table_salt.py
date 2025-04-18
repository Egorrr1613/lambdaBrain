from ASD_FIRST.eight_hash_table.hash_table_2 import HashTableWithSalt


def test_ddos_salt_table():
    """Заполняем хеш таблицу значениями, для которых хеш сумма равна одному и тому же числу (1)"""
    hash_t = HashTableWithSalt(sz=17, stp=3)

    assert hash_t.put('4') == 1
    assert hash_t.put('43') == 4
    assert hash_t.put('433') == 7
    assert hash_t.put('4333') == 10
    assert hash_t.put('43333') == 13
    assert hash_t.put('433333') == 16
    assert hash_t.put('4333333') is None