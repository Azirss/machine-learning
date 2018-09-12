import tensorflow as tf
h = tf.constant('Hello, TensorFlow')
sess = tf.Session()
print(sess.run(h))