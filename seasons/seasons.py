from datetime import date
import inflect
import sys


def main():
    birthday = checkDate(input("Date of Birth: "))
    today = date.today()
    checkDate(birthday)
    print(convert(birthday, today))


def checkDate(birthday):
    try:
        # Format YYYY-MM-DD
        if "-" not in birthday:
            sys.exit("Invalid Date")
        deconstructed = birthday.split("-")
        if (len(deconstructed[0]) < 4 or int(deconstructed[1]) < 1
            or int(deconstructed[1]) > 12 or int(deconstructed[2]) < 1
                or int(deconstructed[2]) > 31):
            sys.exit("Invalid Date")
        return birthday
    except ValueError:
        sys.exit("Invalid Date")


def convert(birthday, today):
    birthday = date.fromisoformat(birthday)
    today = date.fromisoformat(str(today))
    delta = today - birthday
    minutes = int(delta.days) * 24 * 60
    inflector = inflect.engine()
    return f"{inflector.number_to_words(minutes, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()
