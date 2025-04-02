# 🕵️‍♂️ Hangman Game 🎮

Welcome to the **Hangman Game**, a simple Python implementation of the classic word-guessing game! Test your vocabulary, beat the odds, and save the stick figure from an unfortunate fate. 🪢

## 🚀 How to Play

1. Run the script in a Python environment.
2. The game will randomly select a word from a predefined list.
3. You have **6 lives**—each incorrect guess costs one!
4. Enter a letter to guess (lowercase).
5. Correct guesses reveal letters in the word.
6. Incorrect guesses reduce lives and draw part of the hangman. ☠️
7. Guess all letters correctly to **win**! 🎉
8. Lose all 6 lives, and it's **game over**. ❌

## 🌜 Rules

- You can only guess **one letter at a time**.
- Repeating a guessed letter won’t cost you a life, but it won’t help either.
- If you run out of lives, the game ends, and you lose.
- The game provides **visual feedback** on your progress.

## 🛠 Requirements

- Python 3.x
- No additional libraries required (just `random`)

## ▶️ Run the Game

Simply execute the Python script:

```sh
python hangman.py
```

## 🎯 Example Gameplay
```
-----
Choose a letter: a
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'a' is not in this word. You lose a life.
You have 5 lives left!
-----
```

## 📌 Features
👉 ASCII art for each stage of the game

👉 Keeps track of guessed letters

👉 Simple, lightweight, and fun!

