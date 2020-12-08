import func_machine
import machine
import solution


def test_part_1():
    m = machine.Machine.from_file("test_input.txt")

    assert solution.part_1(m) == 5


def test_part_2():
    m = machine.Machine.from_file("test_input.txt")

    assert solution.part_2(m) == 8


def test_func_machine():
    state = func_machine.from_file("test_input.txt")

    executed = set()

    while not state.term:
        if state.pc in executed:
            break

        executed.add(state.pc)
        state = func_machine.step(state)

    assert state.acc == 5
