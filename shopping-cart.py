# design shopping cart mechanism for online shopping site where items with details
# (item_name, quantity , price) can be added in cart, can be removed from cart, bill of total items can be calculated
import json


def item(item_name: str, quantity: int, price: float):
    return {
        'item_name': item_name,
        'quantity': quantity,
        'price': price
    }


def main():
    cart = []
    while True:
        print('1. Add item   2. Remove item   3. View cart & total   4. Exit')
        choice = input('Enter choice: ')[0]

        if choice == '1':
            # TODO: Adding item to cart
            item_name = input('Enter item name: ')
            quantity = input('Enter quantity: ')
            price = input('Enter price: Rs. ')

            cart.append(
                item(item_name, int(quantity), float(price))
            )
            print('Inserted!')

        elif choice == '2':
            # TODO: Removing item from cart
            flag: bool = False
            item_name = input('Enter item name: ')
            for item_ in cart:
                if item_['item_name'] == item_name:
                    flag = True
                    cart.remove(item_)

            print('Removed!') if flag else print('Item not found!')

        elif choice == '3':
            # TODO: Displaying cart and calculating total
            print(json.dumps(cart, indent=2))

            total = 0
            for item_ in cart:
                total += item_['price'] * item_['quantity']
            print('=' * 25)
            print('Cart total: Rs.', total)

        elif choice == '4':
            exit(0)
        else:
            print('Invalid choice!')


main()
