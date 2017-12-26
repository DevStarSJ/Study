import gym
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import  register
import random as pr


register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs= {'map_name': '4x4', 'is_slippery': True}
)

env = gym.make('FrozenLake-v3')

Q = np.zeros([env.observation_space.n, env.action_space.n])
num_episodes = 2000
dis = 0.99

rList = []

def rargmax(vector):
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return pr.choice(indices)

for i in range(num_episodes):
    state = env.reset()
    rAll = 0
    done = False

    e = 1. / ((i // 100)+1)
    while not done:
        # e-greedy
        action = np.argmax(Q[state,:]) \
            if np.random.rand(1) > e else env.action_space.sample()

        new_state, reward, done, _ = env.step(action)

        # apply discount
        Q[state, action] = reward + dis * np.max(Q[new_state, :])

        rAll += reward
        state = new_state

    rList.append(rAll)

print("Success rate: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print("LEFT DOWN RIGHT UP")
print(Q)
plt.bar(range(len(rList)), rList, color="blue")
plt.show()
