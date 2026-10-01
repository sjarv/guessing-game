#def test_sanity():
#    assert 1 + 1 == 2

#def test_sanity_fails():
#    assert 1 + 1 == 3 

from guessing_game.game import GuessingGame

def test_make_guess_too_low():
    game = GuessingGame(secret_number = 50)
    result = game.make_guess(30)
    assert result == "too low"

def test_make_guess_too_high():
    game = GuessingGame(secret_number = 50)
    result = game.make_guess(59)
    assert result == "too high"

def test_make_guess_correct():
    game = GuessingGame(secret_number = 50)
    result = game.make_guess(50)
    assert result == "correct"

def test_hint_close():
    game = GuessingGame(secret_number = 50)
    game.make_guess(51)
    hint = game.hint()
    assert hint == "You are close."

def test_hint_kinda_close():
    game = GuessingGame(secret_number = 50)
    game.make_guess(61)
    hint = game.hint()
    assert hint == "You are kinda close."

def test_hint_far():
    game = GuessingGame(secret_number = 50)
    game.make_guess(81)
    hint = game.hint()
    assert hint == "You are far."

def test_summary_guess_number():
    game = GuessingGame(secret_number = 50)
    game.make_guess(13)
    game.make_guess(41)
    game.make_guess(45)
    number_of_guesses = len(game.guesses)
    assert number_of_guesses == 3
