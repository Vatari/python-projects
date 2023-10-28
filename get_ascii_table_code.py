while True:
    letter = input()

    if letter == "end":
        break

    for symbol in letter:
        print(f"ASCII Code: {ord(symbol)}", end=" ")
