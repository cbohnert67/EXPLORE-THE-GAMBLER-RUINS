# gambler_simulation/gambler.py

class Gambler:
    """
    A class representing a gambler.
    Attributes:
    - initial_stake (int): The initial amount of money the gambler has.
    - stake (int): The current amount of money the gambler has.
    - goal (int): The target amount of money the gambler wants to reach.
    - strategy (object): The strategy used by the gambler to place bets.
    - slot_machine (object): The slot machine used by the gambler to play.
    - stake_history (list): A list of the gambler's stake at each step of the game.
    - spins (int): The number of spins played by the gambler.
    - won (bool): A flag indicating whether the gambler has reached the goal.
    Methods:
    - play(): Plays the game until the gambler reaches the goal or runs out of money.
    - reset(): Resets the gambler's state to the initial values.
    """
    def __init__(self, stake, goal, strategy, slot_machine):
        self.initial_stake = stake
        self.stake = stake
        self.goal = goal
        self.strategy = strategy
        self.slot_machine = slot_machine
        self.stake_history = []
        self.spins = 0
        self.won = False

    def play(self):
        while self.stake > 0 and self.stake < self.goal:
            bet_amount = self.strategy.bet(self.stake)
            result = self.slot_machine.spin()
            self.stake += (result - bet_amount)
            self.stake_history.append(self.stake)
            self.spins += 1
            if self.stake >= self.goal:
                self.won = True

    def reset(self):
        self.stake = self.initial_stake
        self.stake_history = []
        self.spins = 0
        self.won = False
