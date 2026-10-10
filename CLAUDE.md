# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A small Python program: convert a Roman numeral string to an integer (the LeetCode "Roman to Integer" problem; `README.md` holds the problem statement and constraints: 1 ≤ length ≤ 15, valid numeral in [1, 3999]). UI text and comments are in German. No dependencies; needs Python ≥ 3.10.

## Commands

- Run: `python3 main.py` (interactive; prompts on stdin until the input is valid)
- Test all: `python3 -m unittest -q`
- Test a single case: `python3 -m unittest test_main.TestCalcInt.test_grenzen`

## Code layout

- `main.py` — `getInput()` loops until `isValid()` passes (length 1–15, uppercase letters, only `IVXLCDM`, and a strict regex `MUSTER` that enforces correct numerals such as rejecting `IIII`, `VX`, `IC`); `calcInt()` converts by subtracting a symbol when a larger one directly follows. The prompt only runs under `if __name__ == "__main__"`, so the functions can be imported.
- `test_main.py` — unittest suite, including a round trip over every value 1–3999.
- Code style: tab indentation.
