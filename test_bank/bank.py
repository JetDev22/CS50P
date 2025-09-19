def main():
    answer = input("Greeting: ").strip().lower()
    print(f"${value(answer)}")


def value(greeting):
    if "hello" in greeting:
        return 0
    elif len(greeting) != 0 and greeting[0] == "h" and "hello" not in greeting:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
