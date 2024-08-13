# gambler_simulation/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import os

class Visualization:
    @staticmethod
    def plot_stake_history(results):
        data = {strategy: [r['stake_history'] for r in res] for strategy, res in results.items()}
        plt.figure(figsize=(10, 6))
        for strategy, stakes in data.items():
            for stake in stakes:
                plt.plot(stake)
                plt.ylim(-50, 300)
            plt.title('Time Series of Stake by Trial')
            plt.xlabel('Trial')
            plt.ylabel('Stake')
            filename = os.path.join(os.getcwd(), f'time_series_{strategy}.png')
            plt.savefig(filename)
            plt.close()

    @staticmethod
    def plot_win_rates(results):
        win_rates = {strategy: sum(1 for r in res if r['won']) / len(res) * 100 for strategy, res in results.items()}
        strategies = list(win_rates.keys())
        rates = list(win_rates.values())

        plt.figure(figsize=(10, 6))
        sns.barplot(x=strategies, y=rates)
        plt.title('Win Rate by Strategy')
        plt.xlabel('Strategy')
        plt.ylabel('Win Rate (%)')
        filename = os.path.join(os.getcwd(), 'win_rate.png')
        plt.savefig(filename)
        plt.close()

    @staticmethod
    def plot_avg_spins(results):
        avg_spins = {strategy: sum(r['spins'] for r in res) / len(res) for strategy, res in results.items()}
        strategies = list(avg_spins.keys())
        spins = list(avg_spins.values())

        plt.figure(figsize=(10, 6))
        sns.barplot(x=strategies, y=spins)
        plt.title('Average Number of Spins by Strategy')
        plt.xlabel('Strategy')
        plt.ylabel('Average Spins')
        filename = os.path.join(os.getcwd(), 'avg_spins.png')
        plt.savefig(filename)
        plt.close()

    @staticmethod
    def plot_outcome_distribution(results):
        plt.figure(figsize=(10, 6))
        for strategy, res in results.items():
            sns.histplot([r['final_stake'] for r in res], kde=True, label=strategy, stat="density")
        plt.title('Final Stake Distribution by Strategy')
        plt.xlabel('Final Stake')
        plt.ylabel('Density')
        plt.legend()
        filename = os.path.join(os.getcwd(), 'outcome_distribution.png')
        plt.savefig(filename)
        plt.close()
