import sys
import csv


def main():
    checkArgs()
    correct = getAndEditOrigin()
    createNewCsv(correct)


def checkArgs():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    return


def getAndEditOrigin():
    try:
        new = []
        with open(sys.argv[1], "r") as source:
            reader = csv.DictReader(source)
            for row in reader:
                complete = row["name"].split(",")
                corrected = {"first": complete[1].lstrip(
                ), "last": complete[0], "house": row["house"]}
                new.append(corrected)
        return new
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)


def createNewCsv(corrected):
    with open(sys.argv[2], "w") as new:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(new, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(corrected)


if __name__ == "__main__":
    main()
