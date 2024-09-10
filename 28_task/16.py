def MaximumDiscount(n: int, prices: list[int]) -> int:
    if n < 3:
        return 0
    sort_price = bubble_sort(prices, 0, n - 1)
    partition = n // 3
    simple_discount = get_prices_from_start(partition, sort_price, 0)
    if n < 4:
        return simple_discount
    spl_price = split_prices_by_partition(sort_price, n, -1, [])
    difficult_disc = sum(map(lambda i: i[2], spl_price))

    return simple_discount if simple_discount > difficult_disc else difficult_disc


def get_min_el_from_partition(input_l: list[int]) -> int:
    if len(input_l) < 3:
        return 0
    min_el = input_l[0]
    for i in [1, 2]:
        min_el = input_l[i] if min_el > input_l[i] else min_el
    return min_el


def bubble_sort(input_arr: list[int], curr_i: int, tail_i: int):
    next_i = curr_i + 1
    if tail_i == 0:
        return input_arr
    if curr_i == tail_i:
        next_i = 0
        tail_i -= 1
    elif input_arr[curr_i] > input_arr[curr_i + 1]:
        input_arr[curr_i], input_arr[curr_i + 1] = (
            input_arr[curr_i + 1],
            input_arr[curr_i],
        )
    return bubble_sort(input_arr, next_i, tail_i)


def get_prices_from_start(n: int, prises: list, iter_index: int):
    if iter_index == (n - 1) or n == 0:
        return prises[iter_index]
    return prises[iter_index] + get_prices_from_start(n, prises, iter_index + 1)


def split_prices_by_partition(
    prises: list[int], prises_len: int, index_el: int, buffer: list[list[int]]
) -> list[list[int]]:
    if index_el == -prises_len:
        return buffer
    if index_el - 3 < -prises_len - 1:
        return buffer
    buffer.append(prises[index_el : index_el - 3 : -1])
    return split_prices_by_partition(prises, prises_len, index_el - 3, buffer)


def sort_partition(prises: list[list[int]]) -> list[list[int]]:
    if len(prises[-1]) == 1:
        buffer = prises[-1][0]
        prises[-1][0] = prises[-2][0]
        prises[-2][0] = buffer

    if len(prises[-1]) == 2:
        buffer_1, buffer_2 = prises[-1][0], prises[-1][1]
        prises[-1][0] = prises[-3][0]
        prises[-1][1] = prises[-2][0]
        prises[-2][0], prises[-3][0] = (
            buffer_2,
            buffer_1,
        )

    return prises


def test():
    assert bubble_sort([9, 8, 8, 7, 5, 3, 10], 0, 6) == [3, 5, 7, 8, 8, 9, 10]
    assert (
        get_prices_from_start(3, [100, 200, 300, 400, 500, 600, 700, 800, 900], 0)
        == 600
    )
    assert get_prices_from_start(2, [100, 200, 300, 400, 500, 600, 700, 800], 0) == 300

    assert MaximumDiscount(1, [400]) == 0
    assert MaximumDiscount(3, [400, 350, 300]) == 300
    assert MaximumDiscount(4, [100, 400, 350, 300]) == 300
    assert (
        MaximumDiscount(11, [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100])
        == 1800
    )
    assert (
        MaximumDiscount(10, [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1500
    )
    assert MaximumDiscount(9, [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 1200
    assert MaximumDiscount(8, [100, 200, 300, 400, 500, 600, 700, 800]) == 900
    assert MaximumDiscount(7, [100, 200, 300, 400, 500, 600, 700]) == 700
    assert MaximumDiscount(7, [100, 150, 200, 250, 300, 350, 400]) == 450
    assert MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100]) == 450
    assert MaximumDiscount(7, [100, 150, 200, 200, 200, 200, 400]) == 350
    assert MaximumDiscount(6, [100, 200, 300, 400, 500, 600]) == 500
    assert MaximumDiscount(6, [3, 3, 3, 3, 3, 10]) == 6
    assert MaximumDiscount(6, [12, 12, 10, 10, 10, 10]) == 20
    assert MaximumDiscount(6, [1, 3, 3, 3, 5, 6]) == 4

