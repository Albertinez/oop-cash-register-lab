class CashRegister:
    def __init__(self, discount=0):
        # Initialize discount using property setter
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    # ----------------------------
    # Discount Property
    # ----------------------------
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    # ----------------------------
    # Add Item
    # ----------------------------
    def add_item(self, item, price, quantity=1):
        # Increase total
        self.total += price * quantity

        # Add item(s) to items list (including multiples)
        for _ in range(quantity):
            self.items.append(item)

        # Store transaction amount
        self.previous_transactions.append(price * quantity)

    # ----------------------------
    # Apply Discount
    # ----------------------------
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # Format total to remove .0 if whole number
        if self.total.is_integer():
            formatted_total = int(self.total)
        else:
            formatted_total = self.total

        print(f"After the discount, the total comes to ${formatted_total}.")

    # ----------------------------
    # Void Last Transaction
    # ----------------------------
    def void_last_transaction(self):
      if self.previous_transactions:
        last_transaction_amount = self.previous_transactions.pop()
        self.total -= last_transaction_amount
