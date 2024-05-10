# OpenAI-Gym
OpenAI Gym is a toolkit for developing and comparing reinforcement learning algorithms.

This code creates a custom Gym environment for drone navigation with configurable parameters such as the size of the area, starting position of the drone, and number of steps. It defines the action space for the drone to move in four directions (up, down, left, right) and the observation space providing information about the drone's current position. The reward function rewards the drone for reaching the target destination and penalizes it for each step taken and for moving outside boundaries. The step function takes an action as input and returns the new state, reward, and whether the episode is done. The environment resets after each episode, placing the drone in a random starting position within the defined area. Finally, rendering functionality is left unimplemented, as it is optional for visualization.

Python Environment Setup:

import gym
from gym import spaces
import numpy as np

We import the necessary libraries:
gym: The OpenAI Gym library.
spaces: Module containing the spaces classes defining action and observation spaces.
numpy: Library for numerical computing in Python.

Custom Gym Environment Class:
class DroneNavigation(gym.Env):
This defines a custom Gym environment named "DroneNavigation" that adheres to the Gym interface.

Constructor (__init__ method):
    def __init__(self, area_size=(10, 10), start_position=None, num_steps=100):
        super(DroneNavigation, self).__init__()
        
Initializes the environment with parameters:

area_size: Size of the area where the drone can move (default is a 10x10 grid).
start_position: Starting position of the drone (default is None, which results in a random position).
num_steps: Number of steps the drone can take in an episode (default is 100).

Action and Observation Spaces:
        # Define action and observation spaces
        self.action_space = spaces.Discrete(4)  # Up, Down, Left, Right
        self.observation_space = spaces.Box(low=np.array([0, 0]), high=np.array(area_size), dtype=np.float32)
Defines the action space for the drone with four discrete actions (up, down, left, right).
Defines the observation space providing information about the drone's current position within the area.

Reset Method:
    def reset(self):
        self.current_step = 0
        self.drone_position = np.array(self.start_position)
        return self.drone_position
        
Resets the environment:
Sets the current step count to 0.
Sets the drone's position to the starting position.
Returns the initial observation (drone's position).

Step Method:
    def step(self, action):
    
Implements the step function:
Takes an action as input.
Moves the drone based on the action taken.
Calculates the reward based on the new state.
Checks if the episode is done.
Returns the new observation, reward, done flag, and additional info.

Reward Calculation Method:
    def _calculate_reward(self):
    
Helper method to calculate the reward:
Rewards the drone positively when it reaches the target destination.
Penalizes the drone negatively for each step taken and for moving outside boundaries.

Rendering Method:
    def render(self, mode='human'):
        # Visualize the environment (optional)
        pass
Optional method for visualizing the environment.
Currently left unimplemented.

Testing the Environment:
# Testing the environment
if __name__ == "__main__":
    env = DroneNavigation(area_size=(5, 5), start_position=(0, 0), num_steps=10)
    obs = env.reset()
    done = False
    
    while not done:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        print(f"Action: {action}, Drone Position: {obs}, Reward: {reward}")
        
Tests the environment by creating an instance of the DroneNavigation environment with specified parameters.
Resets the environment and runs a loop of steps until the episode is done, printing out the action taken, drone's position, and reward received at each step.
This code sets up a custom Gym environment for drone navigation, providing the necessary methods to interact with the environment, including resetting, stepping through actions, and calculating rewards.



