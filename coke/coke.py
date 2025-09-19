due = 50

while due > 0:
    print(f"Amount Due: {due}")
    given = int(input("Insert Coin: "))

    if given == 25 or given == 10 or given == 5:
        due = due - given
        if due <= 0:
            print(f"Change Owed: {due * -1}")
