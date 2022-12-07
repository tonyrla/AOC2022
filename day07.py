import sys
from collections import defaultdict
from itertools import accumulate

from AOCRla.aoc import AOC

class puzzle(AOC):
    # Out of honesty, my original solution in the morning used DFS,
    # but I just had to try switch case after seeing it on reddit.
    # Modified to prove I understand the puzzle and concept.
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.tree = defaultdict(int)

        self.input: str = self.get_input_data().splitlines()
        cwd = ['/']
        for line in [l.split() for l in self.input]:
            match line:  # dead: disable
                case '$', 'cd', '/':
                    cwd = ['/']
                case '$', 'cd', '..':
                    cwd.pop()
                case '$', 'cd', x: cwd.append(x+'/')
                case size, _:
                    if size.isdigit():
                        for p in accumulate(cwd):
                            self.tree[p] += int(size)
                case _: pass


    def part1(self) -> int|None:
        return sum(s for s in self.tree.values() if s <= 100_000)

    def part2(self) -> int|None:
        m = 70_000_000 - self.tree['/']
        return min(s for s in self.tree.values() if s+m >= 30_000_000)

    def part1_oneliner(self) -> int|None:
        pass

    def part2_oneliner(self) -> int|None:
        pass

if __name__ == '__main__':
    use_browser = False

    if len(sys.argv) > 1:
        use_browser = True
    p = puzzle(open_browser=use_browser)

    part1 = p.part1()
    print(part1)
    p.post_answer(1, part1)

    part2 = p.part2()
    print(part2)
    p.post_answer(2, part2)
