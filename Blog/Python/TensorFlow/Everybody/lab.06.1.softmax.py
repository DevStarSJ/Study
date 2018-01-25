import tensorflow as tf


def index_to_one_hot(index_list, count=None):
    if count is None:
        count = max(index_list) + 1

    result = []

    for one in index_list:
        element = [0 for _ in range(count)]
        element[one] = 1
        result.append(element)

    return result

x_data = [[1,2,1,1],[2,1,3,2],[3,1,3,4],[4,1,5,5],[1,7,5,5],[1,2,5,6],[1,6,6,6],[1,7,7,7]]
y_data = index_to_one_hot([2,2,2,1,1,1,0,0])

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

    all = sess.run(hypothesis, feed_dict={X: [[1,11,7,9],[1,3,4,3],[1,1,0,1]]})
    print(all, sess.run(tf.argmax(all, 1)))