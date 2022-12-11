import math
import operator
import sys
from copy import deepcopy
from typing import Any

from AOCRla.aoc import AOC

operators = {
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod
}

class Item:
    def __init__(self, value: int):
        self.value = value

    def operation(self, operation: str, part1: bool = True, prod: int = 0):
        op = operation.split(" = ")[1]
        match op.split(" "):
            case ["old", operator, value]:
                if value.isnumeric():
                    self.value = operators[operator](self.value, int(value))
                else:
                    self.value = operators[operator](self.value, self.value)
            case _:
                raise ValueError(f"Invalid operation : {op}")
        if part1:
            self.value = math.floor(operators['/'](self.value, 3))
        else:
            self.value = math.floor(operators['%'](self.value, prod))

class Monkey:
    def __init__(self, data: str):
        self.data = data
        self.items = []
        self.operation = None
        self.divisible_test = None
        self.id = None
        self.true_target = None
        self.false_target = None
        self.parse_data()
        self.inspected = 0


    def parse_data(self):
        for line in self.data:
            line = line.strip()
            if line.startswith("Starting items"):
                self.items = [Item(int(x)) for x in line.split(":")[1].split(",")]
            elif line.startswith("Operation"):
                self.operation = line.split(":")[1].strip()
            elif line.startswith("Test"):
                self.divisible_test = int(line.split("divisible by ")[1].strip())
            elif line.startswith("Monkey"):
                self.id = int(line.split(":")[0].split(" ")[1])
            elif line.startswith("If true"):
                self.true_target = int(line.split(" ")[5])
            elif line.startswith("If false"):
                self.false_target = int(line.split(" ")[5])

    def inspect(self, other_monkeys: list[Any], part1: bool = True, prod: int = 0):

        while(len(self.items) > 0):
            item = self.items.pop(0)
            self.inspected += 1

            item.operation(self.operation, part1=part1, prod=prod)
            if item.value % self.divisible_test == 0:
                other_monkeys[self.true_target].items.append(item)
            else:
                other_monkeys[self.false_target].items.append(item)


class puzzle(AOC):
    def __init__(self, open_browser: bool = False):
        super().__init__(open_browser=open_browser)
        self.input = self.get_input_data()

        DATA = self.input
        self._monkeys = []
        self.prod = 1
        for p in DATA.split("\n\n"):
            self._monkeys.append( Monkey(p.splitlines()) )
            self.prod *= self._monkeys[-1].divisible_test

    def _reset_input(self):
        self.monkeys = deepcopy(self._monkeys)

    def simulate(self, monkeys: list[Monkey], rounds:int = 20, part1: bool = True, prod: int = 0):
        for _ in range(0, rounds):
            for monkey in monkeys:
                monkey.inspect(monkeys, part1=part1, prod=prod)

    def part1(self) -> int|None:
        self._reset_input()
        self.simulate(self.monkeys, 20)

        highest_inspected = sorted(self.monkeys, key=lambda x: x.inspected, reverse=True)
        return highest_inspected[0].inspected * highest_inspected[1].inspected


    def part2(self) -> int|None:
        self._reset_input()
        self.simulate(self.monkeys, 10_000, False, self.prod)

        highest_inspected = sorted(self.monkeys, key=lambda x: x.inspected, reverse=True)
        return highest_inspected[0].inspected * highest_inspected[1].inspected

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
    p.post_answer(2, part2)
