def Keymaker(k: int) -> str:
    door_status = [0] * k

    for door_number in range(1, k + 1):
        door_edit(door_status, door_number)
    door_status_str = map(str, door_status)

    return "".join(door_status_str)


def door_edit(door_list: list[int], door_number: int) -> None:
    for i, _ in enumerate(door_list):
        if (i + 1) % door_number == 0:
            door_list[i] = int(door_list[i] == 0)


def test():
    assert Keymaker(1) == "1"
    assert Keymaker(2) == "10"
    assert Keymaker(3) == "100"
    assert Keymaker(4) == "1001"
    assert Keymaker(5) == "10010"
    assert Keymaker(6) == "100100"
    assert Keymaker(7) == "1001000"
    assert Keymaker(8) == "10010000"
    assert Keymaker(9) == "100100001"
    assert Keymaker(10) == "1001000010"
    assert Keymaker(11) == "10010000100"
    assert Keymaker(12) == "100100001000"
    assert Keymaker(13) == "1001000010000"
    assert Keymaker(14) == "10010000100000"
    assert Keymaker(15) == "100100001000000"
    assert Keymaker(16) == "1001000010000001"
    assert Keymaker(17) == "10010000100000010"
    assert Keymaker(18) == "100100001000000100"
    assert Keymaker(19) == "1001000010000001000"
    assert Keymaker(20) == "10010000100000010000"
    assert Keymaker(21) == "100100001000000100000"
    assert Keymaker(22) == "1001000010000001000000"
    assert Keymaker(23) == "10010000100000010000000"
    assert Keymaker(24) == "100100001000000100000000"
    assert Keymaker(25) == "1001000010000001000000001"
    assert Keymaker(26) == "10010000100000010000000010"
    assert Keymaker(27) == "100100001000000100000000100"
    assert Keymaker(28) == "1001000010000001000000001000"
    assert Keymaker(29) == "10010000100000010000000010000"
    assert Keymaker(30) == "100100001000000100000000100000"
    assert Keymaker(31) == "1001000010000001000000001000000"
    assert Keymaker(32) == "10010000100000010000000010000000"
    assert Keymaker(33) == "100100001000000100000000100000000"
    assert Keymaker(34) == "1001000010000001000000001000000000"
    assert Keymaker(35) == "10010000100000010000000010000000000"
    assert Keymaker(36) == "100100001000000100000000100000000001"
    assert Keymaker(49) == "1001000010000001000000001000000000010000000000001"

