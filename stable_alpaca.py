import gym
from gym import spaces
import numpy as np
from trader import trader_agent

ta = trader_agent()

class paca_env(gym.Env):
    def __init__(self) -> None:
        super(paca_env, self).__init__
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8)

    def step(self, action):
        # observe current positions

        return observation, reward, done, info
    def reset(self):
        self.done = False
        self.positions
        return observation  # reward, done, info can't be included
    # def render(self, mode="human"):
    #     pass
    # def close (self):
    #     pass