answer = input("Greeting: ").strip().lower()
if "hello" in answer:
    print("$0")
elif answer[0] == "h" and "hello" not in answer:
    print("$20")
else:
    print("$100")
