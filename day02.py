import sys
from enum import IntEnum

from AOCRla.aoc import AOC



class Points(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    WIN = 6
    DRAW = 3
    LOSE = 0

    @classmethod
    def from_str(cls, key: str) -> 'Points':
        mapping = {
            "A": cls.ROCK,
            "B": cls.PAPER,
            "C": cls.SCISSORS,
            "X": cls.ROCK,
            "Y": cls.PAPER,
            "Z": cls.SCISSORS,
            "WIN": cls.WIN,
            "LOSE": cls.LOSE,
            "DRAW": cls.DRAW,
            "-1": cls.LOSE,
            "0": cls.DRAW,
            "1": cls.WIN,
        }
        return mapping[key]

class puzzle(AOC):
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.input: str = self.get_input_data()

    def part1(self) -> int|None:
        score = 0
        for line in self.input.splitlines():
            enemy, me = map(lambda x: Points.from_str(x), line.split())

            score += me.value
            if enemy == Points.ROCK and me == Points.SCISSORS:
                score += Points.LOSE
            elif me == Points.ROCK and enemy == Points.SCISSORS:
                score += Points.WIN
            else:
                score += Points.from_str(str(me.value - enemy.value))
        return score

    def part2(self) -> int|None:
        # Python is a funny language, let's do this without the enums.
        # Enums are easier to read, but this is more effective.
        RESULTS = {
            "A": 1,
            "B": 2,
            "C": 3,
            "X": 0,
            "Y": 3,
            "Z": 6,
            0 : {
                1: 3,
                2: 1,
                3: 2,
            },
            3 : {
                1: 1,
                2: 2,
                3: 3,
            },
            6 : {
                1: 2,
                2: 3,
                3: 1,
            },
        }

        score: int = 0
        for line in self.input.splitlines():
            enemy_hand, target = map(lambda x: RESULTS.get(x), line.split())
            score += target + RESULTS[target][enemy_hand]

        return score



    def part1_oneliner(self) -> int|None:
        # 'A' - 64 = 1 & 'X' - 87 = 1 -> (ROCK)
        # 'B' - 64 = 2 & 'Y' - 87 = 2 -> (PAPER)
        # 'C' - 64 = 3 & 'Z' - 87 = 3 -> (SCISSORS)
        return sum([6 + me if (opponent-me)%3==2 else 3 + me if (opponent-me)%3==0 else 0 + me for opponent,me in [ (ord(opponent)-64, ord(me)-87) for opponent,me in [ pair.split() for pair in [ line for line in open('./inputs/2022_02.txt').read().strip().split('\n')]]]])

    def part2_oneliner(self) -> int|None:
        return sum([opponent+3 if me == 2 else (opponent-2)%3+1 if me==1 else opponent%3+1+6 for opponent,me in [ (ord(opponent)-64, ord(me)-87) for opponent,me in [ pair.split() for pair in [ line for line in open('./inputs/2022_02.txt').read().strip().split('\n')]]]])



if __name__ == '__main__':
    """
    After 12 hours I realised...You could just map the input straight to matching points.

    Hand x Result = Points
    ROCK[A] vs ROCK[X] == DRAW == 1+3 = 4 -> {'A X': 4, ...}
    Part1 :{ "A X":4, ...,}
    Part2 :{ "A X":3, ...,}
    """
    use_browser = False

    if len(sys.argv) > 1:
        use_browser = True
    p = puzzle(open_browser=use_browser)

    part1 = p.part1()
    part2 = p.part2()

    ol_part1 = p.part1_oneliner()
    assert ol_part1 == part1, f"Part 1 failed: {ol_part1}"
    p.post_answer(1, part1)

    ol_part2 = p.part2_oneliner()
    assert ol_part2 == part2, f"Part 2 failed: {ol_part2}"
    p.post_answer(2, part2)
