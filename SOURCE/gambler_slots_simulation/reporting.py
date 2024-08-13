# gambler_simulation/reporting.py

from unittest import result
from fpdf import FPDF
import statistics
from datetime import datetime

from gambler_slots_simulation.visualization import Visualization
import os
import os

class PDFReport:
    """
    A class for generating PDF reports.
    Args:
        title (str): The title of the report.
        results (dict): A dictionary containing the simulation results.
    Attributes:
        title (str): The title of the report.
        results (dict): A dictionary containing the simulation results.
        pdf (FPDF): The FPDF object used for generating the PDF.
    Methods:
        add_title(): Adds the title of the report to the PDF.
        add_section_title(title: str): Adds a section title to the PDF.
        add_paragraph(text: str): Adds a paragraph of text to the PDF.
        add_table(data: list, columns: list): Adds a table to the PDF.
        add_plot(image_path: str, description: str = ""): Adds a plot to the PDF.
        generate_statistics(): Generates statistics based on the simulation results.
        build_report(include_details: bool = False): Builds the report by adding sections, statistics, and plots to the PDF.
        save(filename: str): Saves the PDF report to a file.
    """
    def __init__(self, title, results, slot_machine):
        self.title = title
        self.results = results
        self.slot_machine = slot_machine
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        
    def add_title(self):
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(200, 10, txt=self.title, ln=True, align='C')
        self.pdf.ln(10)  # Line break

    def add_section_title(self, title):
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(200, 10, txt=title, ln=True, align='L')
        self.pdf.ln(5)

    def add_paragraph(self, text):
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, txt=text)
        self.pdf.ln()

    def add_table(self, data, columns):
        self.pdf.set_font("Arial", "B", 12)
        col_width = self.pdf.w / (len(columns) + 1)
        for column in columns:
            self.pdf.cell(col_width, 10, column, border=1)
        self.pdf.ln()

        self.pdf.set_font("Arial", size=12)
        for row in data:
            for item in row:
                self.pdf.cell(col_width, 10, str(item), border=1)
            self.pdf.ln()

    def add_plot(self, image_path, description=""):
        self.pdf.ln(5)
        self.pdf.image(image_path, w=170)
        if description:
            self.add_paragraph(description)

    def generate_statistics(self):
        stats = {}
        for strategy, data in self.results.items():
            win_rates = [r['won'] for r in data]
            spins = [r['spins'] for r in data]
            final_stakes = [r['final_stake'] for r in data]
            
            stats[strategy] = {
                'win_rate_mean': statistics.mean(win_rates) * 100,
                'spins_mean': statistics.mean(spins),
                'final_stake_mean': statistics.mean(final_stakes),
                'final_stake_median': statistics.median(final_stakes),
                'final_stake_stddev': statistics.stdev(final_stakes) if len(final_stakes) > 1 else 0,
            }
        return stats

    def build_report(self, include_details=False):
        self.add_title()
        self.add_section_title("Simulation Overview")
        self.add_paragraph(f"This report presents the results of the simulation titled '{self.title}', run on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
        self.add_paragraph(f"The simulation was conducted using the following slot machine configuration:")
        self.add_paragraph(f"Slot Machine Payout Probabilities:")
        for i, line in enumerate(self.slot_machine.payout_probs):
            self.add_paragraph(f"Line {i+1}: {line}")
        self.add_paragraph(f"Rewards: {self.slot_machine.rewards}")
        self.add_paragraph(f"Number of Trials: {len(self.results[list(self.results.keys())[0]])}")
        self.add_paragraph(f"Number of Strategies: {len(self.results)}")
        self.pdf.add_page()
        self.add_section_title("Summary Statistics")
        stats = self.generate_statistics()
        for strategy, stat_data in stats.items():
            self.add_section_title(f"Strategy: {strategy}")
            self.add_paragraph(f"Description: {self.results[strategy][0]['description']}")
            self.add_paragraph(f"Win Rate (Mean): {stat_data['win_rate_mean']:.2f}%")
            self.add_paragraph(f"Average Number of Spins: {stat_data['spins_mean']:.2f}")
            self.add_paragraph(f"Final Stake (Mean): {stat_data['final_stake_mean']:.2f}")
            self.add_paragraph(f"Final Stake (Median): {stat_data['final_stake_median']:.2f}")
            self.add_paragraph(f"Final Stake (Standard Deviation): {stat_data['final_stake_stddev']:.2f}")
        self.pdf.add_page()
        if include_details:
            self.add_section_title("Detailed Results")
            for strategy, data in self.results.items():
                self.add_section_title(f"Strategy: {strategy}")
                columns = ['Trial', 'Outcome', 'Spins', 'Won']
                table_data = [[i+1, r['final_stake'], r['spins'], r['won']] for i, r in enumerate(data)]
                self.add_table(table_data, columns)
            self.pdf.add_page()
        self.add_section_title("Visualizations")
        Visualization.plot_win_rates(self.results)
        Visualization.plot_avg_spins(self.results)
        Visualization.plot_outcome_distribution(self.results)
        Visualization.plot_stake_history(self.results)
        

        image_path = f"outcome_distribution.png"
        description = f"Distribution of final stakes for each trial - Strategy: {strategy}"
        self.add_plot(image_path, description)

        image_path = f"win_rate.png"
        description = f"Win rate for each trial - Strategy: {strategy}"
        self.add_plot(image_path, description)

        image_path = f"avg_spins.png"
        description = f"Average number of spins for each trial - Strategy: {strategy}"
        self.add_plot(image_path, description)

        image_path = f"time_series_FixedBetStrategy.png"
        description = f"Time series of gain for Fixed Bet Strategy - Strategy: {strategy}"
        self.add_plot(image_path, description)

        image_path = f"time_series_KellyCriterionStrategy.png"
        description = f"Time series of gain for Kelly Criterion Strategy - Strategy: {strategy}"
        self.add_plot(image_path, description)

        image_path = f"time_series_MartingaleStrategy.png"
        description = f"Time series of gain for Martingale Strategy - Strategy: {strategy}"
        self.add_plot(image_path, description)

        image_path = f"time_series_ReverseMartingaleStrategy.png"
        description = f"Time series of gain for Reverse Martingale Strategy - Strategy: {strategy}"
        self.add_plot(image_path, description)

        image_path = f"time_series_FibonacciStrategy.png"
        description = f"Time series of gain for Fibonacci Strategy - Strategy: {strategy}"
        self.add_plot(image_path, description)
            

           

    def save(self, filename):
        self.pdf.output(filename)
