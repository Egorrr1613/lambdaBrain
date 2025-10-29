"""
Задание: №5
Номер задачи из задания: №2
Краткое название: "Сравнение поиска узла в aBST и классическом дереве с узлами"

Ответ:
Кажется что сложность по времени и при поиске по узлам и при поиске по массиву будет одинакова,
    так как и там и там используется алгоритм бинарного поиска.

По памяти в худшем случае сложность так же одинакова - и там и там O(N).
Однако думаю что сложность по памяти в среднем случае будет хуже у поиска по массиву - o(N),
    тогда как у поиска по нодам o(log N).

    В случае с поиском по массиву требуется хранить в памяти весь массив.
    Тогда как в случае поиска по нодам у нас в памяти хранится только стек рекурсии.

Однако поиск по массиву дает существенное преимущество, если мы уже знаем индекс элемента.
В таком случае сложность составляет O(1),
    что может являться критическим преимуществом в каких либо специфических случаях.
"""
from ASD_SECOND.lesson_5_restore_aBST.gen_abst import _recursion_generate_tree


def delete_element(binary_search_tree_list: list[int], key_to_delete: int) -> list[int | None] | None:
    """
    Задание: №5
    Номер задачи из задания: №3
    Краткое название: "Удаление узла из BST с ребалансировкой"
    Сложность: - size - O(n) / time - O(n)

    Рефлексия:

    """
    if key_to_delete not in binary_search_tree_list:
        return None

    copy_bin_tree = binary_search_tree_list[:]
    index_to_delete = binary_search_tree_list.index(key_to_delete)
    len_tree = len(binary_search_tree_list)

    copy_bin_tree.pop(index_to_delete)
    copy_bin_tree = [node for node in copy_bin_tree if node]

    copy_bin_tree.sort()

    new_tree_list: list[int | None] = [None] * len_tree

    _recursion_generate_tree(sorted_list=copy_bin_tree, list_to_tree=new_tree_list,
                             len_tree=len(copy_bin_tree), current_index_in_tree=0)

    return new_tree_list


"""
Задание: №5
Номер задачи из задания: №4
Краткое название: "Как отсортировать двоичное дерево за O(1) по времени"
Ответ: BST уже является отсортированной структурой данных, 
    так как левый и правый потомки каждого узла распределяются в дереве согласно результату сравнения.
    Повторная сортировка не имеет смысла.

Рефлексия:

"""

