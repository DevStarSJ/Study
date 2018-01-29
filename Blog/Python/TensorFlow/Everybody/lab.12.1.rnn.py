import tensorflow as tf
import numpy as np
import pprint


# input shape : batch size x sequence length x dimension (input case)
# output shape : batch size x sequence length x hidden size (output case)


pp = pprint.PrettyPrinter(indent=4)
sess = tf.InteractiveSession()

# hidden_size = 4
#
# cell = tf.contrib.rnn.BasicRNNCell(num_units=hidden_size)
# # cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size)
#
# output, _states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)

hidden_size = 4 # 출력값의 개수
sequence_length = 5 # 1,5,4 입출력 matrix shape의 2번째 index 크기
cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size)

# One hot encoding
h = [1, 0, 0, 0]
e = [0, 1, 0, 0]
l = [0, 0, 1, 0]
o = [0, 0, 0, 1]

x_data = np.array([[h, e, l, l, o], [e, o, l, l, l], [l, l, e, e, l]], dtype=np.float32)
print(x_data.shape)
outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)

sess.run(tf.global_variables_initializer())
pp.pprint(outputs.eval())