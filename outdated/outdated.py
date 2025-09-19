validMonths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    try:
        userDate = input("Date: ").strip()
        if "/" in userDate:
            userDate = userDate.split("/")
            if (
                int(userDate[0]) <= 12
                and int(userDate[1]) <= 31
                and userDate[0] not in validMonths
            ):
                print(
                    f"{userDate[2]}-{userDate[0].zfill(2)
                                       }-{userDate[1].zfill(2)}"
                )
                break
            else:
                pass
        elif "," in userDate:
            userDate = userDate.split()
            if (
                userDate[0] in validMonths
                and "," in userDate[1]
                and int(userDate[1].strip(",")) <= 31
            ):
                print(
                    f"{userDate[2]}-{str(validMonths.index(userDate[0]
                                                             )+1).zfill(2)}-{userDate[1].strip(",").zfill(2)}"
                )
                break
            else:
                pass
        else:
            pass
    except ValueError:
        pass
