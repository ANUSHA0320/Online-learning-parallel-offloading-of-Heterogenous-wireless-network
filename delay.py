import numpy as np
import matplotlib.pyplot as plt

# Define the number of actions, rounds, and parameters
num_actions = 10
num_rounds = 1000
epsilon = 0.1
tau = 1.0
confidence_bound = 2

# True values of the actions
true_values = np.random.rand(num_actions)

# Initialize estimated values
estimates = np.zeros(num_actions)
action_counts = np.zeros(num_actions)

# Initialize cumulative regrets
cumulative_regrets = {
    'epsilon-greedy': np.zeros(num_rounds), 
    'softmax': np.zeros(num_rounds), 
    'UCB': np.zeros(num_rounds),
    'default': np.zeros(num_rounds)
}

# Function to run a single algorithm and return average delay
def run_algorithm(algorithm):
    global estimates, action_counts
    regrets = np.zeros(num_rounds)
    if algorithm == 'epsilon-greedy':
        for t in range(num_rounds):
            if np.random.rand() < epsilon:
                action = np.random.choice(num_actions)
            else:
                action = np.argmax(estimates)
            
            reward = np.random.normal(true_values[action])
            action_counts[action] += 1
            estimates[action] += (reward - estimates[action]) / action_counts[action]
            
            # Compute regret
            best_action = np.argmax(true_values)
            regrets[t] = true_values[best_action] - true_values[action]
        
    elif algorithm == 'softmax':
        for t in range(num_rounds):
            probabilities = np.exp(estimates / tau) / np.sum(np.exp(estimates / tau))
            action = np.random.choice(num_actions, p=probabilities)
            
            reward = np.random.normal(true_values[action])
            action_counts[action] += 1
            estimates[action] += (reward - estimates[action]) / action_counts[action]
            
            # Compute regret
            best_action = np.argmax(true_values)
            regrets[t] = true_values[best_action] - true_values[action]
    
    elif algorithm == 'UCB':
        ucb_values = np.zeros(num_actions)
        for t in range(num_rounds):
            if np.min(action_counts) == 0:
                action = np.argmin(action_counts)
            else:
                ucb_values = estimates + confidence_bound * np.sqrt(np.log(t + 1) / action_counts)
                action = np.argmax(ucb_values)
            
            reward = np.random.normal(true_values[action])
            action_counts[action] += 1
            estimates[action] += (reward - estimates[action]) / action_counts[action]
            
            # Compute regret
            best_action = np.argmax(true_values)
            regrets[t] = true_values[best_action] - true_values[action]
    
    elif algorithm == 'default':
        for t in range(num_rounds):
            action = np.random.choice(num_actions)
            reward = np.random.normal(true_values[action])
            
            # Compute regret
            best_action = np.argmax(true_values)
            regrets[t] = true_values[best_action] - true_values[action]
    
    # Compute cumulative regret
    cumulative_regret = np.cumsum(regrets)
    
    return cumulative_regret[-1] / num_rounds  # Average delay (cumulative regret per round)

# Run simulations and collect average delays
algorithms = ['default', 'epsilon-greedy', 'softmax', 'UCB']
average_delays = []

for algo in algorithms:
    estimates[:] = 0
    action_counts[:] = 0
    avg_delay = run_algorithm(algo)
    average_delays.append(avg_delay)

# Plot the average delays
plt.figure(figsize=(10, 6))
plt.bar(algorithms, average_delays, color=['gray', 'blue', 'green', 'red'])
plt.xlabel('Algorithm')
plt.ylabel('Delay')
plt.title('Average Delay Comparison of Default, ε-Greedy, Softmax, and UCB Algorithms')
plt.grid(axis='y')
plt.show()
