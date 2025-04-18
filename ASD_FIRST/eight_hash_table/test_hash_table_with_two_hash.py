from ASD_FIRST.eight_hash_table.hash_table import HashTable
from ASD_FIRST.eight_hash_table.hash_table_2 import HashTableTwoHash

import random
import string

HASH_TABLE_SIZE = 101


def generate_random_strings(n, min_length=1, max_length=10):
    """
    Генерирует n строк случайной длины.
    """
    random_strings = []
    for _ in range(n):
        length = random.randint(min_length, max_length)
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        random_strings.append(random_str)
    return random_strings


def test_compare_hash_tables():
    """
    Тест создает 2 хеш таблицы и сравнивает количество коллизий между ними
        при случайном наборе генерируемых входных данных
    """
    random_str_list = generate_random_strings(HASH_TABLE_SIZE)
    index_list_1 = []
    index_list_2 = []

    hash_t = HashTable(sz=HASH_TABLE_SIZE, stp=3)
    hash_t_with_two_hash = HashTableTwoHash(sz=HASH_TABLE_SIZE)

    for random_str_index in range(HASH_TABLE_SIZE):
        index_list_1.append(hash_t.put(random_str_list[random_str_index]))
        index_list_2.append(hash_t_with_two_hash.put(random_str_list[random_str_index]))

    count_none_1 = index_list_1.count(None)
    count_none_2 = index_list_2.count(None)

    print(f"\nКоличество коллизий в исходной хеш таблице: {hash_t.collision_count}\n"
          f"Количество НЕ вставленных объектов: {count_none_1}\n"
          f"Количество коллизий в таблице с двумя хеш функциями: {hash_t_with_two_hash.collision_count}\n"
          f"Количество НЕ вставленных объектов: {count_none_2}\n")
