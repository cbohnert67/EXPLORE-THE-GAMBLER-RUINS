# gambler_simulation/slot_machine.py

import random

class SlotMachine:
    """
    A class representing a slot machine.
    Attributes:
    - payout_probs (list): A list of lists representing the probabilities of each reward for each line.
    - rewards (list): A list of rewards corresponding to each payout probability.
    - lines (int): The number of lines in the slot machine.
    - bonus_trigger (float): The probability of triggering a bonus round.
    - jackpot_win_rate (float): The probability of winning the jackpot.
    - jackpot (int): The current value of the jackpot.
    Methods:
    - spin(): Spins the slot machine and returns the total reward.
    - trigger_bonus_round(): Triggers a bonus round and returns the reward.
    - update_jackpot(contribution): Updates the jackpot value by adding the contribution.
    """
    def __init__(self, payout_probs, rewards, lines=3, bonus_trigger=0.1, jackpot_win_rate=0.0001, jackpot_initial=5000):
        self.payout_probs = payout_probs
        self.rewards = rewards
        self.lines = lines
        self.bonus_trigger = bonus_trigger
        self.jackpot_win_rate = jackpot_win_rate
        self.jackpot_initial = jackpot_initial

    def spin(self):
        total_reward = 0
        for line in range(self.lines):
            outcome = random.choices(self.rewards, self.payout_probs[line])[0]
            total_reward += outcome
        if random.random() < self.bonus_trigger:
            total_reward += self.trigger_bonus_round()
        if random.random() < self.jackpot_win_rate:
            total_reward += self.jackpot_initial
        return total_reward
        

    def trigger_bonus_round(self):
        # Implement a simple bonus round logic
        return random.randint(10, 100)

    def update_jackpot(self, contribution):
        self.jackpot += contribution
