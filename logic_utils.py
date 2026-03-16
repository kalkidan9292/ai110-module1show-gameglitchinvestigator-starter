# FIX: Refactored core game logic from app.py into logic_utils.py
# using Copilot suggestions to separate UI code from game logic.
def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


# FIX: Restricted guesses to integers only.
# Originally the code converted decimals like 31.5 into integers.
# After testing the game manually, we updated parsing to reject decimals.
def parse_guess(raw: str):
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except Exception:
        return False, None, "Please enter a whole number."

    return True, value, None


# FIX: Corrected hint direction after noticing the game said
# "Go HIGHER" when the guess was already higher than the secret.
# Used Copilot to review the logic and confirm the comparison conditions.
def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score