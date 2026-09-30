from guessing_game.game import GuessingGame

def main() -> None:
    game = GuessingGame()
    game.play()
    print(game.summary())
