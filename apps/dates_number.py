from datetime import datetime

def main():
    try:
        user_date = input('Please, enter the date in a format DD/MM/YYYY (ex. 25/09/2024): ')
        date = datetime.strptime(user_date, '%d/%m/%Y')
        print(f"The number of the date {date.date()} is {date.strftime('%j')}.")
    except ValueError as ve:
        print(f'Please, enter a valid date ({ve}).')

if __name__ == '__main__':
    main()