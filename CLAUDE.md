# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A small Python learning exercise: convert a Roman numeral string to an integer (the LeetCode "Roman to Integer" problem; `README.md` holds the problem statement, rules for subtractive pairs IV/IX/XL/XC/CD/CM, and the constraints: 1 ≤ length ≤ 15, valid numeral in [1, 3999]). UI text and comments are in German.

There is no build system, dependency file, linter config, or test suite. Needs Python ≥ 3.10 (`main.py` uses `match`).

## Commands

- Run: `python3 main.py` (interactive; prompts on stdin)

## Code layout

- `main.py` — the whole program, run as a script (no `if __name__ == "__main__"` guard, so importing it executes the prompts). Flow: `getInput()` loops until input passes validation (`isRoman`, uppercase, alpha, length ≤ 15), then `calcInt()` converts and prints. After that, a leftover block reads a number via `to_float()` until non-zero and prints it; this is unrelated to the conversion.
- `schule.py` — separate scratch file with its own unrelated `to_float`/input loop; not imported by `main.py`.

## Known state

`main.py` is work in progress and `calcInt()` is currently broken: it iterates `for i in value` (characters) then indexes `value[i]` (raises `TypeError`), only handles subtraction for `I`, and has no lookahead logic for X/C pairs. Fixing it means comparing each symbol with the next one (subtract if smaller) rather than the `startswith`/`endswith` checks.
