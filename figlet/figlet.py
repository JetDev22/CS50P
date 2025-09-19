import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()
validArgs = ["-f", "--font"]

if len(sys.argv) == 1:
    userInput = input("Input: ")
    figlet.setFont(font=choice(fonts))
    print(f"Output:\n{figlet.renderText(userInput)}")
elif (len(sys.argv) == 3 and sys.argv[1] in validArgs and
      sys.argv[2] in fonts):
    userInput = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(f"Output:\n{figlet.renderText(userInput)}")
else:
    sys.exit(1)
