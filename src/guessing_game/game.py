import random
#random.seed(31)

class GuessingGame :

    def __init__(self, secret_number = None, max_attempts = 5, guesses = None):
        self.secret_number = random.randint(1,100) if secret_number is None else secret_number
        self.max_attempts = max_attempts 
        self.guesses = guesses if guesses is not None else []

    def make_guess(self, guess):
        self.guesses.append(guess)
        if guess == self.secret_number:
            return "correct"
        elif guess > self.secret_number:
            return "too high"
        else :
            return "too low"

    def play(self):
        for attempt in range(1, self.max_attempts + 1):
            user_guess = int(input("Enter an integer between 1 and 100, inclusive."))
            result = self.make_guess(user_guess)
            print(f"Your guess was {result}.")
            if result == "correct":
                print(f"You won!")
                break
        else :
            print(f"You are out of guesses. The secret number was {self.secret_number}.")

    def summary(self):
        number_of_guesses = len(self.guesses)
        minimal_guess = min([abs(x - self.secret_number) for x in self.guesses])
        no_min_dict = {"Number of guesses" : number_of_guesses, "Closest guess distance" : minimal_guess}
        guess_dict = {}
        for index, value in enumerate(self.guesses, 1):
            guess_dict["Guess " + str(index)] = value
        return no_min_dict | guess_dict 

#game1 = GuessingGame(secret_number = 17)
#game1.play()
#print(game1.summary())

#game2 = GuessingGame(secret_number = 55)
#game2.play()
#print(game2.summary())
