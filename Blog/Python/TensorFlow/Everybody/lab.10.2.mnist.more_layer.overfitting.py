import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


num_input = 784
nb_classes = 10 # 0 ~ 9 digits
l1 = 512
l2 = 512
l3 = 512
l4 = 512


X = tf.placeholder(tf.float32, [None, num_input]) # 28 * 28 = 784
Y = tf.placeholder(tf.float32, [None, nb_classes])

W1 = tf.get_variable("W1", shape=[num_input, l1], initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([l1]), name="bias1")
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.get_variable("W2", shape=[l1, l2], initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([l2]), name="bias2")
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.get_variable("W3", shape=[l2, l3], initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([l3]), name="bias3")
L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)

W4 = tf.get_variable("W4", shape=[l3, l4], initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([l4]), name="bias4")
L4 = tf.nn.relu(tf.matmul(L3, W4) + b4)

W5 = tf.get_variable("W5", shape=[l4, nb_classes], initializer=tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random_normal([nb_classes]), name="bias5")
hypothesis = tf.matmul(L4, W5) + b5

# Softmax
#hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)ç
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

# Test model
is_correct = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

# training parameters
training_epochs = 20
batch_size = 100

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            c, _ = sess.run([cost, optimizer], feed_dict={X: batch_xs, Y: batch_ys})
            avg_cost += c / total_batch

        print("Epoch: ", epoch + 1, 'cost = ', avg_cost)

    print("Accuracy: ", accuracy.eval(session=sess, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))
