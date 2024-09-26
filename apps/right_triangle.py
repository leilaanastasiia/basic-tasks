import math

def get_parameters():
    try:
        user_input = input('Please, enter sides of your triangle in cm (ex. 10 10 14.14): ').strip().split()
        parsed_data = [float(p) for p in user_input]
        parsed_data.sort()
        return parsed_data
    except ValueError:
        print("Please, enter 3 valid numbers ")
        return None


def is_equilateral_triangle(a, b, c):
        return a == b == c

def is_right_triangle(a, b, c, tolerance=0.01):
    return math.isclose(a ** 2 + b ** 2, c ** 2, rel_tol=tolerance)

def is_isosceles_triangle(a, b, c):
    return a == b and a != c or b == c and b != a


def main() -> None:
    parsed = get_parameters()
    a, b, c = parsed[0], parsed[1], parsed[2]
    if is_equilateral_triangle(a, b, c):
        print('This is an equilateral triangle.')
    elif is_right_triangle(a, b, c):
        print('This is a right triangle.')
        if is_isosceles_triangle(a, b, c):
            print('And an isosceles triangle as well.')
    elif is_isosceles_triangle(a, b, c):
        print('This is an isosceles triangle.')
    else:
        print("This is not a right triangle.")

if __name__ == '__main__':
    main()