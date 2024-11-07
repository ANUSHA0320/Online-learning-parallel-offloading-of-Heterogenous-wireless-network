import numpy as np
import matplotlib.pyplot as plt

# Synthetic data for the example
algorithms = ['ε-Greedy', 'Boltzmann', 'UCB']
delay_performance = [55, 45, 10]
delay_jitter_performance = [70, 60, 20]
packet_loss_performance = [65, 55, 15]
data_rate_performance = [65, 45, 35]

# Function to create bar plots
def create_bar_plot(ax, data, title, ylabel, color):
    ax.bar(algorithms, data, color=color)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_ylim([0, 80])

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plot Delay Performance
create_bar_plot(axs[0, 0], delay_performance, 'Delay Performance', 'Low Delay Ratio (%)', 'blue')

# Plot Delay Jitter Performance
create_bar_plot(axs[0, 1], delay_jitter_performance, 'Delay Jitter Performance', 'Low Jitter Ratio (%)', 'orange')

# Plot Packet Loss Performance
create_bar_plot(axs[1, 0], packet_loss_performance, 'Packet Loss Performance', 'Low Packet Loss Ratio (%)', 'pink')

# Plot Data Rate Performance
create_bar_plot(axs[1, 1], data_rate_performance, 'Data Rate Performance', 'Low Data Rate Ratio (%)', 'teal')

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()