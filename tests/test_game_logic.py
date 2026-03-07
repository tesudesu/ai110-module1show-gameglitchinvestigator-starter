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


