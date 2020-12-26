# fmt: off
import sys
from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import List

from toolz import first, last

sys.path.append("..")


# fmt: on


@dataclass
class Food:
    ingredients: List
    allergens: List


def part_1(data):
    foods: List[Food] = data

    resolved_db = resolve_food_ings(foods)

    # print resolved
    for key, value in resolved_db.items():
        print(key, ":", value)

    # get save ings
    all_ingredients = []
    for food in foods:
        all_ingredients.extend(food.ingredients)

    save_ings = set(all_ingredients) - set(resolved_db.values())

    total = 0
    counter = Counter(all_ingredients)
    for ing in save_ings:
        total += counter[ing]

    return total

    # allergen_ing = {}
    # ing_allergen = {}
    # for food in foods:
    #     for allergen in food.allergens:
    #         allergen_ing[allergen].extend(food.ingredients)
    #
    #     for ing in food.ingredients:
    #         ing_allergen[ing].extend(food.allergens)


def resolve_food_ings(foods):
    db = defaultdict(list)
    for food in foods:
        for allergen in food.allergens:
            db[allergen].append(set(food.ingredients))
    # reduce to possible ings
    for allergen, ings in db.items():
        intersect = set(ings[0])
        for ing in ings[1:]:
            intersect.intersection_update(ing)
        db[allergen] = intersect
    # resolve db
    resolved_db = {}
    while db:
        # find resolved allergens
        new_resolved = []
        for key, ings in list(db.items()):
            if len(ings) == 1:
                new_resolved.append((key, ings.pop()))
                del db[key]

        # remove resolved allergens in db
        for al, ing in new_resolved:
            resolved_db[al] = ing

            for key, ings in db.items():
                if ing in ings:
                    ings.remove(ing)
    return resolved_db


def part_2(data):
    foods: List[Food] = data

    resolved_db = resolve_food_ings(foods)

    print("NOT: clg,cxfz,knprxg,lxjtns,ncjv,prxmdlz,qdfpq,vzzz")
    items = list(resolved_db.items())
    items.sort(key=first)

    return ",".join(map(last, items))


def parse(lines):
    alergen_ing = defaultdict(list)
    ing_alergen = defaultdict(list)

    foods = []
    for line in lines:
        ingrediances, alergens = line.split(" (")
        ingrediances = ingrediances.split()
        alergens = alergens[9:-1].split(", ")

        foods.append(Food(ingrediances, alergens))

    return foods


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(parse(lines[:])))
    print("Part 2: ", part_2(parse(lines[:])))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
