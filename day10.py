import sys
from collections import defaultdict

from AOCRla.aoc import AOC

class Instruction:
    def __init__(self, instruction: str):
        self.instruction = instruction
        splt = instruction.split()
        self.opcode = splt[0]
        self.argument = 0
        if len(splt) > 1:
            self.argument = int(splt[1])
        self.cycles = 1 if self.opcode == "noop" else 2

    def __repr__(self):
        return f"{self.opcode} {self.argument}"

class CRTCPU:
    def __init__(self, instructions: list[str]):
        self.instructions = [Instruction(i) for i in instructions]
        self.register = 1
        self.ticks = 1

        # 6 rows 40 columns
        self.display = [[' ' for _ in range(40)] for _ in range(6)]
        self.current_row = 0
        self.current_pos = 0

    def draw(self) -> None:
        if self.current_pos >= len(self.display[0]):
            self.current_row += 1
            self.current_pos = 0

        if self.current_pos in range(self.register-1, self.register+2):
            self.display[self.current_row][self.current_pos] = '#'

        self.current_pos += 1

    def draw_display(self) -> None:
        for row in self.display:
            print(''.join(row))

    def _execute(self) -> None:
        if self.instructions[0].opcode == "addx":
            self.register += self.instructions[0].argument

    def tick(self) -> None:
        if self.instructions[0].cycles > 1:
            self.instructions[0].cycles -= 1
        else:
            self._execute()
            self.instructions.pop(0)
        self.ticks += 1


class puzzle(AOC):
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.input: str = self.get_input_data()

    def part1(self) -> int|None:
        cpu = CRTCPU(self.input.splitlines())
        total = 0
        while cpu.instructions:
            if cpu.ticks in (20,60,100,140,180,220):
                total += cpu.register*cpu.ticks
            cpu.tick()
        return total

    def part2(self) -> int|None:
        cpu = CRTCPU(self.input.splitlines())
        while cpu.instructions:
            cpu.draw()
            cpu.tick()

        cpu.draw_display()
        return 0

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
    p.post_answer(1, part1)

    part2 = p.part2()
    # Really need to map these ascii results one day.
