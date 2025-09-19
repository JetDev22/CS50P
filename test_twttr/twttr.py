def main():
    userEntry = input("Input: ")
    print(f"Output: {shorten(userEntry)}")


def shorten(word):
    cleaned = ""
    forbidden = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for char in word:
        if char not in forbidden:
            cleaned = cleaned + char
    return cleaned


if __name__ == "__main__":
    main()
