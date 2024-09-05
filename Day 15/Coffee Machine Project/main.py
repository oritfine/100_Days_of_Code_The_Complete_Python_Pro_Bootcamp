MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_drink(drink):
    ingredients = MENU[drink]['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink}. Enjoy!")


def charge(drink, dollars):
    cost = MENU[drink]['cost']
    dollars -= cost
    if dollars > 0:
        print(f"Here is ${round(dollars, 2)} dollars in change.")
    return cost


def transaction_successful(dollars):
    if dollars >= MENU[drink]['cost']:
        return True
    if dollars != -1:  # -1 represents invalid input of coins
        print("Sorry that's not enough money. Money refunded.")
    return False


def process_coins(drink):
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    except ValueError:
        print("Invalid input.")
        return -1


def resources_sufficient(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def print_report(money):
    print(f"Water: {resources['water']}\n"
          f"Milk: {resources['milk']}\n"
          f"Coffee: {resources['coffee']}\n"
          f"Money: {money}")


if __name__ == '__main__':
    money = 0
    machine_on = True
    while machine_on:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink == "off":
            machine_on = False
        elif drink == "report":
            print_report(money)
        elif drink not in ['espresso', 'latte', 'cappuccino']:
            print("Invalid input.")
        elif resources_sufficient(drink):
            dollars = process_coins(drink)
            if transaction_successful(dollars):
                money += charge(drink, dollars)
                make_drink(drink)
