def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    fraction = fraction.split("/")
    if len(fraction) == 2 and "-" not in fraction[0] and "-" not in fraction[1]:
        x = int(fraction[0])
        y = int(fraction[1])
        if y == 0:
            raise ZeroDivisionError
        else:
            return round(x / y * 100)
    else:
        raise ValueError


def gauge(percentage):
    if percentage >= 90 and percentage <= 100:
        return "F"
    elif percentage <= 1 and percentage >= 0:
        return "E"
    elif percentage > 1 and percentage < 90:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
