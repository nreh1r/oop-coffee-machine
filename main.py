from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
drinkoptions = menu.get_items()
running = True

while running:
    choice = input(f"What would you like? {drinkoptions}: ").lower()
    if choice == "off":
        running = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in drinkoptions:
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)) and money_machine.make_payment(menu.find_drink(choice).cost):
            coffee_maker.make_coffee(menu.find_drink(choice))
