from apps import perfect_weight, triangle_area, months_30_days

options: list = ['perfect_weight', 'triangle_area', 'months_30_days']

def main():
    print('Available apps:', *options, sep='\n')
    user_input: input = input('Please, enter an app name to run: ')

    """
    I was thinking about a better way to choose an app, not an explicit manual one. 
    But I haven't found something useful. 
    Maybe you have any ideas? 
    """

    if user_input in options:
        if user_input == 'perfect_weight':
            perfect_weight.main()
        elif user_input == 'triangle_area':
            triangle_area.main()
        elif user_input == 'months_30_days':
            months_30_days.main()
    else:
        print("Wrong input")

if __name__ == '__main__':
    main()