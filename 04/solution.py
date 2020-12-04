import re
from typing import Dict

HCL_PATTERN = re.compile(r"^#[a-f|0-9]{6}$")
REQUIRED = {
    "byr",  # (Birth Year)
    "iyr",  # (Issue Year)
    "eyr",  # (Expiration Year)
    "hgt",  # (Height)
    "hcl",  # (Hair Color)
    "ecl",  # (Eye Color)
    "pid",  # (Passport ID)
    # 'cid',  # (Country ID)
}


def part_1(data: Dict):
    valid = 0
    for passport in data:
        if set(passport.keys()).issuperset(REQUIRED):
            valid += 1

    return valid


def part_2(data):
    valid = 0
    for passport in data:
        try:
            if not set(passport.keys()).issuperset(REQUIRED):
                continue

            byr = passport["byr"]
            if not byr.isnumeric():
                continue
            if not (1920 <= int(byr) <= 2002):
                continue

            iyr = passport["iyr"]
            if not iyr.isnumeric():
                continue
            if not (2010 <= int(iyr) <= 2020):
                continue

            eyr = passport["eyr"]
            if not eyr.isnumeric():
                continue
            if not (2020 <= int(eyr) <= 2030):
                continue

            hgt = passport["hgt"]
            hgt, hgt_si = hgt[:-2], hgt[-2:]
            if not hgt.isnumeric():
                continue
            if not (
                (hgt_si == "cm" and 150 <= int(hgt) <= 193)
                or (hgt_si == "in" and 59 <= int(hgt) <= 76)
            ):
                continue

            hcl = passport["hcl"]
            hcl.startswith("#")
            if not (HCL_PATTERN.fullmatch(hcl)):
                continue

            ecl = passport["ecl"]
            if not (ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}):
                continue

            pid = passport["pid"]
            if not pid.isnumeric():
                continue
            if not pid.isnumeric():
                continue
            if not (len(pid) == 9):
                continue
            if not (0 <= int(pid) <= 999999999):
                continue

            # cid = passport['cid']
            # ignore
        except:
            continue

        valid += 1

    return valid


def parse(lines):
    passports = []
    passport = {}
    passports.append(passport)

    for line in lines:
        if len(line) == 0:
            passport = {}
            passports.append(passport)

        for kv_pair in line.split():
            key, value = kv_pair.split(":")
            passport[key] = value

    return passports


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    data = parse(lines)
    print("Part 1: ", part_1(data))
    print("Part 2: ", part_2(data))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
