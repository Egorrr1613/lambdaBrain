def MassVote(n: int, votes: list[int]) -> str:
    if n == 1:
        return "majority winner 1"
    votes_with_num = []
    for i in range(n):
        votes_with_num.append((i, votes[i]))
    sum_vote = sum(votes)
    sorted_vote = sort_vote(votes_with_num, 0, n - 1)

    if sorted_vote[n - 1][1] == sorted_vote[n - 2][1]:
        return "no winner"
    if (sum_vote / 2) < sorted_vote[n - 1][1]:
        return f"majority winner {(sorted_vote[n - 1][0]) + 1}"

    return f"minority winner {(sorted_vote[n - 1][0]) + 1}"


def sort_vote(
    input_list: list[tuple[int, int]], index: int, tail_index: int
) -> list[tuple[int, int]]:
    if tail_index == 0:
        return input_list
    if index == tail_index:
        index = 0
        tail_index -= 1
    if input_list[index][1] > input_list[index + 1][1]:
        input_list[index], input_list[index + 1] = (
            input_list[index + 1],
            input_list[index],
        )
    return sort_vote(input_list, index + 1, tail_index)


def test():
    assert MassVote(2, [10, 11]) == "majority winner 2"
    assert MassVote(5, [60, 10, 10, 15, 5]) == "majority winner 1"
    assert MassVote(5, [5, 10, 10, 15, 60]) == "majority winner 5"
    assert MassVote(5, [5, 10, 100, 15, 5]) == "majority winner 3"
    assert MassVote(3, [10, 10, 10]) == "no winner"
    assert MassVote(2, [10, 10]) == "no winner"
    assert MassVote(1, [100]) == "majority winner 1"
    assert MassVote(3, [10, 10, 5]) == "no winner"
    assert MassVote(3, [10, 15, 10]) == "minority winner 2"
    assert MassVote(3, [23, 50, 27]) == "minority winner 2"

