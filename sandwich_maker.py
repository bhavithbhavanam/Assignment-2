class HamSandwichMaker:
    def _init_(self):
        # Initialize resources and recipes
        self.resources = {
            "bread": 12,  # slices
            "ham": 18,    # slices
            "cheese": 24  # ounces
        }
        self.recipes = {
            "small": {
                "ingredients": {"bread": 2, "ham": 4, "cheese": 4},
                "cost": 1.75,
            },
            "medium": {
                "ingredients": {"bread": 4, "ham": 6, "cheese": 8},
                "cost": 3.25,
            },
            "large": {
                "ingredients": {"bread": 6, "ham": 8, "cheese": 12},
                "cost": 5.5,
            }
        }
        self.machine_on = True

    def check_resources(self, sandwich_size):
        """Checks if there are enough resources for the requested sandwich."""
        ingredients = self.recipes[sandwich_size]["ingredients"]
        for item, amount in ingredients.items():
            if self.resources[item] < amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Prompts user for coins and calculates the total."""
        print("Please insert coins.")
        large_dollars = int(input("How many large dollars? "))
        half_dollars = int(input("How many half dollars? "))
        quarters = int(input("How many quarters? "))
        nickels = int(input("How many nickels? "))
        total = (large_dollars * 1) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, payment, cost):
        """Validates the payment and calculates change if necessary."""
        if payment < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif payment > cost:
            change = round(payment - cost, 2)
            print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size):
        """Deducts resources and prepares the sandwich."""
        ingredients = self.recipes[sandwich_size]["ingredients"]
        for item, amount in ingredients.items():
            self.resources[item] -= amount
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

    def show_report(self):
        """Displays the remaining resources."""
        print("\nResources Report:")
        for item, amount in self.resources.items():
            unit = "slice(s)" if item != "cheese" else "ounce(s)"
            print(f"{item.capitalize()}: {amount} {unit}")
        print()

    def run(self):
        """Main loop to handle user inputs."""
        while self.machine_on:
            choice = input("What would you like? (small/medium/large/off/report): ").lower()
            if choice == "off":
                self.machine_on = False
                print("Turning off the machine. Goodbye!")
            elif choice == "report":
                self.show_report()
            elif choice in self.recipes:
                if self.check_resources(choice):
                    payment = self.process_coins()
                    if self.transaction_result(payment, self.recipes[choice]["cost"]):
                        self.make_sandwich(choice)
            else:
                print("Invalid choice. Please select a valid option.")

# Start the program
