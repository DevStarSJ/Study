import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np
import pprint


pp = pprint.PrettyPrinter(indent=4)
sess = tf.InteractiveSession()


# Unique chars (vocaulary) : one hot encoding
# voc index : dictionary

h = [1, 0, 0, 0, 0]
i = [0, 1, 0, 0, 0]
e = [0, 0, 1, 0, 0]
l = [0, 0, 0, 1, 0]
o = [0, 0, 0, 0, 1]

# input shape : batch size x sequence length x dimension (input case)
# output shape : batch size x sequence length x hidden size (output case)

batch_size = 1
sequence_length = 6
input_dim = 5
hidden_size = 5

idx2char = ['h', 'i', 'e', 'l', 'o']
x_data = [[0, 1, 0, 2, 3, 3]] # hihell
x_one_hot = [[h, i, h, e, l, l]]

y_data = [[1, 0, 2, 3, 3, 4]] # ihello

X = tf.placeholder(tf.float32, [None, sequence_length, input_dim]) # X one-hot
Y = tf.placeholder(tf.int32, [None, sequence_length]) # Y label

cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
initial_state = cell.zero_state(batch_size, tf.float32)
outputs, _states = tf.nn.dynamic_rnn(cell, X, initial_state=initial_state, dtype=tf.float32)


# Cost : sequence_loss
weights = tf.ones([batch_size, sequence_length])
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs, targets=Y, weights=weights)
loss = tf.reduce_mean(sequence_loss)
train = tf.train.AdamOptimizer(learning_rate=0.1).minimize(loss)

# RNN 에서 나온 결과를 바로 logits으로 사용하는 것은 안좋은 방법이나 간단하게 하기 위해서 그냥 사용했다.

prediction = tf.argmax(outputs, axis=2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(2000):
        l, _ = sess.run([loss, train], feed_dict={X: x_one_hot, Y: y_data})
        result = sess.run(prediction, feed_dict={X: x_one_hot})
        print(i, "loss: ", l , "prediction: ", result, "true Y: ", y_data)

        # print char using dic
        result_str = [idx2char[c] for c in np.squeeze(result)]
        print("\tPrediction str: ", ''.join(result_str))
