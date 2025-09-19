import random
import sys

while True:
    try:
        n = int(input("Level: "))
        if n < 1:
            pass
        else:
            target = random.randint(1, n)
            while True:
                guess = int(input("Guess: "))
                if guess <= 0:
                    pass
                elif guess > target:
                    print("Too large!")
                elif guess < target:
                    print("Too small!")
                elif guess == target:
                    print("Just right!")
                    sys.exit(0)
    except ValueError:
        pass
