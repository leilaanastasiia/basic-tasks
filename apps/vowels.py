import string

def main():
    alphabet = {}
    for i, latter in enumerate(string.ascii_uppercase, start=1):
        alphabet[latter] = i
    vowels = ['A', 'E', 'I', 'O', 'U']
    output = {k : v for k, v in alphabet.items() if k in vowels}
    print(output)


if __name__ == '__main__':
    main()