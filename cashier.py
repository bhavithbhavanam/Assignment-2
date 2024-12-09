class Cashier:
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