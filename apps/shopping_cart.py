cart: dict = {}

def main():
    print('Please, enter the name of the product, its amount, and price. '
        '"Stop" as the name to end entering.')
    while True:
        name = input('Name: ')
        if name == 'Stop':
            break
        else:
            amount = int(input('Amount: '))
            price = float(input('Price: '))
            cart[name] = {'amount': amount,
                        'price': price}
    print('The products and their prices are listed below:')
    user_cart = make_check(cart)
    for key, value in user_cart.items():
        print(f'{key}: {value}')
    total_price = sum(user_cart.values())
    print(f'The total price is {total_price}.')


def make_check(cart: dict):
    check = {}
    for key, value in cart.items():
        check[key] = value['amount'] * value['price']
    return check


if __name__ == '__main__':
    main()