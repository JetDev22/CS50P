import re
import sys


def main():
    print(convert(input("Hours: ")))


def cleanTime(time, timeOfDay):
    if ":" in time:
        hour, minute = time.split(":")
        if (int(hour) > 12 or int(minute) > 59 or len(hour) > 2 or len(minute) > 2):
            raise ValueError
        if timeOfDay == "PM":
            hour = str(int(hour) + 12)
            if hour == "24":
                hour = "12"
        else:
            if int(hour) == 12:
                hour = "00"
            else:
                hour = hour.zfill(2)
    elif int(time) <= 12:
        hour = time
        if timeOfDay == "PM":
            hour = str(int(hour) + 12)
            if hour == "24":
                hour = "12"
        else:
            if int(hour) == 12:
                hour = "00"
            else:
                hour = hour.zfill(2)
        minute = "00"
    else:
        raise ValueError
    return f"{hour}:{minute}"


def convert(s):
    try:
        if match := re.match(r"(\d+:?.?\d?.(AM|PM)?.to.\d+:?\d?\d?.(AM|PM)?)", s):
            time = match.group().split()
            try:
                first = cleanTime(time[0], time[1])
                last = cleanTime(time[3], time[4])
            except IndexError:
                raise ValueError
            return f"{first} to {last}"
        else:
            raise ValueError
            sys.exit(0)
    except ValueError:
        raise ValueError
        sys.exit(0)


if __name__ == "__main__":
    main()
