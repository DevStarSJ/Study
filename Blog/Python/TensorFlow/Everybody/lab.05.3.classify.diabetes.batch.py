import tensorflow as tf


filename_queue = tf.train.string_input_producer(
    ['data-03-diabetes.csv'],
    shuffle=False, name='filename_queue')

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

record_defaults = [[0.] for _ in range(9)]

xy = tf.decode_csv(value, record_defaults=record_defaults)

train_x_batch, train_y_batch = tf.train.batch([xy[0:-1], xy[-1:]], batch_size=10)

x_num = len(xy[0:-1])

X = tf.placeholder(tf.float32, shape=[None, x_num])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([x_num, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis))
learning_rate = 0.1

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

print("before run")


for step in range(10001):
    x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
    cost_val, _ ,  _ = sess.run([cost, hypothesis, train], feed_dict={X: x_batch, Y: y_batch})
    if step % 1000 == 0:
        print(step, "Cost: ", cost_val)

x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
print(sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_batch, Y: y_batch}))

coord.request_stop()
coord.join(threads)

