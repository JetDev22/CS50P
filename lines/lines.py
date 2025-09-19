import sys

# check that correct arguments given
if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)
elif "py" not in sys.argv[1] and len(sys.argv) == 2:
    print("Not a Python file")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)


# open python file and check count lines
try:
    codeOnly = []
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.lstrip().startswith("#"):
                pass
            elif len(line.lstrip()) == 0:
                pass
            else:
                codeOnly.append(line)
    print(len(codeOnly))

except FileNotFoundError:
    print("File does not exist")
