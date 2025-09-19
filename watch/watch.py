import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'^<iframe.+youtube\.com/embed/([\w-]+).+</iframe>$', s):
        videoURL = match.group(1)
        return f"https://youtu.be/{videoURL}"
    else:
        return None


if __name__ == "__main__":
    main()
