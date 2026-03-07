from logic_utils import check_guess, parse_guess

# When Enter is pressed, the form submits the raw text input to parse_guess.
# These tests verify that parse_guess correctly handles what the user typed.

def test_parse_guess_valid_number():
    # Typing "42" and pressing Enter should yield a valid int guess
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty_string():
    # Pressing Enter with an empty input should return an error, not crash
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_non_numeric():
    # Pressing Enter with text like "abc" should return a clear error
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_decimal():
    # Typing "7.9" and pressing Enter should truncate to int 7
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7
    assert err is None



def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests for the hint message bug fix (messages were previously inverted)

def test_too_high_message_says_go_lower():
    # When guess is too high, the message should tell player to go LOWER
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # When guess is too low, the message should tell player to go HIGHER
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Tests for the int vs string bug fix (secret was cast to str on even attempts)

def test_check_guess_both_ints():
    # Both guess and secret should always be ints; comparison must be numeric not lexicographic
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"  # "9" > "10" lexicographically but 9 < 10 numerically

def test_check_guess_secret_is_int_not_string():
    # Passing secret as int (not str) should work correctly
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"