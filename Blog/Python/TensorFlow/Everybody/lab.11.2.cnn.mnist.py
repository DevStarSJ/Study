import tensorflow as tf


from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


num_input = 784
num_classes = 10 # 0 ~ 9 digits


X = tf.placeholder(tf.float32, [None, num_input]) # 28 * 28 = 784
X_img = tf.reshape(X, [-1, 28, 28, 1]) # img ?x28x28x1 (black/white)
Y = tf.placeholder(tf.float32, [None, num_classes])

keep_prob = tf.placeholder(tf.float32)

# num of filter : 32, size: 3x3, color: 1
W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01))
conv1 = tf.nn.conv2d(X_img, W1, strides=[1, 2, 2, 1], padding='SAME') # ?x28x28x32
relu1 = tf.nn.relu(conv1)
L1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME') # ?x14x14x32

# L2 input : ?x14x14x32
# num of filter : 64, size: 3x3, color: 32(전 layer의 filter수)
W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01))
conv2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME') # ?x14x14x64
relu2 = tf.nn.relu(conv2)
print(relu2.shape)
L2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], padding='SAME') # ?x7x7x64
print(L2.shape)
L2 = tf.reshape(L2, [-1, 7 * 7 * 64]) # Make fully-connected layer : ?x3136

# Final Fully-connected Layer : 7x7x64 -> 10
W3 = tf.get_variable("W3", shape=[7*7*64, num_classes], initializer=tf.contrib.layers.xavier_initializer())
b = tf.Variable(tf.random_normal([num_classes]))
hypothesis = tf.matmul(L2, W3) + b

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
            feed_dict = {X: batch_xs, Y: batch_ys}
            c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
            avg_cost += c / total_batch

        print("Epoch: ", epoch + 1, 'cost = ', avg_cost)

    print("Accuracy: ", accuracy.eval(session=sess, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))
