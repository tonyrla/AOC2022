# Advent of Code 2022

This repository contains my Python AOC utility and solutions to the [Advent of Code 2022](https://adventofcode.com/2022) challenges.

![](https://img.shields.io/badge/day%20📅-21-blue)
![](https://img.shields.io/badge/stars%20⭐-28-yellow)
![](https://img.shields.io/badge/days%20completed-14-red)
## Usage
### Session cookie to fetch inputs and submit answers
*  Get your session cookie from [Advent of Code](https://adventofcode.com/) and save it in [./data/.secret_session_cookie](./data/.secret_session_cookie)
*  Inputs are cached to ./inputs, a session cookie lasts for a month, and that's how long the inputs are valid.
*  Inputs and answers are fetched and submitted by parsing the folder structure and filenames, so make sure they are named correctly.
   * `20\d{2}` for the year. Yes, you can break this. Do you have to?
   * `[^0-9]` for the day from the filename. `666_superclever_day01` is not the intended usage <3
   * `aoc2022/day01.py`, `aoc/python/2022/day01.py` etc.

To generate the puzzle .py files for every day:
```bash
python -m AOCRla.aoc
```

To run a specific day's puzzle:
```bash
python ./dayXX.py
```

To open a web browser with the correct puzzle selected, add anything after the python file:
```bash
python ./day01.py  asdf
```
