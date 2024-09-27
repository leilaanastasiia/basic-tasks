import string

def filter_vowels():
    alphabet = {v: k for k, v in enumerate(string.ascii_uppercase, start=1)}
    vowels = ['A', 'E', 'I', 'O', 'U']
    return  {k : v for k, v in alphabet.items() if k in vowels}

def main():
    vowels = filter_vowels()
    print(vowels)


if __name__ == '__main__':
    main()