def Resolve(do_print=False):

    with open("input.txt", "r") as f:
        content = f.read()

    numbers = [int(c) for c in content[:-1]]

    def PlayWithCrabs(start, links, it):
        l = len(links) - 1
        current = start
        pick = [0] * 3
        dest = 0
        for _ in range(it):
            n = links[current]
            for i in range(3):
                pick[i], n = n, links[n]
            dest = ((current - 2) % l) + 1
            while dest in pick:
                dest = ((dest - 2) % l) + 1
            links[current], links[pick[2]], links[dest] = (
                links[pick[2]],
                links[dest],
                pick[0],
            )
            current = links[current]

    # Part1

    l1 = len(numbers)
    links = [0] * (l1 + 1)
    for i, n in enumerate(numbers):
        links[n] = numbers[(i + 1) % l1]
    PlayWithCrabs(numbers[0], links, 100)
    lst = [0] * (l1 + 1)
    n = 1
    for i in range(1, (l1 + 1)):
        lst[i] = n
        n = links[n]
    str1 = "".join([str(n) for n in lst[2:]])

    # Part2

    l2 = 1000000
    links = [0] * (l2 + 1)
    for i, n in enumerate(numbers):
        links[n] = numbers[(i + 1) % l1]
    for n in range(l1 + 1, l2):
        links[n] = n + 1
    links[numbers[-1]] = l1 + 1
    links[l2] = numbers[0]
    PlayWithCrabs(numbers[0], links, 10000000)
    val2 = links[1]
    val2 *= links[val2]

    if do_print:
        print("Numeros gaulois 1:", str1)
        print("Etoiles gauloises 2:", val2)


# #############################################################################
if __name__ == "__main__":
    Resolve(True)
    # Results with given input:
    #   1: 32897654
    #   2: 186715244496
