import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def MinMaxScaler(data):
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    return numerator / (denominator + 1e-7)

timesteps = seq_length = 7
data_dim = 5
hidden_dim = 10
output_dim = 1
learning_rate = 0.01
iterations = 500

xy = np.loadtxt('data-02-stock_daily.csv', delimiter=',')
xy = xy[::-1] # reverse order
xy = MinMaxScaler(xy)
x = xy
y = xy[:, [-1]]

# input data

dataX = []
dataY = []

for i in range(0, len(y) - seq_length):
    _x = x[i: i + seq_length]
    _y = y[i + seq_length]
    print(i, _x, '->', _y)

    dataX.append(_x)
    dataY.append(_y)

# split to train and testing
train_size = int(len(dataY) * 0.7)
test_size = len(dataY) - train_size
trainX, testX = np.array(dataX[:train_size]), np.array(dataX[train_size:])
trainY, testY = np.array(dataY[:train_size]), np.array(dataY[train_size:])

#print(len(trainY), len(testY),)


batch_size = len(dataX)


X = tf.placeholder(tf.float32, [None, seq_length, data_dim]) # X one-hot
Y = tf.placeholder(tf.float32, [None, 1]) # Y label

cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_dim, state_is_tuple=True, activation=tf.tanh)
outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
Y_pred = tf.contrib.layers.fully_connected(outputs[:, -1], output_dim, activation_fn=None)

# cost / loss
loss = tf.reduce_sum(tf.square(Y_pred - Y))
train = tf.train.AdamOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(iterations):
        l, _ = sess.run([loss, train], feed_dict={X: trainX, Y: trainY})
        print(i, l)

    testPredict = sess.run(Y_pred, feed_dict={X: testX})

    plt.plot(testY, 'r')
    plt.plot(testPredict)
    plt.show()

