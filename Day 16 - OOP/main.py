from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu= Menu()

is_on = True

while is_on:
    choice = input(f"What would you drink: {menu.get_items()}: ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        money_machine.report()
        coffee_maker.report()

    elif choice == "ingredients":
        choice = input(f"Which ingredients want to learn?: {menu.get_items()}: ")
        ingredients = menu.find_drink(choice)
        print(ingredients.ingredients)

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



