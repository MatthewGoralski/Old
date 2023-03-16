def add_comma():
    with open("input.txt", "r") as f:
        input_string = f.read()
    words = input_string.split()
    return ', '.join(words)

print(add_comma())