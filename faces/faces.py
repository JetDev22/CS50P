def convert(entry):
    entry = entry.replace(":)", "🙂")
    entry = entry.replace(":(", "🙁")
    return entry


def main():
    entry = input()
    print(convert(entry))


main()
