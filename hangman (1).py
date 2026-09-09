# CodeAlpha — Task 1: Hangman Game
# Five predefined words. Six lives. Letter-by-letter guessing.
# Key concepts: random, while loop, if-else, strings, lists.
# Run: python hangman.py

from __future__ import annotations

import random
import sys

WORDS = ["PYTHON", "PLANET", "RIVER", "GUITAR", "ORBIT"]
MAX_WRONG = 6

GALLOWS = [
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========""",
]


def choose_word(exclude: str | None = None) -> str:
    pool = [w for w in WORDS if w != exclude] or list(WORDS)
    return random.choice(pool)


def masked(word: str, guessed: list[str]) -> str:
    return " ".join(letter if letter in guessed else "_" for letter in word)


def read_guess(guessed: list[str]) -> str:
    while True:
        raw = input("Guess a letter: ").strip().upper()
        if len(raw) != 1 or not raw.isalpha():
            print("  Please enter a single letter A-Z.")
            continue
        if raw in guessed:
            print("  You already tried '%s'." % raw)
            continue
        return raw


def play_round(previous: str | None = None) -> tuple[str, bool]:
    word = choose_word(previous)
    guessed: list[str] = []
    wrong = 0

    print()
    print("INK & TICKER — Hangman")
    print("Five words. Six lives. Guess the letter.")
    print("-" * 36)

    while True:
        print(GALLOWS[wrong])
        print()
        print("  Word:   %s" % masked(word, guessed))
        print("  Tried:  %s" % (", ".join(guessed) if guessed else "-"))
        print("  Lives:  %d" % (MAX_WRONG - wrong))

        if all(letter in guessed for letter in word):
            print()
            print("  You had it. %s." % word)
            return word, True
        if wrong >= MAX_WRONG:
            print()
            print("  Out of lives. The word was %s." % word)
            return word, False

        letter = read_guess(guessed)
        guessed.append(letter)
        if letter in word:
            print("  '%s' is in the word." % letter)
        else:
            wrong += 1
            print("  '%s' is not in the word." % letter)


def main() -> None:
    previous: str | None = None
    wins = 0
    losses = 0
    try:
        while True:
            previous, won = play_round(previous)
            if won:
                wins += 1
            else:
                losses += 1
            print()
            print("  Score  %d won / %d lost" % (wins, losses))
            again = input("Play again? [Y/n] ").strip().lower()
            if again in {"n", "no"}:
                break
        print()
        print("Thanks for playing.")
    except (KeyboardInterrupt, EOFError):
        print()
        print("Goodbye.")
        sys.exit(0)


if __name__ == "__main__":
    main()
