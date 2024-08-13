# gambler_simulation/strategies.py

from abc import ABC, abstractmethod

class BettingStrategy(ABC):
    @abstractmethod
    def bet(self, current_stake):
        pass

class FixedBetStrategy(BettingStrategy):
    """
    Fixed bet strategy: always bet the same amount.
    Attributes:
        bet_amount (float): The amount to bet on each round.
    Methods:
        bet(current_stake):
            Determines the amount to bet based on the current stake.
    """
    def __init__(self, bet_amount):
        self.description = """Fixed bet strategy: always bet the same amount."""
        self.bet_amount = bet_amount

    def bet(self, current_stake):
        return min(self.bet_amount, current_stake)

class KellyCriterionStrategy(BettingStrategy):
    """
    Kelly criterion strategy: calculates the optimal bet size based on the probability of winning and the payout ratio.
    Attributes:
        probability_of_winning (float): The probability of winning the bet.
        payout_ratio (float): The ratio of the payout for a winning bet.
    """
    def __init__(self, probability_of_winning, payout_ratio):
        self.description = """Kelly criterion strategy: calculates the optimal bet size based on the probability of winning and the payout ratio."""
        self.probability_of_winning = probability_of_winning
        self.payout_ratio = payout_ratio

    def bet(self, current_stake):
        bet_fraction = (self.probability_of_winning * (self.payout_ratio + 1) - 1) / self.payout_ratio
        return max(1, min(int(current_stake * bet_fraction), current_stake))

class MartingaleStrategy(BettingStrategy):
    """
    Martingale strategy: double the bet after each loss, reset to initial bet after each win.
    Attributes:
    - initial_bet: The initial bet amount.
    - current_bet: The current bet amount.
    Methods:
    - bet(current_stake): Determines the bet amount based on the current stake.
    """
    def __init__(self, initial_bet):
        self.description = """Martingale strategy: double the bet after each loss, reset to initial bet after each win."""
        self.initial_bet = initial_bet
        self.current_bet = initial_bet

    def bet(self, current_stake):
        bet = min(self.current_bet, current_stake)
        self.current_bet *= 2 if current_stake < self.current_bet else self.initial_bet
        return bet

class ReverseMartingaleStrategy(BettingStrategy):
    """
    Reverse Martingale strategy: double the bet after each win, reset to initial bet after each loss.
    Attributes:
        initial_bet (float): The initial bet amount.
        current_bet (float): The current bet amount.
    Methods:
        bet(current_stake): Determines the bet amount based on the current stake.
    """
    def __init__(self, initial_bet):
        self.description = """Reverse Martingale strategy: double the bet after each win, reset to initial bet after each loss."""
        self.initial_bet = initial_bet
        self.current_bet = initial_bet

    def bet(self, current_stake):
        bet = min(self.current_bet, current_stake)
        self.current_bet *= 2 if current_stake >= self.current_bet else self.initial_bet
        return bet

class FibonacciStrategy(BettingStrategy):
    """
    Fibonacci strategy: bet according to the Fibonacci sequence.
    This strategy is implemented as a class called FibonacciStrategy, which is a subclass of BettingStrategy. It is used to determine the betting amount based on the Fibonacci sequence.
    Attributes:
        description (str): A description of the strategy.
        initial_bet (int): The initial betting amount.
        fibonacci_sequence (list): The Fibonacci sequence.
        current_index (int): The current index in the Fibonacci sequence.
    Methods:
        bet(current_stake): Determines the betting amount based on the current stake.
    Example usage:
        strategy = FibonacciStrategy(initial_bet=10)
        bet_amount = strategy.bet(current_stake=100)
    """  
    def __init__(self, initial_bet):
        self.description = """Fibonacci strategy: bet according to the Fibonacci sequence."""
        self.initial_bet = initial_bet
        self.fibonacci_sequence = [1, 1]
        self.current_index = 1

    def bet(self, current_stake):
        bet = min(self.fibonacci_sequence[self.current_index], current_stake)
        self.current_index += 1
        if self.current_index >= len(self.fibonacci_sequence):
            self.fibonacci_sequence.append(self.fibonacci_sequence[-1] + self.fibonacci_sequence[-2])
        return bet

class DAlembertStrategy(BettingStrategy):
    """
    D'Alembert strategy: increase the bet by one unit after each loss, decrease by one unit after each win.
    Attributes:
        Determines the bet amount based on the current stake.
        Parameters:
            current_stake (int): The current stake of the player.
        Returns:
            int: The bet amount to be placed.
    """

    def __init__(self, initial_bet):
        self.description = """D'Alembert strategy: increase the bet by one unit after each loss, decrease by one unit after each win."""
        self.initial_bet = initial_bet
        self.current_bet = initial_bet

    def bet(self, current_stake):
        bet = min(self.current_bet, current_stake)
        self.current_bet += 1 if current_stake < self.current_bet else -1
        return bet


    