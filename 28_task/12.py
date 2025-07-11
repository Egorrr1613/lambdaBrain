def MassVote(n: int, votes: list[int]) -> str:
    if n == 1:
        return "majority winner 1"
    indexed_votes = []
    for i in range(n):
        indexed_votes.append((i, votes[i]))
    sum_vote = sum(votes)
    sorted_vote = sort_vote(indexed_votes, 0, n - 1)

    if sorted_vote[n - 1][1] == sorted_vote[n - 2][1]:
        return "no winner"
    if (sum_vote / 2) < sorted_vote[n - 1][1]:
        return f"majority winner {(sorted_vote[n - 1][0]) + 1}"

    return f"minority winner {(sorted_vote[n - 1][0]) + 1}"


def sort_vote(
    indexing_vote_list: list[tuple[int, int]], index: int, last_vote_index: int
) -> list[tuple[int, int]]:
    if last_vote_index == 0:
        return indexing_vote_list
    if index == last_vote_index:
        index = 0
        last_vote_index -= 1
    if indexing_vote_list[index][1] > indexing_vote_list[index + 1][1]:
        indexing_vote_list[index], indexing_vote_list[index + 1] = (
            indexing_vote_list[index + 1],
            indexing_vote_list[index],
        )
    return sort_vote(indexing_vote_list, index + 1, last_vote_index)


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
    assert MassVote(3, [23, 51, 27]) == "majority winner 2"

