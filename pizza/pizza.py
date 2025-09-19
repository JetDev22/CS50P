import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif ".csv" not in sys.argv[1]:
    print("Not a csv file")
    sys.exit(1)

try:
    with open(sys.argv[1], "r") as menu:
        reader = csv.DictReader(menu)
        print(tabulate(reader, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
