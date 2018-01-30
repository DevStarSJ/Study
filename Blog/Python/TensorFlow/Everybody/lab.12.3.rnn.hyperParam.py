import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np
import pprint

sample = "if you want you"

idx2char = list(set(sample))
char2idx = {c: i for i, c in enumerate(idx2char)}

# hyper parameters
dic_size = len(char2idx) # rnn input
hidden_size = len(char2idx) # rnn output
num_classes = len(char2idx) # final output (softmax)
batch_size = 1
sequence_length = len(sample) - 1 # number of lst unfolding (unit #)


# input data

sample_idx = [char2idx[c] for c in sample]
x_data = [sample_idx[:-1]]
y_data = [sample_idx[1:]]


X = tf.placeholder(tf.int32, [None, sequence_length]) # X one-hot
Y = tf.placeholder(tf.int32, [None, sequence_length]) # Y label
X_one_hot = tf.one_hot(X, num_classes)

cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
initial_state = cell.zero_state(batch_size, tf.float32)
outputs, _states = tf.nn.dynamic_rnn(cell, X_one_hot, initial_state=initial_state, dtype=tf.float32)


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
        l, _ = sess.run([loss, train], feed_dict={X: x_data, Y: y_data})
        result = sess.run(prediction, feed_dict={X: x_data})

        result_str = [idx2char[c] for c in np.squeeze(result)]
        print(i, "loss: ", l , "prediction: ", result,  ''.join(result_str))

