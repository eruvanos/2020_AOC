from typing import Dict

from pydantic import BaseModel, validator, conint, constr

HCL_PATTERN = r"^#[a-f|0-9]{6}$"
HGT_PATTERN = r"^\d{1,3}(in|cm)$"
ECL_PATTERN = r"^(amb|blu|brn|gry|grn|hzl|oth)$"


class Passport_v1(BaseModel):
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str


class Passport_v2(BaseModel):
    byr: conint(ge=1920, le=2002)  # (Birth Year)
    iyr: conint(ge=2010, le=2020)  # (Issue Year)
    eyr: conint(ge=2020, le=2030)  # (Expiration Year)
    hgt: constr(regex=HGT_PATTERN)  # (Height)
    hcl: constr(regex=HCL_PATTERN)  # (Hair Color)
    ecl: constr(regex=ECL_PATTERN)  # (Eye Color)
    pid: constr(min_length=9, max_length=9)  # (Passport ID)

    @validator("pid")
    def validate_pid(cls, v: str):
        if not v.isnumeric():
            raise ValueError("pid is not a number")
        return v

    @validator("hgt")
    def validate_hgt(cls, v: str):
        if v.endswith("cm") and 150 <= int(v[:-2]) <= 193:
            return v
        elif v.endswith("in") and 59 <= int(v[:-2]) <= 76:
            return v
        else:
            raise ValueError("invalid height")


def part_1(data: Dict):
    valid = 0
    for i, passport in enumerate(data):
        try:
            Passport_v1(**passport)
        except ValueError as e:
            # print(f'{i:03.0f}. {e}')
            continue
        valid += 1

    return valid


def part_2(data):
    valid = 0
    for i, passport in enumerate(data):
        try:
            Passport_v2(**passport)
        except ValueError as e:
            # print(f'{i:03.0f}. {e}')
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
