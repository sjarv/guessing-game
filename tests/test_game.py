import pytest 
from guessing_game.game import GuessingGame

@pytest.fixture
def three_guess_game():
    game = GuessingGame(secret_number = 50)
    game.make_guess(13)
    game.make_guess(41)
    game.make_guess(45)
    return game 

def test_make_guess_too_low(game):
    result = game.make_guess(30)
    assert result == "too low"

def test_make_guess_too_high(game):
    result = game.make_guess(59)
    assert len(game.guesses) == 1
    assert result == "too high"

def test_make_guess_correct(game):
    result = game.make_guess(50)
    assert len(game.guesses) == 1
    assert result == "correct"

def test_hint_close(game):
    game.make_guess(51)
    hint = game.hint()
    assert hint == "You are close."

def test_hint_kinda_close(game):
    game.make_guess(61)
    hint = game.hint()
    assert hint == "You are kinda close."

def test_hint_far(game):
    game.make_guess(81)
    hint = game.hint()
    assert hint == "You are far."

def test_summary_guess_number(three_guess_game):
    number_of_guesses = len(three_guess_game.guesses)
    assert number_of_guesses == 3
