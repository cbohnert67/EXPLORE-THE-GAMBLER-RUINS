# gambler_simulation/simulation.py

class Simulation:
    """
    A class representing a simulation of gamblers playing a game.
    Attributes:
        gamblers (list): A list of Gambler objects representing the gamblers in the simulation.
        trials (int): The number of trials to run in the simulation.
        results (dict): A dictionary containing the results of the simulation for each gambler.
    Methods:
        run(): Runs the simulation for the specified number of trials.
        get_results(): Returns the results of the simulation.
    """
    def __init__(self, gamblers, trials=100):
        self.gamblers = gamblers
        self.trials = trials
        self.results = {gambler.strategy.__class__.__name__: [] for gambler in gamblers}

    def run(self):
        for _ in range(self.trials):
            for gambler in self.gamblers:
                gambler.play()
                self.results[gambler.strategy.__class__.__name__].append({
                    'strategy': gambler.strategy.__class__.__name__,
                    'description': gambler.strategy.description,
                    'won': gambler.won,
                    'spins': gambler.spins,
                    'final_stake': gambler.stake,
                    'stake_history': gambler.stake_history,
                })
                gambler.reset()
    def get_results(self):
        return self.results
