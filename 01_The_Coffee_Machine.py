coffees = [
    {
        'name': 'espresso',
        'water': 50,
        'milk': 0,
        'coffee': 18,
        'price': 1.5
    },
    {
        'name': 'latte',
        'water': 200,
        'milk': 150,
        'coffee': 24,
        'price': 2.5
    },
    {
        'name': 'cappuccino',
        'water': 250,
        'milk': 100,
        'coffee': 24,
        'price': 3.0
    }
]

vending_machine = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}

coin_operated = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}

def report_machine():
    print("Coffee Machine Report")
    print(f"Water: {vending_machine['water']}ml")
    print(f"Milk: {vending_machine['milk']}ml")
    print(f"Coffee: {vending_machine['coffee']}g")

def check_resources(coffee_name):
    for item in coffees:
        if item['name'] == coffee_name:
            if item['water'] > vending_machine['water']:
                print("Sorry, there is not enough water.")
                return False
            if item['milk'] > vending_machine['milk']:
                print("Sorry, there is not enough milk.")
                return False
            if item['coffee'] > vending_machine['coffee']:
                print("Sorry, there is not enough coffee.")
                return False
            return True

def resources_reduction(coffee_name):
    for item in coffees:
        if item['name'] == coffee_name:
            vending_machine['water'] -= item['water']
            vending_machine['milk'] -= item['milk']
            vending_machine['coffee'] -= item['coffee']

def coins_operated():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * coin_operated['quarters'] +
             dimes * coin_operated['dimes'] +
             nickles * coin_operated['nickles'] +
             pennies * coin_operated['pennies'])
    return total

def command_coffee_machine():
    user_command = ""
    while user_command != 'off':
        user_command = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
        if user_command in ['espresso', 'latte', 'cappuccino']:
            if check_resources(user_command):
                payment = coins_operated()
                for item in coffees:
                    if item['name'] == user_command:
                        if payment >= item['price']:
                            resources_reduction(user_command)
                            change = round(payment - item['price'], 2)
                            print(f"Here is your {user_command}. Enjoy!")
                            if change > 0:
                                print(f"Here is ${change} in change.")
                        else:
                            print("Sorry, that's not enough money. Money refunded.")
        elif user_command == 'report':
            report_machine()
        elif user_command == 'off':
            print("Coffee Machine turned off.")
        else:
            print("Invalid command.")


command_coffee_machine()