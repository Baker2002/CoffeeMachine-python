from data import MENU
from data import resources


def total_money():
    penny_input = int(input("How many pennies"))
    nickle_input = int(input("How many nickles"))
    dime_input = int(input("How many dimes"))
    quarter_input = int(input("How many quarters"))
    total = (penny_input * 0.01) + (nickle_input * 0.05) + (dime_input * 0.1) + (quarter_input * 0.25)
    return total


def coffee_cost_check(user_input, total):
    if total >= MENU[user_input]["cost"]:
        return True
    else:
        return False


def check_coffe_resources(user_input):
    if resources["water"] > MENU[user_input]["ingredients"]["water"]:
        if resources["milk"] > MENU[user_input]["ingredients"]["milk"]:
            if resources["coffee"] > MENU[user_input]["ingredients"]["coffee"]:
                return True


def create_coffe(user_input, total):
    if check_coffe_resources(user_input):
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
        total -= MENU[user_input]["cost"]
        print(f"Your {user_input} is done\nChange is {round(total, 2)}")
    else:
        print("Not enough resources")


def report():
    print(f'water = {resources["water"]}ml\nmilk = {resources["milk"]}ml\ncoffee = {resources["coffee"]}g')


user_input = ""


while user_input != "off":
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "report":
        report()
    elif user_input == "off":
        break
    else:
        total = total_money()
        if coffee_cost_check(user_input, total):
            create_coffe(user_input, total)
        else:
            print("Not enough money")
