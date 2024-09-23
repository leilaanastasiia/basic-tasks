def main():
    user_name: str = input('Please, enter your name: ')
    user_height: str = input('Now enter your height in cm (ex. 165): ')
    ideal_weight = int(user_height) - 110
    if ideal_weight >= 0:
        print(f'{user_name}, your perfect weight is {ideal_weight} kg.')
    else:
        print(f"{user_name}, your weight is already lower than optimal. Maybe, you should gain {abs(ideal_weight)} kg.")


if __name__ == '__main__':
    main()