import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit(0)


def validate(ip):
    valid = True
    if match := re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        foundIP = match.group().split(".")
        if foundIP[0] == "000":
            valid = False
            return valid
        for digit in foundIP:
            if int(digit) >= 0 and int(digit) <= 255:
                pass
            else:
                valid = False
                return valid
    else:
        valid = False
        return valid
    return valid


if __name__ == "__main__":
    main()
