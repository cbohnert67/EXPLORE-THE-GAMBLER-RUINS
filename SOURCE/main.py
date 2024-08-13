from gambler_slots_simulation.strategies import FibonacciStrategy, ReverseMartingaleStrategy
from gambler_slots_simulation import FixedBetStrategy, KellyCriterionStrategy, MartingaleStrategy, SlotMachine, Gambler, Simulation, Visualization
from gambler_slots_simulation.reporting import PDFReport
import random
import os
from tqdm import tqdm  # Import tqdm for the progress bar

# Define slot machine with varying odds
payout_probs = [
    [0.5, 0.3, 0.15, 0.05],  # Line 1
    [0.6, 0.25, 0.1, 0.05],  # Line 2
    [0.4, 0.35, 0.2, 0.05]   # Line 3
]
rewards = [0, 2, 5, 10]

slot_machine = SlotMachine(payout_probs=payout_probs, rewards=rewards)

# Create 5 multiline real with varying odds slots machines for comparison
real_world_payout_probs = []
real_world_rewards = [0, 2, 5, 10]

for _ in range(5):
    payout_probs = [[random.uniform(0, 1) for _ in range(4)] for _ in range(3)]
    total_probs = [sum(line) for line in payout_probs]
    payout_probs = [[prob / total_probs[i] for prob in line] for i, line in enumerate(payout_probs)]
    real_world_payout_probs.append(payout_probs)

real_world_slot_machines = []
for payout_probs in real_world_payout_probs:
    real_world_slot_machines.append(SlotMachine(payout_probs=payout_probs, rewards=real_world_rewards))

TRIALS_NUMBER = 100  # Define the number of trials
stake = 100
goal = 500

# Iterate over slot machines with a progress bar
for i, slot_machine in enumerate(tqdm(real_world_slot_machines, desc="Slot Machines")):
    gamblers = []
    gamblers.append(Gambler(stake=stake, goal=goal, strategy=FixedBetStrategy(bet_amount=10), slot_machine=slot_machine))
    gamblers.append(Gambler(stake=stake, goal=goal, strategy=KellyCriterionStrategy(probability_of_winning=0.6, payout_ratio=2), slot_machine=slot_machine))
    gamblers.append(Gambler(stake=stake, goal=goal, strategy=MartingaleStrategy(initial_bet=10), slot_machine=slot_machine))
    gamblers.append(Gambler(stake=stake, goal=goal, strategy=ReverseMartingaleStrategy(initial_bet=10), slot_machine=slot_machine))
    gamblers.append(Gambler(stake=stake, goal=goal, strategy=FibonacciStrategy(initial_bet=10), slot_machine=slot_machine))
    
    # Run the simulation
    simulation = Simulation(gamblers=gamblers, trials=TRIALS_NUMBER)
    simulation.run()

    # Visualize results
    results = simulation.get_results()

    directory = f"./results/slot_machine_{i+1}"
    os.makedirs(directory, exist_ok=True)
    os.chdir(directory)

    # Generate PDF report
    title = f"Slot Machine {i+1} - Simulation Analysis"
    report = PDFReport(title=title, results=results, slot_machine=slot_machine)
    report.build_report()
    filename = f"slot_machine{i+1}_simulation_report.pdf"
    report.save(filename)
    os.chdir("../..")