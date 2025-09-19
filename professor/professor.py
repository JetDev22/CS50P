
import random


def main():
    level = get_level()
    score = 0
    for test in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        attempts = 0
        correct = x + y
        while True:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == correct:
                    score += 1
                    break
                elif guess != correct and attempts < 3:
                    print("EEE")
                    attempts += 1
                    if attempts == 3:
                        print(f"{x} + {y} = {correct}")
                        break
                    else:
                        pass
            except ValueError:
                attempts += 1
                print("EEE")
                if attempts == 3:
                    print(f"{x} + {y} = {correct}")
                    break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in range(1, 4):
                pass
            else:
                break
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level in range(1, 4):
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
        else:
            raise ValueError()


if __name__ == "__main__":
    main()
