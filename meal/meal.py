def main():
    time = input("What time is it? ")
    cleanTime = convert(time)

    if cleanTime >= 7 and cleanTime <= 8:
        print("breakfast time")
    elif cleanTime >= 12 and cleanTime <= 13:
        print("lunch time")
    elif cleanTime >= 18 and cleanTime <= 19:
        print("dinner time")


def convert(time):
    deconstructed = time.split(":")
    hour = float(deconstructed[0])
    rawMinute = float(deconstructed[1])
    if rawMinute > 0:
        minute = 1/(60/rawMinute)
    else:
        minute = rawMinute
    return float(hour+minute)


if __name__ == "__main__":
    main()
