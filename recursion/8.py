import os


def find_files(
    current_dir: str,
    count_files: list,
    not_check_file_and_dir_in_current_dir: list,
    deep_storage: list,
) -> list:
    # Если не проверенных объектов = 0 и размер deep_storage = 0 (начальная точка)
    # Значит все обошли, возвращаем кол-во файлов
    if len(not_check_file_and_dir_in_current_dir) == 0 and len(deep_storage) == 0:
        return count_files

    # Если не проверенных объектов = 0 и размер deep_storage > 1
    # Значит на этом уровне все проверено, возвращаемся на директорию выше
    if len(not_check_file_and_dir_in_current_dir) == 0 and len(deep_storage) > 0:
        dir_to_rec = os.path.join(current_dir, "..")
        list_to_rec = deep_storage.pop()

    # Если не проверенных объектов больше чем 0 и очередной объект это файл - то ...
    if len(not_check_file_and_dir_in_current_dir) > 0 and os.path.isfile(
        os.path.join(current_dir, not_check_file_and_dir_in_current_dir[0])
    ):
        count_files.append(not_check_file_and_dir_in_current_dir.pop(0))

        dir_to_rec = current_dir
        list_to_rec = not_check_file_and_dir_in_current_dir

    # Если не проверенных объектов больше чем 0 и очередной объект это директория - то ...
    elif len(not_check_file_and_dir_in_current_dir) > 0 and os.path.isdir(
        os.path.join(current_dir, not_check_file_and_dir_in_current_dir[0])
    ):

        dir_to_rec = os.path.join(current_dir, not_check_file_and_dir_in_current_dir[0])
        list_to_rec = os.listdir(
            os.path.join(current_dir, not_check_file_and_dir_in_current_dir.pop(0))
        )

        deep_storage.append(not_check_file_and_dir_in_current_dir)

    return find_files(dir_to_rec, count_files, list_to_rec, deep_storage)


def test():
    test_dir = os.path.join(os.getcwd(), "..", "data", "8")
    assert sorted(find_files(test_dir, [], os.listdir(test_dir), [])) == sorted(
        [
            "i1.py",
            "i2.py",
            "i3.py",
            "i4.py",
            "i5.py",
            "42",
        ]
    )
