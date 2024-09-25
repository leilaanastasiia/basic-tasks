def main():
    stop = input('Please, tell me where to stop a fibonacci sequence, '
        'because we all need to stop somewhere... (ex. 100): ')
    fibonacci_numbers = [1, 1]
    for i in range(2, int(stop)):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    print(fibonacci_numbers)

if __name__ == '__main__':
    main()