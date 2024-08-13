# Gambler Slot Machine Simulation

This project is a comprehensive tool for simulating and analyzing various gambling strategies on slot machines. It includes modules for defining slot machines, implementing betting strategies, running simulations, visualizing results, and generating detailed PDF reports.

## GitHub Copilot

This project was developed using GitHub Copilot, which assisted in writing and refining the code.

## Setup

### Create a Virtual Environment

To get started, create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install the Dependencies

Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run a simulation, use the main script of the project. For example:

```python
python main.py
```

The script runs the simulation for different betting strategies on slot machines with varying odds and saves the results as PDF files in the `results` directory.

## Betting Strategies

The project includes several betting strategies:

- **Fixed Bet Strategy**: Betting a fixed amount each round.
- **Kelly Criterion Strategy**: Using the Kelly criterion to determine the bet amount.
- **Martingale Strategy**: Doubling the bet after each loss.
- **Reverse Martingale Strategy**: Doubling the bet after each win.
- **Fibonacci Strategy**: Using the Fibonacci sequence to determine the bet amount.

Each strategy offers a different approach to managing bets, allowing for a comprehensive comparison of their effectiveness in different slot machine scenarios.

## Results

The results of the simulations are visualized and saved as PDF reports. Each report includes:

- Charts depicting win rates, average spins, outcome distributions, and stake histories.
- Statistical analysis of each strategy's performance.
- Detailed summaries of the simulation outcomes.

These reports provide valuable insights into how different betting strategies perform under various conditions.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a branch for your feature:

   ```bash
   git checkout -b feature/my-feature
   ```

3. Commit your changes:

   ```bash
   git commit -am 'Add my feature'
   ```

4. Push your branch:

   ```bash
   git push origin feature/my-feature
   ```

5. Create a Pull Request.

Your contributions help make this project better!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.