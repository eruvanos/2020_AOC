from machine import Machine


def part_1(machine: Machine):
    executed = set()

    while not machine.term:
        if machine.pc in executed:
            break

        executed.add(machine.pc)
        machine.step()

    return machine.acc


def part_2(machine: Machine):
    code_backup = machine.code[:]

    breakpoints = [
        pc for pc, (op, arg) in enumerate(code_backup) if op in {"nop", "jmp"}
    ]

    while True:
        acc = part_1(machine)

        if machine.term:
            break
        else:
            machine = Machine(code_backup[:])

            pc = breakpoints.pop(0)
            op, arg = machine.code[pc]
            machine.code[pc] = ("nop" if op == "jmp" else "jmp", arg)
            # print(f'modified {pc}: {op}')

    return machine.acc


def parse(lines):
    return Machine.from_lines(lines)


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(parse(lines)))
    print("Part 2: ", part_2(parse(lines)))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
