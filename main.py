from apps import (
    perfect_weight,
    triangle_area,
    # right_triangle,
    # quadratic_equation,
    # shopping_cart,
    # dates_number,
    # months_30_days,
    # array_to_100,
    # fibonacci_numbers,
    # vowels
)

def main():
    apps = {
        'perfect_weight': perfect_weight.main,
        'triangle_area': triangle_area.main,
        # 'right_triangle': right_triangle.main,
        # 'quadratic_equation': quadratic_equation.main,
        # 'shopping_cart': shopping_cart.main,
        # 'dates_number': dates_number.main,
        # 'months_30_days.py': months_30_days.main,
        # 'array_to_100': array_to_100.main,
        # 'fibonacci_numbers': fibonacci_numbers.main,
        # 'vowels': vowels.main
    }
    print('Available apps:', *apps.keys(), sep='\n')
    user_input: input = input('Please, enter an app name to run: ')

    if user_input in apps:
        apps[user_input]()
    else:
        print("Wrong input")

if __name__ == '__main__':
    while True:
        main()
