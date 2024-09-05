from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    machine_on = True
    while machine_on:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if choice == "off":
            machine_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice not in ['espresso', 'latte', 'cappuccino']:
            print("Invalid input.")
        else:
            drink_item = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink_item) and money_machine.make_payment(drink_item.cost):
                coffee_maker.make_coffee(drink_item)
