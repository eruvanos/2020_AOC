import solution, machine


def test_part_1():
    m = machine.Machine.from_file("test_input.txt")

    assert solution.part_1(m) == 5


def test_part_2():
    m = machine.Machine.from_file("test_input.txt")

    assert solution.part_2(m) == 8
