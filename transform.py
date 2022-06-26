while True:
    text = input('enter some text: ')
    print("1. to lower case")
    print("2. to upper case")
    method = int(input('method: '))

    if method == 1:
        print(text.lower())
    if method == 2:
        print(text.upper())
