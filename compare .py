import matplotlib.pyplot as plt

# Given weights from the AHP analysis
criteria = ['Delay', 'Delay Jitter', 'Packet Loss', 'Task Complexity', 'Computing Performance']
weights = [0.472, 0.181, 0.095, 0.064, 0.188]

# Plotting the bar chart
plt.figure(figsize=(9, 6))
plt.bar(criteria, weights, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Criteria')
plt.ylabel('Weights')
plt.title('Weights of Criteria for OLPO Analysis')
plt.show()
