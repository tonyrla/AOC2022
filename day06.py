import sys

from AOCRla.aoc import AOC

class puzzle(AOC):
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.input = self.get_input_data()

    markers = {
        "SOPM": 4,
        "SOMM": 14,
    }

    def get_marker_char(self, data: str, marker_spot: str) -> int:
        offset = self.markers[marker_spot]
        for i in range(len(data)):
            sequence = list(data[i:i+offset])
            if len(set(sequence)) == offset:
                return i+offset

    def part1(self, data: str) -> int|None:
        get = self.get_marker_char(data, "SOPM")
        return get

    def part2(self,data:str) -> int|None:
        get = self.get_marker_char(data, "SOMM")
        return get

    def part1_oneliner(self) -> int|None:
        pass

    def part2_oneliner(self) -> int|None:
        pass

if __name__ == '__main__':
    use_browser = False

    if len(sys.argv) > 1:
        use_browser = True
    p = puzzle(open_browser=use_browser)


    part1 = p.part1(p.input)
    p.post_answer(1, part1)
    part2 = p.part2(p.input)
    p.post_answer(2, part2)
