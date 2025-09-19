groceryList = {}

while True:
    try:
        grocery = input()
    except EOFError:
        break
    else:
        grocery = grocery.upper()
        if grocery in groceryList:
            groceryList[grocery] += 1
        else:
            groceryList[grocery] = 1

sortedGrocery = dict(sorted(groceryList.items()))
for key in sortedGrocery:
    print(f"{sortedGrocery[key]} {key}")
