import tensorflow as tf

xs = [1, 2, 3]
ys = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name='weight')
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
hypothesis = X * W

cost = tf.reduce_mean(tf.square(hypothesis - Y))
learning_rate = 0.1

# 직접 미분을 구현
gradient = tf.reduce_mean((hypothesis - Y) * X)
decent = W - learning_rate * gradient
update = W.assign(decent)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

W_val = []
cost_val = []

for step in range(51):
    sess.run(update, feed_dict={X: xs, Y: ys})
    print(step, sess.run(cost, feed_dict={X: xs, Y: ys}), sess.run(W))
