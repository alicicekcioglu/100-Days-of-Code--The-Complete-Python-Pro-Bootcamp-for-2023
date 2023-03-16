menu = {
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
    "water": 10000,
    "milk": 10000,
    "coffee": 10000,
    "money": 0
}

def coin(penny, dime, nickel, quarter):
    a = 0.01
    b = 0.10
    c = 0.5
    d = 0.25
    total = (penny * a) + (dime * b) + (nickel * c) + (quarter * d)
    return total

def report():
    print(
        f'\nWater: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}gr\nMoney: ${resources["money"]}\n')

off = True
def taking_order():
    order = input("What What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        return report()

    elif order == "latte" and resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
        print("Please insert coins.")
        penny = int(input("How many pennies?: "))
        dime = int(input("How many dimes?: "))
        nickel = int(input("How many nickels?: "))
        quarter = int(input("How many quarters?: "))
        a = coin(penny, dime, nickel, quarter)
        print(a)

        if a >= 2.5:
            resources["water"] -= 200
            resources["milk"] -= 150
            resources["coffee"] -= 24
            resources["money"] += 2.5
            print("Here is your latte. Enjoy!")
            if a > 2.5:
                print(f"Here your cashback: {a-2.5}")
        else:
            print("Not enough money! Money refunded")
    elif order == "espresso" and resources["water"] >= 50 and resources["coffee"] >= 18:
        print("Please insert coins.")
        penny = int(input("How many pennies?: "))
        dime = int(input("How many dimes?: "))
        nickel = int(input("How many nickels?: "))
        quarter = int(input("How many quarters?: "))
        a = coin(penny, dime, nickel, quarter)
        print(a)

        if a >= 2.5:
            resources["water"] -= 50
            resources["coffee"] -= 18
            resources["money"] += 1.5
            print("Here is your latte. Enjoy!")
            if a > 2.5:
                print(f"Here your cashback: {a - 1.5}")
        else:
            print("Not enough money! Money refunded")

    elif order == "cappuccino" and resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
        print("Please insert coins.")
        penny = int(input("How many pennies?: "))
        dime = int(input("How many dimes?: "))
        nickel = int(input("How many nickels?: "))
        quarter = int(input("How many quarters?: "))
        a = coin(penny, dime, nickel, quarter)
        print(a)

        if a >= 2.5:
            resources["water"] -= 250
            resources["milk"] -= 100
            resources["coffee"] -= 24
            resources["money"] += 3.00
            print("Here is your latte. Enjoy!")
            if a > 2.5:
                print(f"Here your cashback: {a - 3.00}")
        else:
            print("Not enough money! Money refunded")
    elif order == "off":
        global off
        off = False

while off:
    taking_order()