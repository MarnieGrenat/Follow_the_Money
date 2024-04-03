class MoneyBag:
    def __init__(self):
        self.amount = 0
        self.money_list = []

    def collect(self, amount:str, verbose:bool=False) -> None:
        self.money_list.append(amount)
        self.amount += int(amount)
        print(f"[VERBOSE] Money value: {amount}") if verbose else None

    def remove(self, amount) -> None:
        '''Not used. Legacy code'''
        self.money_list.remove(amount)
        self.amount -= amount

    def get_amount(self) -> int:
        return self.amount

    def get_money_list(self) -> list:
        return self.money_list

