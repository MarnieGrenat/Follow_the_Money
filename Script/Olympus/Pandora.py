class Pandora:
    """
    A class representing a bag.

    Attributes:
        amount (int): The total amount in the bag.
        money_list (list): A list of values in the bag.

    Methods:
        collect(amount: str, verbose: bool = False) -> None:
            Collects money and adds it to the bag.

        remove(amount) -> None:
            Not used. Legacy code.

        get_amount() -> int:
            Returns the total amount of money in the bag.

        get_money_list() -> list:
            Returns the list of money values in the bag.
    """

    def __init__(self):
        self.amount = 0
        self.money_list = []

    def collect(self, value: int, verbose: bool = False) -> None:
        """
        Collects money and adds it to the bag.

        Args:
            amount (str): The amount of money to collect.
            verbose (bool, optional): Whether to print verbose information. Defaults to False.
        """
        self.money_list.append(value)
        self.amount += value
        if verbose:
            print(f"[LOG] Money value: {value}")

    def remove(self, amount) -> None:
        """
        Not used. Legacy code.
        """
        self.money_list.remove(amount)
        self.amount -= amount

    def get_amount(self) -> int:
        """
        Returns the total amount of money in the bag.

        Returns:
            int: The total amount of money in the bag.
        """
        return self.amount

    def get_money_list(self) -> list:
        """
        Returns the list of money values in the bag.

        Returns:
            list: The list of money values in the bag.
        """
        return self.money_list
