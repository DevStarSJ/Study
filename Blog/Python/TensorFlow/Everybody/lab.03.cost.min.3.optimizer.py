import tensorflow as tf

xs = [1, 2, 3]
ys = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name='weight')
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
hypothesis = X * W

cost = tf.reduce_mean(tf.square(hypothesis - Y))
learning_rate = 0.1

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

W_val = []
cost_val = []

for step in range(51):
    sess.run(train, feed_dict={X: xs, Y: ys})
    print(step, sess.run(W))
