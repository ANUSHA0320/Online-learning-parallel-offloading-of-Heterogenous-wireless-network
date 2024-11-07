import numpy as np
import random

class EpsilonGreedyParallelOffloading:
    def __init__(self, num_arms, epsilon, num_slots):
        self.num_arms = num_arms
        self.epsilon = epsilon
        self.num_slots = num_slots
        self.rewards = np.zeros(num_arms)
        self.arm_counts = np.zeros(num_arms)

    def select_arm(self):
        if random.random() > self.epsilon:
            return np.argmin(self.rewards / (self.arm_counts + 1e-5))
        else:
            return np.random.randint(0, self.num_arms)

    def update(self, arm, reward):
        self.arm_counts[arm] += 1
        self.rewards[arm] = (self.rewards[arm] * (self.arm_counts[arm] - 1) + reward) / self.arm_counts[arm]

    def run(self, reward_function):
        for t in range(self.num_slots):
            arm = self.select_arm()
            reward = reward_function(arm)
            self.update(arm, reward)
        self.print_results()

    def print_results(self):
        print("Epsilon-Greedy Results")
        print("Final Rewards:", self.rewards)
        print("Arm Selection Counts:", self.arm_counts)

def reward_function(arm):
    return np.random.rand()

num_arms = 10
epsilon = 0.1
num_slots = 100

epsilon_greedy = EpsilonGreedyParallelOffloading(num_arms, epsilon, num_slots)
epsilon_greedy.run(reward_function)

class SoftmaxParallelOffloading:
    def __init__(self, num_arms, temperature, num_slots):
        self.num_arms = num_arms
        self.temperature = temperature
        self.num_slots = num_slots
        self.rewards = np.zeros(num_arms)
        self.arm_counts = np.zeros(num_arms)

    def select_arm(self):
        exp_values = np.exp(self.rewards / self.temperature)
        probabilities = exp_values / np.sum(exp_values)
        return np.random.choice(range(self.num_arms), p=probabilities)

    def update(self, arm, reward):
        self.arm_counts[arm] += 1
        self.rewards[arm] = (self.rewards[arm] * (self.arm_counts[arm] - 1) + reward) / self.arm_counts[arm]

    def run(self, reward_function):
        for t in range(self.num_slots):
            arm = self.select_arm()
            reward = reward_function(arm)
            self.update(arm, reward)
        self.print_results()

    def print_results(self):
        print("Softmax Results")
        print("Final Rewards:", self.rewards)
        print("Arm Selection Counts:", self.arm_counts)

num_arms = 10
temperature = 0.1
num_slots = 100

softmax = SoftmaxParallelOffloading(num_arms, temperature, num_slots)
softmax.run(reward_function)


class UCBParallelOffloading:
    def __init__(self, num_arms, num_slots):
        self.num_arms = num_arms
        self.num_slots = num_slots
        self.rewards = np.zeros(num_arms)
        self.arm_counts = np.zeros(num_arms)
        self.total_counts = 0

    def select_arm(self):
        if self.total_counts < self.num_arms:
            return self.total_counts
        ucb_values = self.rewards + np.sqrt(2 * np.log(self.total_counts + 1) / (self.arm_counts + 1e-5))
        return np.argmin(ucb_values)

    def update(self, arm, reward):
        self.total_counts += 1
        self.arm_counts[arm] += 1
        self.rewards[arm] = (self.rewards[arm] * (self.arm_counts[arm] - 1) + reward) / self.arm_counts[arm]

    def run(self, reward_function):
        for t in range(self.num_slots):
            arm = self.select_arm()
            reward = reward_function(arm)
            self.update(arm, reward)
        self.print_results()

    def print_results(self):
        print("UCB Results")
        print("Final Rewards:", self.rewards)
        print("Arm Selection Counts:", self.arm_counts)

num_arms = 10
num_slots = 100

ucb = UCBParallelOffloading(num_arms, num_slots)
ucb.run(reward_function)

