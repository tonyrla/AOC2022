import re
import sys
from collections import defaultdict
from typing import Generator

from AOCRla.aoc import AOC

class puzzle(AOC):
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.input = self.get_input_data()

    def _build_columns(self, stacks_str: str) -> dict[int,list[str]]:
        stacks = stacks_str.splitlines()
        stacks.reverse()

        # I guess you could also go with line[1::4]
        cols: defaultdict[int, list[str]] = defaultdict(list[str])
        headers = re.findall(r"(\d+)",stacks.pop(0))
        for line in stacks:
            for col in headers:
                cont = line[:4].strip()
                if cont:
                    cols[int(col)].insert(0,line[:4].strip())
                line = line[4:]
        return cols

    def _parse_return(self, cols: dict[int,list[str]]) -> str|None:
        retval = ""
        for col in cols:
            retval += cols[col][0][1]
        return retval

    def _parse_instructions(self, instructions: str) -> Generator[tuple[int,int,int], None, None]:
        for inst in instructions.splitlines():
            count, from_col, to_col = re.findall(r"(\d+)",inst)
            yield (int(count), int(from_col), int(to_col))
        return None

    def part1(self, data:str) -> str|None:
        stacks, instructions = data.split('\n\n')
        cols = self._build_columns(stacks)
        for count, from_col, to_col in self._parse_instructions(instructions):
            for _ in range(int(count)):
                cols[int(to_col)].insert(0,cols[int(from_col)].pop(0))

        return self._parse_return(cols)


    def part2(self, data: str) -> str|None:
        stacks, instructions = data.split('\n\n')
        cols = self._build_columns(stacks)

        for count, from_col, to_col in self._parse_instructions(instructions):
            sublist = cols[from_col][:count]
            for n, item in enumerate(sublist):
                cols[int(from_col)].remove(item)
                cols[int(to_col)].insert(n,item)


        return self._parse_return(cols)

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
