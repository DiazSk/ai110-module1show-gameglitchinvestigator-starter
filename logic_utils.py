def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 500
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    cleaned = raw.strip()
    if cleaned == "":
        return False, None, "Enter a guess."

    if "." in cleaned:
        return False, None, "Use a whole number (no decimals)."

    try:
        value = int(cleaned)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        return current_score + max(10, points)

    if outcome in {"Too High", "Too Low"}:
        return current_score - 5

    return current_score
