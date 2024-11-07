import matplotlib.pyplot as plt

# Sample data based on the provided graph
options = ['Opt1', 'Opt2', 'Opt3', 'Opt4', 'Opt5', 'Opt6', 'Opt7', 'Opt8', 'Opt9']
network_selection_5G = [0.2, 0.2, 0.3, 0.5, 0.3, 0.2, 0.2, 0.2, 0.2]
network_selection_4G = [0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2]
network_selection_WiFi6 = [0.2, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2]
network_selection_WiFi5 = [0.2, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2]
network_selection_WiFi4 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(options, network_selection_5G, 's-', label='5G')
plt.plot(options, network_selection_4G, 'o-', label='4G')
plt.plot(options, network_selection_WiFi6, '^-', label='Wi-Fi6')
plt.plot(options, network_selection_WiFi5, 'v-', label='Wi-Fi5')
plt.plot(options, network_selection_WiFi4, 'd-', label='Wi-Fi4')

# Adding labels and title
plt.xlabel('e-Greedy')
plt.ylabel('Network Selection(%)')
plt.title('The selection ratio of HWN under e-Greedy.')
plt.legend()

# Display the plot
plt.show()