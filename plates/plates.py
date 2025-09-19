def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2:
        return False
    invalids = [".", ",", " ", "_", "-", ":", ";"]
    digitFound = False
    if s[0].isalpha() and s[1].isalpha() and len(s) >= 2 and len(s) <= 6:
        for char in s:
            if char in invalids:
                return False
            if char == "0" and digitFound is False:
                return False
            if char.isdigit():
                digitFound = True
            if digitFound is True and char.isalpha():
                return False
        return True
    else:
        return False


main()
