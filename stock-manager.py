from os import system                # Import system function to clear the console screen
from random import randint           # Import randint to generate random integer codes
from math import inf                 # Import infinity constant for input range checks


def input_digit_verifier(prompt: str, data_type: str, params=[0]):
    """
    Verifies and returns a numeric input from the user.
    - If data_type is 'Float', accepts float values (commas replaced with dots).
    - If data_type is 'Int', accepts integer values, optionally within a range specified by params.
    """
    if data_type == 'Float':
        while True:
            system('cls')                              # Clear console before each prompt
            user_input = input(prompt)                 # Prompt user for input
            user_input = user_input.replace(',', '.')  # Replace commas with dots for float parsing
            response = None

            # Check if the cleaned input represents a valid float
            if user_input.isdigit() or user_input.replace('.', '').isdigit():
                response = float(user_input)

            if response is not None:
                return response                         # Return the parsed float once valid

    elif data_type == 'Int':
        while True:
            system('cls')                              # Clear console before each prompt
            user_input = input(prompt)                 # Prompt user for input
            response = None

            # Check if the input is a valid integer string
            if user_input.isdigit():
                response = int(user_input)

            # If a range (min, max) is provided, enforce it
            if len(params) > 1:
                if response is not None and response > params[0] and response <= params[1]:
                    return response                     # Return integer if within the specified range
            else:
                if response is not None:
                    return response                     # Return integer if no range constraints


def input_code_verifier(prompt: str, inventory):
    """
    Verifies that the user enters a valid integer code.
    Returns -1 if the user inputs -1 to indicate “go back,” or returns a code that exists in the current inventory.
    """
    while True:
        system('cls')                                  # Clear console before each prompt
        user_input = input(prompt)                     # Prompt user for code input
        code = None

        if user_input.isdigit():
            code = int(user_input)                     # Convert input to integer if valid digits

        # If user explicitly enters -1, return -1 to signal “go back”
        if code is not None and code == -1:
            return -1

        # Check if the entered code matches any existing product code
        if code is not None and any(item['code'] == code for item in inventory):
            return code                                # Return the valid code
        else:
            invalid_option()                           # Otherwise, notify invalid option and loop again


def invalid_option():
    """
    Informs the user that their choice was invalid, then waits for them to press '1' to return.
    """
    while True:
        system('cls')                                  # Clear console
        user_input = input('Invalid option!\nEnter "1" to return\nR: ')
        choice = None

        if user_input.isdigit():
            choice = int(user_input)

        # When the user enters 1, break out and return control to the previous menu
        if choice == 1:
            break


def press_enter_to_return(message: str):
    """
    Displays a message to the user and waits for them to enter '1' to return to the main menu.
    """
    while True:
        user_input = input(f'\n{message}\nEnter "1" to return\nR: ')
        choice = None

        if user_input.isdigit():
            choice = int(user_input)

        if choice == 1:
            break                                      # Return once the user presses 1


def remove_from_inventory(code: int, inventory):
    """
    Removes the item with the given code from the inventory list.
    """
    for item in inventory:
        if item['code'] == code:
            index = inventory.index(item)              # Find the index of the matching item
            inventory.pop(index)                       # Remove it from the list
            break                                      # Stop looping after removal


def add_to_inventory(name: str, quantity: int, inventory, price=0):
    """
    Adds a new item to the inventory with an auto-generated 5-digit code.
    If price > 0, includes the price field; otherwise, omits it.
    """
    while True:
        code = randint(10000, 99999)                  # Generate a random 5-digit code
        exists = any(item['code'] == code for item in inventory)
        if not exists:                                # Ensure the generated code is unique
            break

    # Build the product dictionary, including price if provided
    if price > 0:
        product = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'code': code
        }
    else:
        product = {
            'name': name,
            'quantity': quantity,
            'code': code
        }

    inventory.append(product)                         # Add the new product to the inventory list


def change_attribute(code: int, attribute: str, new_value, inventory):
    """
    Updates the specified attribute of the item with the given code in the inventory.
    """
    for item in inventory:
        if item['code'] == code:
            item[attribute] = new_value                # Set the new attribute value
            break                                      # Stop once updated


def main():
    inventory = []                                   # Initialize empty inventory list

    while True:
        # Repeatedly display inventory contents until a valid menu option is chosen
        while True:
            system('cls')                            # Clear screen before displaying inventory

            # If the inventory is empty, show a placeholder message
            if len(inventory) == 0:
                print('\n* Inventory *\n\nEMPTY')
            else:
                # Otherwise, list each item with its details
                print('\n* Inventory *')
                for item in inventory:
                    try:
                        # If the item has a price, print name, price, quantity, and code
                        print(
                            f"\nName: {item['name']}\n"
                            f"Price: {item['price']}\n"
                            f"Quantity: {item['quantity']}\n"
                            f"Code: {item['code']}"
                        )
                    except KeyError:
                        # If no price field exists, print name, quantity, and code only
                        print(
                            f"\nName: {item['name']}\n"
                            f"Quantity: {item['quantity']}\n"
                            f"Code: {item['code']}"
                        )

            print('\n-------------------------------------------')

            # Display the main menu prompt
            user_input = input(
                '\n* Stock Manager *\n\n'
                '1- Add Product to Inventory\n'
                '2- Remove Product from Inventory\n'
                '3- Change Item Attributes\n'
                '4- Exit\n\nR: '
            )

            menu_choice = None
            if user_input.isdigit():
                menu_choice = int(user_input)          # Convert the choice to integer if valid

            # Only accept choices 1–4
            if menu_choice is not None and 1 <= menu_choice <= 4:
                break                                 # Exit the inner loop when a valid option is chosen

        # Handle each menu option
        if menu_choice == 4:
            system('cls')
            print('\nProgram terminated!')           # Notify the user the program is ending
            break                                   # Exit the outer loop and end program

        elif menu_choice == 1:
            # Option 1: Add a new product to inventory
            system('cls')
            name = input('\nEnter the item name\nR: ')  # Ask for product name

            include_price = input_digit_verifier(
                '\nWould you like to specify the product price?\n\n'
                '1- Yes\n2- No\nR: ',
                'Int',
                [0, 2]
            )

            if include_price == 1:
                # If user chooses to include a price, prompt for price and quantity
                price = input_digit_verifier(
                    f'\nItem name: {name}\n\nEnter the item price\nR: ',
                    'Float',
                    [0, inf]
                )
                quantity = input_digit_verifier(
                    f'\nItem name: {name}\nItem price: {price}\n\n'
                    'Enter the quantity of this item in stock\nR: ',
                    'Int',
                    [0, inf]
                )
            else:
                # Otherwise, only prompt for quantity
                quantity = input_digit_verifier(
                    f'\nItem name: {name}\n\n'
                    'Enter the quantity of this item in stock\nR: ',
                    'Int',
                    [0, inf]
                )
                price = 0                             # Default price to zero if not provided

            add_to_inventory(name, quantity, inventory, price)  # Add the new product object
            press_enter_to_return('\nItem added successfully!')  # Confirmation message

        elif menu_choice == 2:
            # Option 2: Remove a product from inventory
            if len(inventory) == 0:
                # If inventory is empty, inform the user to add a product first
                press_enter_to_return('Add a product first before attempting to remove!')
            else:
                code = input_code_verifier(
                    '\nEnter the code of the product you want to remove, or enter "-1" to return\nR: ',
                    inventory
                )
                if code != -1:
                    remove_from_inventory(code, inventory)   # Delete the matching product
                    press_enter_to_return('Item removed successfully!')

        elif menu_choice == 3:
            # Option 3: Change attributes of an existing item
            if len(inventory) == 0:
                # If no products exist, inform user to add first
                press_enter_to_return('Add a product first before changing attributes!')
            else:
                code = input_code_verifier(
                    '\nEnter the code of the product you want to modify, or enter "-1" to return\nR: ',
                    inventory
                )

                # Locate the index of the item with the matching code
                for i, item in enumerate(inventory):
                    if item['code'] == code:
                        index = i
                        break

                if code != -1:
                    # Loop until the user exits the attribute-edit menu
                    while True:
                        # If the item has a price field, show price in the menu
                        if 'price' in inventory[index]:
                            attribute_choice = input_digit_verifier(
                                f"Name: {inventory[index]['name']}\n"
                                f"Price: {inventory[index]['price']}\n"
                                f"Quantity: {inventory[index]['quantity']}\n"
                                f"Code: {inventory[index]['code']}\n\n"
                                'Which attribute would you like to change?\n\n'
                                '1- Name\n'
                                '2- Price\n'
                                '3- Quantity\n'
                                '4- Exit\nR: ',
                                'Int',
                                [0, 4]
                            )
                        else:
                            # If no price field, only show name, quantity, and code
                            attribute_choice = input_digit_verifier(
                                f"Name: {inventory[index]['name']}\n"
                                f"Quantity: {inventory[index]['quantity']}\n"
                                f"Code: {inventory[index]['code']}\n\n"
                                'Which attribute would you like to change?\n\n'
                                '1- Name\n'
                                '2- Price\n'
                                '3- Quantity\n'
                                '4- Exit\nR: ',
                                'Int',
                                [0, 4]
                            )

                        # Process the chosen attribute
                        if attribute_choice == 1:
                            attribute = 'name'
                            new_value = input('\nEnter the new item name\nR: ')

                        elif attribute_choice == 2:
                            attribute = 'price'
                            # Check if the item actually has a price field
                            has_price = any(
                                'price' in item and item['code'] == code
                                for item in inventory
                            )

                            if not has_price:
                                # If no price attribute exists, return to menu
                                press_enter_to_return('This item does not have a price attribute!')
                                break

                            # Otherwise, prompt for new price
                            new_value = input_digit_verifier(
                                '\nEnter the new price for the item\nR: ',
                                'Float',
                                [0, inf]
                            )

                        elif attribute_choice == 3:
                            attribute = 'quantity'
                            # Prompt for new quantity
                            new_value = input_digit_verifier(
                                '\nEnter the new quantity for the item\nR: ',
                                'Int'
                            )

                        else:
                            break                             # Exit attribute edit loop if choice is 4

                        # Apply the change to the inventory
                        change_attribute(code, attribute, new_value, inventory)
                        press_enter_to_return('Attribute changed successfully!')


if __name__ == "__main__":
    main()                                              # Run the main function only if this script is executed directly
