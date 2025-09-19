import sys

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        result = "Adieu, adieu, to"
        if len(names) == 1:
            result = result + " " + names[0]
        elif len(names) == 2:
            result = result + " " + names[0] + " and " + names[1]
        else:
            end = names.pop()
            for name in names:
                result = result + " " + name + ","
            result = result + " and " + end
        print(f"\n{result}")
        sys.exit(0)
