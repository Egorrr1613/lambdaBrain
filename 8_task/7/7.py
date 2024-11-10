def matrix(n: int, m: int, input_matrix: list[list[int]]) -> list[int]:
    res = []
    recursion(n, m, input_matrix, 0, 0, res)
    print(res)
    return res


def recursion(n: int, m: int, input_matrix: list[list[int]],
              start_point_m: int, start_point_n: int, result: list[int]):
    if n == 1 and m == 1:
        if (len(input_matrix) + len(input_matrix[0])) % 2 == 0:
            result.append(input_matrix[start_point_m][start_point_n])
        return result

    for i in range(n * m):
        ii = i + 1
        if i < n:
            result.append(input_matrix[start_point_m][i + start_point_n])
            print('a')

        elif ii < n + m:
            print(f'b: i: {i}, n: {n}, m: {m}, start_point_m: {start_point_m}'
                  f' coordinate: {i - (m - 1) + start_point_m}')
            result.append(input_matrix[i - (n - 1) + start_point_m][n - 1 + start_point_n])

        elif ii <= m - 2 + 2 * n:
            result.append(input_matrix[m - 1 + start_point_m]
                          [(m - 2 + 2 * n) - i - 1 + start_point_n])
            print('c')

        elif ii <= 2 * (m - 2) + 2 * n:
            result.append(input_matrix[(2 * (m - 2) + 2 * n) - i][start_point_n])
            print('d')

        print(f'i: {i}, res: {result}\n')

        if ii == (m - 2) * 2 + 2 * n:
            return recursion(n - 2, m - 2, input_matrix, start_point_m + 1, start_point_n + 1, result)


"""
    n -- ширина, m-высота
    
    Перешли на очередной индекс массива
    Если идекс + 1 меньше или равен чем: ширина, тогда добавляем в массив элемент из 0[i]
    
    Если индекс + 1 меньше чем: ширина + высота, то вычитаем из индекса ширина, получаем h (индекс нужного массива)
        добавляем элемент по индексу h[m]
    
    Если индекс меньше или равен: высота - 2 + 2*ширина (n - 2 + 2m), 
        тогда вычитаем из индекса 2*ширина + высоту - 2 (n - 2 + 2m). Модуль разности будет используем как n[res - i]
        
    Если индекс меньше или равен (высота - 2)*2 + 2*ширина (2(n - 2) + 2m), 
        тогда вычитаем из индекса 2*ширина + 2*(высоту - 2) (2(n - 2) + 2m). Модуль разности будет используем как res[0]
        
    Иначе нужно сужать ось
"""


def test():
    assert matrix(1, 1, [[1]]) == [1]

    assert matrix(3, 1, [[1, 2, 3]]) == [1, 2, 3]

    assert matrix(1, 3, [[1], [2], [3]]) == [1, 2, 3]

    assert matrix(2, 2,
                  [[1, 2],
                   [3, 4]]) == [1, 2, 4, 3]

    assert matrix(2, 3,
                  [[1, 2],
                   [3, 4],
                   [5, 6]]) == [1, 2, 4, 6, 5, 3]

    assert matrix(3, 2,
                  [[1, 2, 3],
                   [4, 5, 6]]) == [1, 2, 3, 6, 5, 4]

    assert matrix(3, 3,
                  [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    assert matrix(4, 3,
                  [[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    assert matrix(3, 4,
                  [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]]) == [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]

    assert matrix(4, 4,
                  [[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
