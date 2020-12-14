# fmt: off
import re
import sys

from utils import bits

sys.path.append("..")

# fmt: on

MEM_PATTERN = re.compile(r"mem\[(\d*)\]")


def part_1(instructions):
    mask = None
    mem = {}
    for cmd, value in instructions:
        if cmd == "mask":
            mask = value
        elif cmd.startswith("mem"):
            addr = int(MEM_PATTERN.search(cmd).group(1))

            int_value = value
            for offset, bit in enumerate(reversed(mask)):
                if bit == "1":
                    m = 1 << offset
                    int_value |= m
                elif bit == "0":
                    m = ~(1 << offset)
                    int_value &= m

            # print(f"mem[{addr}] = {int_value:b} {int_value}")
            mem[addr] = int_value
    return sum(mem.values())


def resolve_floats(addr, fill: int):
    """
    replaces every X using bits of fill parameter
    """
    list_addr = list(reversed(addr))
    off = 0
    for i, a in enumerate(list_addr):
        if a == "X":
            if bits.test_bit(fill, off):
                list_addr[i] = "1"
            else:
                list_addr[i] = "0"
            off += 1

    return "".join(reversed(list_addr))


def permut(addr):
    """
    Permutes the address replacing X with either 0,1
    """
    for x in range(2 ** addr.count("X")):
        yield resolve_floats(addr, x)


def part_2(instructions):
    mask = None
    mem = {}

    for cmd, value in instructions:
        if cmd == "mask":
            mask = value
        elif cmd.startswith("mem"):
            # parse address
            addr = int(MEM_PATTERN.search(cmd).group(1))

            # mask address
            addr = list(f"{addr:b}".rjust(len(mask), "0"))
            for offset, bit in enumerate(mask):
                if bit == "1":
                    addr[offset] = "1"
                elif bit == "X":
                    addr[offset] = "X"

            # save value, resolve addresses by template
            for floating_addr in permut(list(reversed(addr))):
                # print(f"mem[{int(floating_addr, 2)} - {floating_addr}] = {value}")
                mem[floating_addr] = value

    return sum(mem.values())


def parse(lines):
    instructions = []
    complex = 0
    for line in lines:
        cmd, value = line.split(" = ")
        if cmd == "mask":
            complex += value.count("X") ** 2
            instructions.append((cmd, value))
        elif cmd.startswith("mem"):
            instructions.append((cmd, int(value)))

    return instructions


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
