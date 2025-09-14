from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

mnist_builder = tfds.builder("mnist")
mnist_builder.download_and_prepare()

info = mnist_builder.info
print(info)

mnist_train = mnist_builder.as_dataset(split="train")

fig = tfds.show_examples(info, mnist_train, rows=3, cols=3)
fig.savefig('output/mnist_examples.png')

plt.show()