def main() -> None:
    user_input = input('Please, enter sides of your triangle in cm (ex. 10 10 14.14): ')
    parameters = [float(p) for p in user_input.strip().split(sep=' ')]
    parameters.sort()
    a, b, c = parameters[0], parameters[1], parameters[2]
    if a == b == c:
        print('This is an equilateral triangle.')
    elif round(a * a + b * b) == round(c * c):
        print('This is a right triangle.')
        if a == b and a != c or b == c and b != a:
            print('And an equilateral triangle as well.')
    elif a == b and a != c or b == c and b != a:
        print('This is an isosceles triangle.')
    else:
        print("This is not a right triangle.")

if __name__ == '__main__':
    main()