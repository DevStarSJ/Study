import tensorflow as tf


from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


num_input = 784
num_classes = 10 # 0 ~ 9 digits
num_l4 = 625


X = tf.placeholder(tf.float32, [None, num_input]) # 28 * 28 = 784
X_img = tf.reshape(X, [-1, 28, 28, 1]) # img ?x28x28x1 (black/white)
Y = tf.placeholder(tf.float32, [None, num_classes])

keep_prob = tf.placeholder(tf.float32)


# num of filter : 32, size: 3x3, color: 1
W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01))
L1 = tf.nn.conv2d(X_img, W1, strides=[1, 1, 1, 1], padding='SAME') # ?x28x28x32
L1 = tf.nn.relu(L1)
L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME') # ?x14x14x32
L1 = tf.nn.dropout(L1, keep_prob)

# L2 input : ?x14x14x32
# num of filter : 64, size: 3x3, color: 32(전 layer의 filter수)
W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01))
L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME') # ?x14x14x64
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME') # ?x7x7x64
L2 = tf.nn.dropout(L2, keep_prob)

# L3
W3 = tf.Variable(tf.random_normal([3, 3, 64, 128], stddev=0.01))
L3 = tf.nn.conv2d(L2, W3, strides=[1, 1, 1, 1], padding='SAME') # ?x7x7x64
L3 = tf.nn.relu(L3)
L3 = tf.nn.max_pool(L3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME') # ?x4x4x128
L3 = tf.nn.dropout(L3, keep_prob)
L3 = tf.reshape(L3, [-1, 4 * 4 * 128]) # Make fully-connected layer : ?x3136

# L4 FC
W4 = tf.get_variable("W4", shape=[4*4*128, num_l4], initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([num_l4]))
L4 = tf.nn.relu(tf.matmul(L3, W4) + b4)
L4 = tf.nn.dropout(L4, keep_prob)

# L5 FC
W5 = tf.get_variable("W5", shape=[num_l4, num_classes], initializer=tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random_normal([num_classes]))
hypothesis = tf.matmul(L4, W5) + b5


# Softmax
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
            feed_dict = {X: batch_xs, Y: batch_ys, keep_prob: 0.7}
            c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
            avg_cost += c / total_batch

        print("Epoch: ", epoch + 1, 'cost = ', avg_cost)

    print("Accuracy: ", accuracy.eval(session=sess, feed_dict={X: mnist.test.images, Y: mnist.test.labels, keep_prob: 1}))
