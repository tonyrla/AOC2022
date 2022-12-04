import sys

from AOCRla.aoc import AOC

class puzzle(AOC):
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.input: str = self.get_input_data()

    def _get_ranges(self, line: str) -> tuple[range, range]:
        start_a, end_a, start_b, end_b = tuple(map(int,line.replace(',', '-').split('-')))
        set_a = range(start_a, end_a+1)
        set_b = range(start_b, end_b+1)
        return set_a, set_b

    def part1(self) -> int|None:
        input = self.input.splitlines()
        count = 0
        for line in input:
            set_a, set_b = self._get_ranges(line)
            intersections = len(set(set_a).intersection(set_b))
            count += (intersections == len(set_a) or intersections == len(set_b))

        return count

    def part2(self) -> int|None:
        input = self.input.splitlines()
        count = 0
        for line in input:
            set_a, set_b = self._get_ranges(line)
            count += len(set(set_a).intersection(set_b)) > 0
        return count

    def part1_oneliner(self) -> int|None:
        return sum([len(pair[0]) == len(set(pair[0]).intersection(pair[1])) or len(pair[1]) == len(set(pair[0]).intersection(pair[1])) for pair in [(range(pair[0],pair[1]+1), range(pair[2],pair[3]+1)) for pair in [tuple(map(int, pair.replace(',', '-').split('-'))) for pair in [line for line in open(f'./inputs/2022_04.txt').read().strip().splitlines()]]]])

    def part2_oneliner(self) -> int|None:
        return sum([len(set(pair[0]).intersection(pair[1])) > 0 for pair in [(range(pair[0],pair[1]+1), range(pair[2],pair[3]+1)) for pair in [tuple(map(int, pair.replace(',', '-').split('-'))) for pair in [line for line in open(f'./inputs/2022_04.txt').read().strip().splitlines()]]]])

if __name__ == '__main__':
    use_browser = False

    if len(sys.argv) > 1:
        use_browser = True
    p = puzzle(open_browser=use_browser)

    part1 = p.part1()
    ol_part1 = p.part1_oneliner()
    assert part1 == ol_part1, f"Part 1: {part1} != {ol_part1}"
    p.post_answer(1, part1)

    part2 = p.part2()
    ol_part2 = p.part2_oneliner()
    assert part2 == ol_part2, f"Part 2: {part2} != {ol_part2}"
    p.post_answer(2, part2)
