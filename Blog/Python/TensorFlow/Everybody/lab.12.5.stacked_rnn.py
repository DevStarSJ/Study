import tensorflow as tf
import numpy as np


sentence = "if you want to build a ship, don't drum up people together to collect wood and don't assign them tasks and work, but rather teach them to long for the endless immensity of the sea."

idx2char = list(set(sentence))
char2idx = {c: i for i, c in enumerate(idx2char)}

# hyper parameters
dic_size = len(char2idx) # rnn input
hidden_size = len(char2idx) # rnn output
num_classes = len(char2idx) # final output (softmax)
batch_size = 1
sequence_length = len(sentence) - 1 # number of lst unfolding (unit #)
seq_length = 10

# input data

dataX = []
dataY = []

for i in range(0, len(sentence) - seq_length):
    x_str = sentence[i: i+seq_length]
    y_str = sentence[i+1: i+seq_length+1]
    print(i, x_str,'->',y_str)

    x = [char2idx[c] for c in x_str]
    y = [char2idx[c] for c in y_str]

    dataX.append(x)
    dataY.append(y)

batch_size = len(dataX)


X = tf.placeholder(tf.int32, [None, seq_length]) # X one-hot
Y = tf.placeholder(tf.int32, [None, seq_length]) # Y label
X_one_hot = tf.one_hot(X, num_classes)

cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
cell = tf.contrib.rnn.MultiRNNCell([cell] * 2, state_is_tuple=True)

outputs, _states = tf.nn.dynamic_rnn(cell, X_one_hot, dtype=tf.float32)

# Softmax Layer
# wide to sequential
X_for_softmax = tf.reshape(outputs, [-1, hidden_size])

softmax_w = tf.get_variable("softmax_w", [hidden_size, num_classes])
softmax_b = tf.get_variable("softmax_b", [num_classes])

outputs = tf.matmul(X_for_softmax, softmax_w) + softmax_b
# sequential to wide
outputs = tf.reshape(outputs, [batch_size, seq_length, num_classes])

# Cost : sequence_loss
weights = tf.ones([batch_size, seq_length])
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs, targets=Y, weights=weights)
loss = tf.reduce_mean(sequence_loss)
train = tf.train.AdamOptimizer(learning_rate=0.1).minimize(loss)

prediction = tf.argmax(outputs, axis=2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(500):
        l, _, results = sess.run([loss, train, outputs], feed_dict={X: dataX, Y: dataY})

        for j, result in enumerate(results):
            index = np.argmax(result, axis=1)
            print(i, j, ''.join([idx2char[t] for t in index]), l)
