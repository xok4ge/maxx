import gym
import pygame
from gym.utils.play import play

mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 1}
play(gym.make("ALE/AirRaid-v5", render_mode="rgb_array"), keys_to_action=mapping)

# play(gym.make("CartPole-v1", render_mode="rgb_array"), keys_to_action=mapping)