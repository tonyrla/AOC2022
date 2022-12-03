import sys
from itertools import zip_longest

from AOCRla.aoc import AOC

def get_priority(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38

def grouper(iterable: list[str]) -> list[list[str]]:
    return zip_longest(fillvalue=None, *([iter(iterable)] * 3))  # type: ignore

class puzzle(AOC):
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.input = self.get_input_data()

    def part1(self) -> int|None:
        total = 0
        for line in self.input.strip().splitlines():
            midpoint = int(len(line) / 2)
            a = line[:midpoint]
            b = line[midpoint:]
            intersection = set(a).intersection(set(b))
            total += sum(get_priority(c) for c in intersection)
        return total

    def part2(self) -> int|None:
        total = 0
        for groups in grouper(self.input.strip().splitlines()):
            intersection = set(groups[0]).intersection(set(groups[1]), set(groups[2]))
            total += sum(get_priority(c) for c in intersection)

        return total

    def part1_oneliner(self) -> int|None:
        return sum(ord(c) - 96 if c.islower() else ord(c) - 38 for c in [set(x[:int(len(x)/2)]).intersection(x[int(len(x)/2):]).pop() for x in open('./inputs/2022_03.txt').read().strip().splitlines()])


    def part2_oneliner(self) -> int|None:
        return sum(ord(c) - 96 if c.islower() else ord(c) - 38 for c in [set(groups[0]).intersection(groups[1],groups[2]).pop() for groups in zip_longest(fillvalue=None, *([iter(open('./inputs/2022_03.txt').read().strip().splitlines())] * 3))])


if __name__ == '__main__':
    use_browser = False

    if len(sys.argv) > 1:
        use_browser = True
    p = puzzle(open_browser=use_browser)

    part1 = p.part1()
    p.post_answer(1, part1)
    ol_part1 = p.part1_oneliner()
    assert ol_part1 == part1, f"Part 1 oneliner failed. Expected {part1}, got {ol_part1}"
    print(f"Part 1 oneliner passed: {ol_part1} == {part1}")

    part2 = p.part2()
    p.post_answer(2, part2)
    ol_part2 = p.part2_oneliner()
    assert ol_part2 == part2, f"Part 2 oneliner failed. Expected {part2}, got {ol_part2}"
    print(f"Part 2 oneliner passed: {ol_part2} == {part2}")
