import gym
from gym.envs.registration import register
import readchar


# In[2]:

# MACROS    
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

# Key mapping
array_keys = {
    '\x1b[A' : UP,
    '\x1b[B' : DOWN,
    '\x1b[C' : RIGHT,
    '\x1b[D' : LEFT}


# In[3]:


# Register FrozenLake with is_slippery False
register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': True}
)

env = gym.make('FrozenLake-v3')
env.render() # Show the initial board

while True:
    # Choose an action from keyboard
    key = readchar.readkey()
    if key not in array_keys.keys():
        print("Game aborted!")
        break
        
    action = array_keys[key]
    state, reward, done, info = env.step(action)
    env.render() # Show the board after action
    print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)
    
    if done:
        print("Finished with reward", reward)
        break

