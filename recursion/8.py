import os


def find_files(current_dir: str) -> list:
    if os.path.isfile(current_dir):
        return [current_dir]

    result = []
    for i in os.listdir(current_dir):
        result += find_files(os.path.join(current_dir, i))
    return result


def test():
    test_dir = os.path.join(os.getcwd(), "..", "data", "8")
    assert sorted(find_files(test_dir)) == sorted(
        [
            "/Users/egorreutov/learn/lambdaBrain/recursion/../data/8/a/i1.py",
            "/Users/egorreutov/learn/lambdaBrain/recursion/../data/8/b/c/i2.py",
            "/Users/egorreutov/learn/lambdaBrain/recursion/../data/8/d/e/f/i3.py",
            "/Users/egorreutov/learn/lambdaBrain/recursion/../data/8/d/i4.py",
            "/Users/egorreutov/learn/lambdaBrain/recursion/../data/8/i5.py",
            "/Users/egorreutov/learn/lambdaBrain/recursion/../data/8/42",
        ]
    )
