import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


num_input = 784
num_classes = 10 # 0 ~ 9 digits
num_l4 = 625

class Model:

    def __init__(self, sess, name):
        self.sess = sess
        self.name = name
        self._build_net()


    def _build_net(self):
        with tf.variable_scope(self.name):
            self.X = tf.placeholder(tf.float32, [None, 784])
            X_img = tf.reshape(self.X, [-1, 28, 28, 1])
            self.Y = tf.placeholder(tf.float32, [None, 10])
            self.keep_prob = tf.placeholder(tf.float32)

            # num of filter : 32, size: 3x3, color: 1
            W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01))
            L1 = tf.nn.conv2d(X_img, W1, strides=[1, 1, 1, 1], padding='SAME')  # ?x28x28x32
            L1 = tf.nn.relu(L1)
            L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')  # ?x14x14x32
            L1 = tf.nn.dropout(L1, self.keep_prob)

            # L2 input : ?x14x14x32
            # num of filter : 64, size: 3x3, color: 32(전 layer의 filter수)
            W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01))
            L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')  # ?x14x14x64
            L2 = tf.nn.relu(L2)
            L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')  # ?x7x7x64
            L2 = tf.nn.dropout(L2, self.keep_prob)

            # L3
            W3 = tf.Variable(tf.random_normal([3, 3, 64, 128], stddev=0.01))
            L3 = tf.nn.conv2d(L2, W3, strides=[1, 1, 1, 1], padding='SAME')  # ?x7x7x64
            L3 = tf.nn.relu(L3)
            L3 = tf.nn.max_pool(L3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')  # ?x4x4x128
            L3 = tf.nn.dropout(L3, self.keep_prob)
            L3 = tf.reshape(L3, [-1, 4 * 4 * 128])  # Make fully-connected layer : ?x3136

            # L4 FC
            W4 = tf.get_variable("W4", shape=[4 * 4 * 128, num_l4], initializer=tf.contrib.layers.xavier_initializer())
            b4 = tf.Variable(tf.random_normal([num_l4]))
            L4 = tf.nn.relu(tf.matmul(L3, W4) + b4)
            L4 = tf.nn.dropout(L4, self.keep_prob)

            # L5 FC
            W5 = tf.get_variable("W5", shape=[num_l4, num_classes], initializer=tf.contrib.layers.xavier_initializer())
            b5 = tf.Variable(tf.random_normal([num_classes]))
            self.logits = tf.matmul(L4, W5) + b5

            # Softmax
            self.cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=self.logits, labels=self.Y))
            self.optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(self.cost)

            # Test model
            is_correct = tf.equal(tf.argmax(self.logits, 1), tf.argmax(self.Y, 1))
            self.accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))


    def predict(self, x_test, keep_prop=1.0):
        return self.sess.run(self.logits,
                 feed_dict={self.X: x_test, self.keep_prob: keep_prop})


    def train(self, x_data, y_data, keep_prob=0.7):
        return self.sess.run([self.cost, self.optimizer],
                 feed_dict= {self.X: x_data, self.Y: y_data, self.keep_prob: keep_prob})


    def get_accuracy(self, x_test, y_test, keep_prop=1.0):
        return self.sess.run(self.accuracy,
                feed_dict= {self.X: x_test, self.Y: y_test, self.keep_prob: keep_prop})


sess = tf.Session()
models = [Model(sess, "m" + str(i)) for i in range(7)]

sess.run(tf.global_variables_initializer())

# training parameters
training_epochs = 1
batch_size = 100


for epoch in range(training_epochs):
    avg_cost_list = np.zeros(len(models))
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)

        for idx, m in enumerate(models):
            c, _ = m.train(batch_xs, batch_ys)
            avg_cost_list[idx] += c / total_batch

    print("Epoch: ", epoch + 1, 'cost = ', avg_cost_list)

for m in models:
    print(m.get_accuracy(mnist.test.images, mnist.test.labels))

#print("Accuracy: ", accuracy.eval(session=sess, feed_dict={X: mnist.test.images, Y: mnist.test.labels, keep_prob: 1}))

# Test model and check accuracy
test_size = len(mnist.test.labels)
predictions = np.zeros(test_size * 10).reshape(test_size, 10)

for idx,m in enumerate(models):
    print(idx, 'Accuracy: ', m.get_accuracy(mnist.test.images, mnist.test.lables))
    p = m.predict(mnist.test.images)
    predictions += p

ensemble_correct_prediction = tf.equal(tf.argmax(predictions, 1), tf.argmax(mnist.test.labels, 1))
ensemble_accuracy = tf.reduce_mean(tf.cast(ensemble_correct_prediction, tf.float32))
print('Ensemble accuracy: ', sess.run(ensemble_accuracy))