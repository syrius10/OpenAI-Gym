import gym
from gym import spaces
import numpy as np

class DroneNavigation(gym.Env):
    def __init__(self, area_size=(10, 10), start_position=None, num_steps=100):
        super(DroneNavigation, self).__init__()
        
        # Define area size
        self.area_size = area_size
        
        # Define number of steps
        self.num_steps = num_steps
        
        # Define action and observation spaces
        self.action_space = spaces.Discrete(4)  # Up, Down, Left, Right
        self.observation_space = spaces.Box(low=np.array([0, 0]), high=np.array(area_size), dtype=np.float32)
        
        # Initialize drone position
        if start_position is None:
            self.start_position = np.random.randint(0, area_size[0]), np.random.randint(0, area_size[1])
        else:
            self.start_position = start_position
        self.reset()

    def reset(self):
        self.current_step = 0
        self.drone_position = np.array(self.start_position)
        return self.drone_position
    
    def step(self, action):
        # Move drone based on action
        if action == 0:  # Up
            self.drone_position[1] += 1
        elif action == 1:  # Down
            self.drone_position[1] -= 1
        elif action == 2:  # Left
            self.drone_position[0] -= 1
        elif action == 3:  # Right
            self.drone_position[0] += 1
        
        # Clip drone position to stay within area bounds
        self.drone_position = np.clip(self.drone_position, 0, np.array(self.area_size) - 1)
        
        # Calculate reward
        reward = self._calculate_reward()
        
        # Check if episode is done
        done = self.current_step >= self.num_steps or np.all(self.drone_position == np.array(self.area_size) - 1)
        
        self.current_step += 1
        
        return self.drone_position, reward, done, {}

    def _calculate_reward(self):
        if np.all(self.drone_position == np.array(self.area_size) - 1):
            return 10  # Positive reward when reaching the target
        elif np.any(self.drone_position < 0) or np.any(self.drone_position >= self.area_size):
            return -1  # Negative reward for moving outside boundaries
        else:
            return -0.1  # Negative reward for each step
    
    def render(self, mode='human'):
        # Visualize the environment (optional)
        pass

# Testing the environment
if __name__ == "__main__":
    env = DroneNavigation(area_size=(5, 5), start_position=(0, 0), num_steps=10)
    obs = env.reset()
    done = False
    
    while not done:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        print(f"Action: {action}, Drone Position: {obs}, Reward: {reward}")

