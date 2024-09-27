def make_calendar() -> dict:
    months_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                    'September', 'October', 'November', 'December']
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    calendar = dict((k, v) for k, v in zip(months_names, days_in_month))
    return calendar



def main():
    calendar = make_calendar()
    days = input('Please enter a number of days in months of 2024 year: ')
    filtered = {k: v for k, v in calendar.items() if v == int(days)}
    if len(filtered) == 0:
        filtered = {'Result': 'Sorry, no month with this value was found.'}
    print(*filtered.keys(), sep='\n')


if __name__ == '__main__':
    main()