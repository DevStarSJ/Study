import tensorflow as tf


filename_queue = tf.train.string_input_producer(
    ['data-01-test-score.csv'],
    shuffle=False, name='filename_queue')

reader = tf.TextLineReader(skip_header_lines=1)
key, value = reader.read(filename_queue)

record_defaults = [[0.], [0.], [0.], [0.]]

xy = tf.decode_csv(value, record_defaults=record_defaults)

train_x_batch, train_y_batch = tf.train.batch([xy[0:-1], xy[-1:]], batch_size=10)

X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(X, W) + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))
learning_rate = 1e-5

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for step in range(2001):
    x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
    #print(x_batch, y_batch)
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_batch, Y: y_batch})
    #print(step, "Cost: ", cost_val, "Prediction: ", hy_val)

coord.request_stop()
coord.join(threads)

print("Your score will be ", sess.run(hypothesis, feed_dict={X:[[100, 70, 101]]}))
print("Others score will be ", sess.run(hypothesis, feed_dict={X:[[60, 70, 110],[90,100,80]]}))
