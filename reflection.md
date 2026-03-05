# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I started, game logic lived inside `app.py` while `logic_utils.py` was mostly stubbed with `NotImplementedError`, which made the code harder to test and maintain. I also noticed that attempts were being counted before input validation, so invalid entries could consume turns. Decimal input like `42.5` was quietly converted to an integer, which gave confusing behavior instead of a clear validation error. The score rules for high/low guesses were inconsistent and could reward wrong guesses on specific turns.

---

## 2. How did you use AI as a teammate?

I used Claude Code to reason through each bug and to propose refactoring steps from UI code to utility functions. A correct suggestion was to move `parse_guess`, `get_range_for_difficulty`, and `update_score` into `logic_utils.py` and import them in `app.py`, which made testing much easier. A misleading suggestion I rejected was to keep coercing decimal strings into integers for convenience; that hides bad input and creates confusing outcomes for players. I verified each accepted suggestion by running `pytest` and checking that behavior matched expected game rules.

---

## 3. Debugging and testing your fixes

I validated fixes in two ways: automated tests and logic review in `app.py`. I added new pytest cases to confirm decimal inputs are rejected, integer inputs parse correctly, and score updates are consistent for wins and non-win hints. I also changed the submit flow so attempts increment only after a valid, in-range guess. After these changes, all tests pass with `pytest -q`, which confirms the repaired logic works as expected.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script on each interaction, so state must be carefully managed in `st.session_state`. The order of operations matters: when counters update before validation, the UI can show unfair attempt loss. I also learned to keep game rules in pure functions and keep the UI layer focused on interaction and display. That separation makes state bugs easier to isolate.

---

## 5. Looking ahead: your developer habits

I want to keep the habit of writing or updating tests immediately after each fix so regressions are caught quickly. I also learned to treat AI suggestions as drafts that need verification, not as final truth. For future projects, I will ask AI to explain tradeoffs and edge cases before applying large edits. That helps me stay responsible for the final code quality.
