import gym
import numpy as np
import tensorflow as tf

env = gym.make('CartPole-v0')

# Constancts defining out neural network
input_size = env.observation_space.shape[0]
output_size = env.action_space.n
learning_rate = 0.1

X = tf.placeholder(tf.float32, [None, input_size], name="input_x") # state input

# First layer of weights
W1 = tf.get_variable("W1", shape=[input_size, output_size], initializer=tf.contrib.layers.xavier_initializer())

Qpred = tf.matmul(X, W1) # Out Q prediction

# We need to define the parts of the network needed for learning a policy
Y = tf.placeholder(shape=[None, output_size], dtype=tf.float32)

# Loss function
loss = tf.reduce_sum(tf.square(Y - Qpred))

# Learning
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

# Set Q-learning related parameters
dis = .9
num_episodes = 2000

# Create lists to contain total rewards and steps per episode
rList = []

one_hot_mat = np.identity(16)
def one_hot(x):
    return one_hot_mat[x: x+1]

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(num_episodes):
        # Reset environment and get first new observation
        s = env.reset()
        e = 1. / ((i / 10) + 1)
        rAll = 0
        step_count = 0
        done = False
        local_loss = []

        # The Q-Network training
        while not done:
            step_count += 1
            x = np.reshape(s, [1, input_size])
            # Choose an action by greedily (with e chance of random action) from the Q-network
            Qs = sess.run(Qpred, feed_dict={X: x})

            if np.random.rand(1) < e:
                a = env.action_space.sample()
            else:
                a = np.argmax(Qs)

            # Get new state and reward from environment
            s1, reward, done, _ = env.step(a)

            if done:
                # Update Q, and no Qs+1, since it's a terminal state
                Qs[0, a] = -100
            else:
                x1 = np.reshape(s1, [1, input_size])
                # Obtain the Q_s1 values by feeding the new state through our network
                Qs1 = sess.run(Qpred, feed_dict={X: x1})
                # Update Q
                Qs[0, a] = reward + dis * np.max(Qs1)

            # Train out network using target (Y) and predicted Q (Qpred) values
            sess.run(train, feed_dict={X: x, Y: Qs})

            s = s1

        rList.append(step_count)

        # If last 10's avg steps are 500, it's good enough
        print("Episode: {} steps: {}".format(i, step_count))
        if len(rList) > 10 and np.mean(rList[-10:]) > 500:
            break

    # See our trained network in action
    observation = env.reset()
    reward_sum = 0

    while True:
        env.render()

        x = np.reshape(observation, [1, input_size])
        Qs = sess.run(Qpred, feed_dict={X: x})
        a = np.argmax(Qs)

        observation, reward, done, _ = env.step(a)
        reward_sum += reward

        if done:
            print("Total score: {}".format(reward_sum))
            break

