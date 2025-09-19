import sys
from PIL import Image
from PIL import ImageOps


def main():
    checkArgs()
    editImage()


def checkArgs():
    validFiles = ["jpeg", "jpg", "png"]
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) == 3:
        try:
            file1 = sys.argv[1].lower().split(".")[1]
            file2 = sys.argv[2].lower().split(".")[1]
            if file1 not in validFiles or file2 not in validFiles:
                print("Invalid input")
                sys.exit(1)
            elif file1 != file2:
                print("Input and output have different extensions")
                sys.exit(1)
        except IndexError:
            print("Invalid input")
            sys.exit(1)


def editImage():
    image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    imageAdjusted = ImageOps.fit(image, size)
    imageAdjusted.paste(shirt, shirt)
    imageAdjusted.save(sys.argv[2])


if __name__ == "__main__":
    main()
