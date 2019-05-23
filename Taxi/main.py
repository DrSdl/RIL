from agent import Agent
from monitor import interact
import gym
import numpy as np

env = gym.make('Taxi-v2')
agent = Agent()
avg_rewards, best_avg_reward = interact(env, agent)
#print("avg reward: ",avg_rewards)
#print("best avg reward: ", best_avg_reward)
