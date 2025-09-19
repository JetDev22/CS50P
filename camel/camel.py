camel = input("camelCase: ")

snakeCase = ""

for char in camel:
    if char.isupper():
        snakeCase = snakeCase + "_" + char.lower()
    else:
        snakeCase = snakeCase + char

print(snakeCase)
