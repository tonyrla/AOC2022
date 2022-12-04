import sys

from AOCRla.aoc import AOC

class puzzle(AOC):
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.input = self.get_input_data()

    def part1(self) -> int|None:
        input = self.get_input_data().splitlines()
        count = 0
        for line in input:
            a,b = line.split(',')
            start_a, end_a = a.split('-')
            start_b, end_b = b.split('-')
            set_a = range(int(start_a), int(end_a)+1)
            set_b = range(int(start_b), int(end_b)+1)
            intersections = len(set(set_a).intersection(set_b))
            if intersections == len(set_a) or intersections == len(set_b):
                count += 1

        return count

    def part2(self) -> int|None:
        input = self.get_input_data().splitlines()
        count = 0
        for line in input:
            a,b = line.split(',')
            start_a, end_a = a.split('-')
            start_b, end_b = b.split('-')
            set_a = range(int(start_a), int(end_a)+1)
            set_b = range(int(start_b), int(end_b)+1)
            if len(set(set_a).intersection(set_b)) > 0:
                count += 1
        return count

    def part1_oneliner(self) -> int|None:
        return sum([1 if len(pair[0]) == len(set(pair[0]).intersection(pair[1])) or len(pair[1]) == len(set(pair[0]).intersection(pair[1])) else 0 for pair in [(range(pair[0],pair[1]+1), range(pair[2],pair[3]+1)) for pair in [tuple(map(int, pair.replace(',', '-').split('-'))) for pair in [line for line in open(f'./inputs/2022_04.txt').read().strip().splitlines()]]]])


    def part2_oneliner(self) -> int|None:
        return sum([1 if len(set(pair[0]).intersection(pair[1])) > 0 else 0 for pair in [(range(pair[0],pair[1]+1), range(pair[2],pair[3]+1)) for pair in [tuple(map(int, pair.replace(',', '-').split('-'))) for pair in [line for line in open(f'./inputs/2022_04.txt').read().strip().splitlines()]]]])

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
