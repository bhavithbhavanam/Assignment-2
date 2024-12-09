import data
from sandwich_maker import HamSandwichMaker
from cashier import Cashier

def main():
    resources = data.resources
    recipes = data.recipes
    sandwich_maker = HamSandwichMaker(resources)
    cashier = Cashier()
    machine_on = True

    while machine_on:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()
        if choice == "off":
            machine_on = False
            print("Turning off the machine. Goodbye!")
        elif choice == "report":
            print("\nResources Report:")
            for item, amount in resources.items():
                unit = "slice(s)" if item != "cheese" else "ounce(s)"
                print(f"{item.capitalize()}: {amount} {unit}")
            print()
        elif choice in recipes:
            if sandwich_maker.check_resources(choice, recipes):
                payment = cashier.process_coins()
                if cashier.transaction_result(payment, recipes[choice]["cost"]):
                    sandwich_maker.make_sandwich(choice, recipes)
        else:
            print("Invalid choice. Please select a valid option.")

