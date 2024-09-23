def main():
    parameters = input('Please, enter an a & h of your triangle in cm (ex. 2 5): ')
    a, h = parameters.strip().split(sep=' ')
    area = 1/2 * int(a) * int(h)
    print(f'The area of your triangle is {area} cm\u00b2.')


if __name__ == '__main__':
    main()