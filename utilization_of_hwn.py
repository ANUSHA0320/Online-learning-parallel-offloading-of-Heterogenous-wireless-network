import numpy as np
import matplotlib.pyplot as plt

# Define the weight vectors for each method
weights = {
    '4G': [0.45773088, 0.11960993, 0.11960993, 0.06779268, 0.23525658],
    '5G': [0.05621057, 0.22433497, 0.22433497, 0.37660383, 0.11851566],
    'WiFi4': [0.4890154, 0.11119827, 0.11119827, 0.06565655, 0.2229315],
    'WiFi5': [0.45773088, 0.11960993, 0.11960993, 0.06779268, 0.23525658],
    'WiFi6': [0.05621057, 0.22433497, 0.22433497, 0.37660383, 0.11851566]
}

network_types = list(weights.keys())
num_networks = len(network_types)
num_criteria = len(weights['4G'])

# Convert weights dictionary to list
weights_list = list(weights.values())

# Parameters for MAB algorithms
epsilon = 0.1  # For ε-greedy
temperature = 1.0  # For Softmax
num_episodes = 1000  # Number of trials

def epsilon_greedy(epsilon, weights):
    num_networks = len(weights)
    total_rewards = np.zeros(num_networks)
    selection_counts = np.zeros(num_networks)
    
    for _ in range(num_episodes):
        if np.random.rand() < epsilon:
            chosen_network = np.random.choice(num_networks)
        else:
            chosen_network = np.argmax(total_rewards / (selection_counts + 1e-5))
        
        reward = np.random.choice(weights[chosen_network])
        total_rewards[chosen_network] += reward
        selection_counts[chosen_network] += 1
    
    return selection_counts / num_episodes

def softmax(temperature, weights):
    num_networks = len(weights)
    total_rewards = np.zeros(num_networks)
    selection_counts = np.zeros(num_networks)
    
    for _ in range(num_episodes):
        probabilities = np.exp(total_rewards / (selection_counts + 1e-5) / temperature)
        probabilities /= np.sum(probabilities)
        chosen_network = np.random.choice(num_networks, p=probabilities)
        
        reward = np.random.choice(weights[chosen_network])
        total_rewards[chosen_network] += reward
        selection_counts[chosen_network] += 1
    
    return selection_counts / num_episodes

def ucb(weights):
    num_networks = len(weights)
    total_rewards = np.zeros(num_networks)
    selection_counts = np.zeros(num_networks)
    total_counts = 0
    
    for _ in range(num_episodes):
        if np.min(selection_counts) == 0:
            chosen_network = np.argmin(selection_counts)
        else:
            ucb_values = total_rewards / (selection_counts + 1e-5) + np.sqrt(2 * np.log(total_counts + 1) / (selection_counts + 1e-5))
            chosen_network = np.argmax(ucb_values)
        
        reward = np.random.choice(weights[chosen_network])
        total_rewards[chosen_network] += reward
        selection_counts[chosen_network] += 1
        total_counts += 1
    
    return selection_counts / num_episodes

# Run algorithms
epsilon_utilization = epsilon_greedy(epsilon, weights_list)
softmax_utilization = softmax(temperature, weights_list)
ucb_utilization = ucb(weights_list)

# Plot results
plt.figure(figsize=(12, 6))

x = np.arange(num_networks)
width = 0.25

plt.bar(x - width, epsilon_utilization, width, label='ε-Greedy')
plt.bar(x, softmax_utilization, width, label='Softmax')
plt.bar(x + width, ucb_utilization, width, label='UCB')

plt.xlabel('Network Types')
plt.ylabel('Utilization Rate')
plt.title('Comparison of MAB Algorithms')
plt.xticks(x, network_types)
plt.legend()

plt.tight_layout()
plt.show()

# Print utilization rates
print("Utilization Rates for ε-Greedy:")
for i, network in enumerate(network_types):
    print(f"{network}: {epsilon_utilization[i]:.4f}")

print("\nUtilization Rates for Softmax:")
for i, network in enumerate(network_types):
    print(f"{network}: {softmax_utilization[i]:.4f}")

print("\nUtilization Rates for UCB:")
for i, network in enumerate(network_types):
    print(f"{network}: {ucb_utilization[i]:.4f}")
