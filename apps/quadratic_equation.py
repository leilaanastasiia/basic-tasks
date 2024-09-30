from math import sqrt

def get_parameters():
    try:
        user_input = input('Please, enter the coefficients of the equation(ex. 3 -7 2): ').strip().split()
        parsed = [int(c) for c in user_input]
        return parsed
    except ValueError:
        print('Please enter only numbers.')


def calculate_discriminant(a, b, c) -> int:
    return b * b - 4 * a * c

def one_root(a, b) -> int:
    root = -b / (2 * a)
    return root

def two_roots(a, b, d) -> dict[str, int]:
    root1 = (-b + sqrt(d)) / (2 * a)
    root2 = (-b - sqrt(d)) / (2 * a)
    return {
        'root1': root1,
        'root2': root2,
            }

def main() -> None:
    parsed = get_parameters()
    if len(parsed) == 3:
        if parsed[0] == 0:
            print('"a" can not equals to zero. Try again.')
        else:
            a, b, c = parsed[0], parsed[1], parsed[2]
            d = calculate_discriminant(a, b, c)
            if d < 0:
                print(f'The discriminant ({d}) is less than zero. The equation does not nave any roots.')
            if d == 0:
                root = one_root(a, b)
                print(f'The discriminant equals to {d}. The root is {root}.')
            if d > 0:
                root1, root2 = two_roots(a, b, d).values()
                print(f'The discriminant equals to {d}. The root is {root1:.1f} and {root2:.1f}.')
    else:
        print('Please enter 3 numbers.')


if __name__ == '__main__':
    main()