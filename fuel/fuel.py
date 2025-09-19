while True:
    fraction = input("Fraction: ")
    fraction = fraction.split("/")

    if len(fraction) == 2:
        try:
            x = int(fraction[0])
            y = int(fraction[1])
            result = round(x/y*100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if result >= 90 and result <= 100:
                print("F")
                break
            elif result <= 1 and result >= 0:
                print("E")
                break
            elif result > 1 and result < 90:
                print(f"{result}%")
                break
            else:
                pass
