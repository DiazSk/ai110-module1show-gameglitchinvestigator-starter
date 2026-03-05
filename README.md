# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

This game is a number guessing challenge built with Streamlit where players try to find a secret number within a limited number of attempts. I investigated and repaired logic glitches around input handling, attempt tracking, and score updates. I also refactored shared game logic into `logic_utils.py` so the UI code in `app.py` stays cleaner and easier to test.

## 📸 Demo

- [ ] Insert a screenshot of the fixed winning game here.
![Winning-game](./winning-game.png)

How to capture demo evidence:
- Run `python -m streamlit run app.py`
- Play until a win state is shown
- Take a screenshot of the success message and score

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
![Edge-Case Testing](./edge-case-testing.png)
