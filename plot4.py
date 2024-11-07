import matplotlib.pyplot as plt

# Data
options = ['Op1', 'Op2', 'Op3', 'Op4', 'Op5', 'Op6', 'Op7', 'Op8', 'Op9']
delay_e_greedy = [65, 70, 75, 77, 78, 80, 82, 83, 85]
delay_boltzmann = [67, 70, 72, 74, 75, 76, 78, 79, 80]
delay_ucb = [75, 73, 71, 72, 70, 75, 74, 76, 75]

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(options, delay_e_greedy, marker='s', color='black', label='e-Greedy')
plt.plot(options, delay_boltzmann, marker='o', color='red', label='Boltzmann')
plt.plot(options, delay_ucb, marker='^', color='blue', label='UCB')

# Adding title and labels
plt.title('Delay vs the number of HWN')
plt.xlabel('Options')
plt.ylabel('Delay (ms)')
plt.legend()

# Show the plot
plt.show()