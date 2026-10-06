import pytest
from guessing_game.game import GuessingGame

@pytest.fixture
def game():
    return GuessingGame(secret_number = 50)
