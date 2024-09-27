def get_cart() -> dict:
    cart: dict = {}
    while True:
        name = input('Name: ')
        if name == 'Stop':
            break
        else:
            amount, price = int(input('Amount: ')),  float(input('Price: '))
            cart[name] = {'amount': amount,
                        'price': price}
    return cart

def make_check(cart: dict) -> dict:
    check = {}
    for key, value in cart.items():
        check[key] = value['amount'] * value['price']
    return check


def main() -> None:
    print('Please, enter the name of the product, its amount, and price. '
        '"Stop" as the name to end entering.')
    check = make_check(get_cart())
    print('The products and their prices are listed below:')
    for key, value in check.items():
        print(f'{key}: {value}')
    total_price = sum(check.values())
    print(f'The total price is {total_price}.')


if __name__ == '__main__':
    main()