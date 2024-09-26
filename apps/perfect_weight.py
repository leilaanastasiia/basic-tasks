def main():
    user_name, user_height = input('Please, enter your name and height: (ex. Mark 179)').split()
    ideal_weight = int(user_height) - 110
    if ideal_weight >= 0:
        print(f'{user_name}, your perfect weight is {ideal_weight} kg.')
    else:
        print(f"{user_name}, your weight is already lower than optimal. Maybe, you should gain {abs(ideal_weight)} kg.")


if __name__ == '__main__':
    main()