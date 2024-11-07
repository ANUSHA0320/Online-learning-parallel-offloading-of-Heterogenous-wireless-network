import matplotlib.pyplot as plt

# Sample data based on the provided graph
options = ['Opt1', 'Opt2', 'Opt3', 'Opt4', 'Opt5', 'Opt6', 'Opt7', 'Opt8', 'Opt9']
network_selection_5G = [20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2]
network_selection_4G = [20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1]
network_selection_WiFi6 = [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]
network_selection_WiFi5 = [19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9]
network_selection_WiFi4 = [19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(options, network_selection_5G, 's-', label='5G')
plt.plot(options, network_selection_4G, 'o-', label='4G')
plt.plot(options, network_selection_WiFi6, '^-', label='Wi-Fi6')
plt.plot(options, network_selection_WiFi5, 'v-', label='Wi-Fi5')
plt.plot(options, network_selection_WiFi4, 'd-', label='Wi-Fi4')

# Adding labels and title
plt.xlabel('UCB')
plt.ylabel('Network Selection(%)')
plt.title('The selection ratio of HWN under the UCB.')
plt.legend()

# Display the plot
plt.show()