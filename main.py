
from data import MENU
from data import resources
from data import money


def check_coffe(user_input):
    if resources["water"] > MENU[user_input]["ingredients"]["water"]:
        if resources["milk"] > MENU[user_input]["ingredients"]["milk"]:
            if resources["coffee"] > MENU[user_input]["ingredients"]["coffee"]:
                return True
def create_coffe(user_input):
    print()



def report():
    print(f'water = {resources["water"]}ml\nmilk = {resources["milk"]}ml\ncoffee = {resources["coffee"]}g')

#user_input = input("What would you like? (espresso/latte/cappuccino):")


report()
