import tensorflow as tf
import numpy as np


def index_to_one_hot(index_list, count=None):

    if count is None:
        count = int(max([x[0] for x in index_list]) + 1)

    result = []

    for one in index_list:
        element = [0 for _ in range(count)]
        element[int(one)] = 1
        result.append(element)

    return result


xy = np.loadtxt('data-04-zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = index_to_one_hot(xy[:, [-1]])


input_num = len(x_data[0])
nb_classes = len(y_data[0])

X = tf.placeholder(tf.float32, [None, input_num])
Y = tf.placeholder(tf.float32, [None, nb_classes])

W = tf.Variable(tf.random_normal([input_num, nb_classes]), name="weight")
b = tf.Variable(tf.random_normal([nb_classes]), name="bias")

hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

feed_dict = {X: x_data, Y: y_data}

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run(optimizer, feed_dict=feed_dict)
        if step % 200 == 0:
            print(step, sess.run(cost, feed_dict=feed_dict))

    all = sess.run(hypothesis, feed_dict={X: [[0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0]]})
    print(all, sess.run(tf.argmax(all, 1)))