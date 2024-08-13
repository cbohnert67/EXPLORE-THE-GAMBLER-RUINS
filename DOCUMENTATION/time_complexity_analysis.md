To analyze the time complexity of the simulation in the `main.py` script, let's break down the different parts of the code and understand how they contribute to the overall time complexity. The main factors affecting the time complexity are:

1. **Number of Gamblers** (`G`):
   - The simulation runs experiments for each gambler.

2. **Number of Trials** (`T`):
   - Each gambler is simulated for a number of trials.

3. **Simulation Loop**:
   - For each trial, the simulation runs a loop to simulate bets and outcomes until the gambler either reaches the goal or runs out of money.

### Detailed Analysis

#### 1. **Initialization of Gamblers and Slot Machine**

- **Setup**: Initializing the `SlotMachine` and creating `Gambler` instances are constant-time operations.
- **Complexity**: `O(1)` for initialization.

#### 2. **Simulation Execution**

The most computationally expensive part of the script is the simulation of trials. Let's analyze the complexity in detail.

- **Outer Loop (Trials)**:
  ```python
  for _ in range(1000):  # This is T
      ...
  ```
  This loop runs `T` times, where `T` is the number of trials.

- **Inner Loop (Simulation of Each Trial)**:
  ```python
  while gambler.stake > 0 and gambler.stake < gambler.goal:
      bet = gambler.strategy.bet(gambler.stake)
      reward = slot_machine.spin()
      gambler.stake += reward - bet
      if slot_machine.trigger_bonus():
          gambler.stake += slot_machine.spin()
  ```
  This loop simulates each bet until the gambler either wins or loses all their money. Let's analyze the operations within this loop:
  
  - **Bet and Outcome**:
    - The `bet()` method of the strategy is typically `O(1)`.
    - The `spin()` and `trigger_bonus()` methods of the `SlotMachine` are also `O(1)`.

  The most complex part is the number of iterations of the `while` loop, which is variable and depends on the gambler's stake and goal. The number of iterations can be up to `O(N)`, where `N` is the number of bets it takes to either reach the goal or lose all the stake.

  For each trial:
  - **Complexity of Each Trial**: The number of iterations of the `while` loop can be at worst `O(N)`, where `N` depends on the initial stake and the goal. Thus, the worst-case complexity for a single trial is `O(N)`.

- **Overall Simulation Complexity**:
  - **Number of Trials (T)**: Each trial runs in `O(N)` time.
  - **Total Complexity**: Since there are `T` trials, the total complexity is `O(T * N)`.

#### 3. **Outcome Distribution Collection**

To gather outcome data:
```python
for _ in range(1000):  # Collect outcomes for a larger sample
    ...
```
- **Time Complexity**: Each iteration has the same complexity as a single trial, i.e., `O(N)`. Collecting outcomes over 1000 runs adds a factor of 1000, so this step is `O(1000 * N)`, which is `O(N)` with respect to the number of outcomes collected.

### Parameters Controlling Time Complexity

1. **Number of Trials (`T`)**:
   - Directly affects the total number of simulations. Higher `T` increases the total computation time linearly.

2. **Complexity of Each Trial (`N`)**:
   - Influenced by the gambler's initial stake and goal. The number of bets (`N`) per trial affects how many operations are performed within each trial loop. 

3. **Number of Gamblers (`G`)**:
   - Since each gambler is simulated independently, the total complexity scales linearly with the number of gamblers. This adds a factor of `G` to the overall complexity, making it `O(G * T * N)`.

### Summary

- **Time Complexity**: The overall time complexity of the simulation is `O(G * T * N)`, where:
  - `G` is the number of gamblers.
  - `T` is the number of trials.
  - `N` is the average number of iterations in the `while` loop for each trial.

Understanding these parameters helps in optimizing the simulation by either reducing the number of trials, adjusting the stakes and goals, or minimizing the number of gamblers, depending on the required balance between computational efficiency and simulation detail.