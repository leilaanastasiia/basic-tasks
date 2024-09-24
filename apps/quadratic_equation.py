from math import sqrt

def main():
    user_input = input('Please, enter the coefficients of the equation(ex. 3 -7 2): ')
    coefficients = [int(c) for c in user_input.strip().split(sep=' ')]
    a, b, c = coefficients[0], coefficients[1], coefficients[2]
    if a == 0:
        print('"a" can not equals to zero. Try again.')
    else:
        d = b * b - 4 * a * c
        if d < 0:
            print(f'The discriminant ({d}) is less than zero. The equation does not nave any roots.')
        if d == 0:
            x1 = -b / (2 * a)
            print(f'The discriminant equals to {d}. The root is {x1}.')
        if d > 0:
            x1 = round((-b + sqrt(d)) / (2 * a), 1)
            x2 = round((-b - sqrt(d)) / (2 * a), 1)
            print(f'The discriminant equals to {d}. The root is {x1} and {x2}.')


if __name__ == '__main__':
    main()