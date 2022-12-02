import sys

from AOCRla.aoc import AOC

class puzzle(AOC):
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.input = self.get_input_data()

    def sum_calories(self, input: list[str]) -> list[int]:
        lines = input
        cals = 0
        lunchbags = []
        for line in lines:
            try:
                cals += int(line)
            except ValueError:
                lunchbags.append(cals)
                cals = 0
        return sorted(lunchbags, reverse=True)

    def part1(self) -> int|None:
        return self.sum_calories(self.input.split('\n'))[0]

    def part2(self) -> int|None:
        return sum(self.sum_calories(self.input.split('\n'))[:3])


if __name__ == '__main__':
    user_browser = False

    if len(sys.argv) > 1:
        user_browser = True

    p = puzzle(open_browser=user_browser)

    part1 = p.part1()
    p.post_answer(1, part1)

    part2 = p.part2()
    p.post_answer(2, part2)
