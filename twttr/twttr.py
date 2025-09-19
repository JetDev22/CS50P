original = input("Input: ")
cleaned = ""
forbidden = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for char in original:
    if char not in forbidden:
        cleaned = cleaned + char

print(f"Output: {cleaned}")
