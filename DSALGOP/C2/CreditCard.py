class CreditCard:
    """A consumer credit card"""


def __init__(self, customer, bank, acnt, limit):
    """Create a new credit card instance.
    The initial balance is zero.

    customer the name of the customer
    bank     the name of the bank
    acnt     the account identifier
    limit    credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._acnt = acnt
    self._limit = limit
    self._balance = 0


def get_customer(self):
    return self._customer


def get_bank(self):
    return self._bank


def get_account(self):
    return self._acnt


def get_limit(self):
    return self._limit


def get_balance(self):
    return self._balance


def get_charge(self, price):
    if price + self._balance > self._limit:
        return False
    else:
        self._balance += price
        return True


def make_payment(self, amount):
    self._balance -= amount

