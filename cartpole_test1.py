from time import sleep
import os
import cv2
import gymnasium as gym
import gnwrapper
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
import matplotlib.pyplot as plt

env = gym.make("CartPole-v1", render_mode = "human")
episodes =50
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        
	#env.render()
        action = env.action_space.sample()
        n_state, reward, done,trucated, info = env.step(action)
        score += reward
    
    #sleep(0.03)
    env.render()
    #cv2.imshow("Window Title", env.render())
	    
    print('Episode:{} Score:{}'.format(episode, score))
    # Close the rendering window properly
    #cv2.destroyAllWindows()
    #cv2.waitKey(1)  # Ensure window processes events
	
env.close()

