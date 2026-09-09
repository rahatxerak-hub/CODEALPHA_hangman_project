# CodeAlpha_Hangman

A simple text-based Hangman game built in Python, created as Task 1 for the
CodeAlpha Python Programming Internship.

## How It Works

- The program picks a random word from a small predefined list.
- The player guesses one letter at a time.
- Correct guesses reveal the letter's position(s) in the word.
- Incorrect guesses reduce the remaining attempts (6 total) and draw the
  next stage of the hangman.
- The game ends when the player either guesses the full word or runs out
  of attempts.

## Concepts Used

- `random` module for word selection
- `while` loops for the main game loop
- `if`/`else` for guess validation and win/loss checks
- Strings and lists for word storage and display
- Sets for tracking guessed letters (avoids duplicate guesses)

## How to Run

```bash
python hangman.py
```

Follow the on-screen prompts to guess letters. You'll be asked if you
want to play again after each round.

## Example

```
Word:  _ _ _ h _ _
Wrong guesses left: 4

Guess a letter: o
Good guess!
```
