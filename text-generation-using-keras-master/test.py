import tensorflow as tf
# tf.compat.v1.disable_eager_execution()
# hello = tf.constant('hello,tensorflow')
# sess= tf.compat.v1.Session()
# print(sess.run(hello))

import tensorflow as tf
a = tf.test.is_built_with_cuda()  # 判断CUDA是否可以用
b = tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None) # 判断GPU是否可以用
print(a)
print(b)
print(tf.__version__)