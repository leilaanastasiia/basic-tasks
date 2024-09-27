def main():
    try:
        base, height = input('Please, enter base, height of your triangle in cm (ex. 2 5): ').strip().split()
        area = 0.5 * float(base) * float(height)
        print(f'The area of your triangle is {area:.2f} cm\u00b2.')
    except ValueError:
        print("Please, enter 2 valid numbers.")


if __name__ == '__main__':
    main()