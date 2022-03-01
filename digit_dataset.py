#The "load_digits" dataset contains approximately 1800 images of handwritten digits 0 through 9.
# Each image is 8x8 which translates to 64 attributes per image.

from sklearn import datasets
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import pandas as pd

digits = datasets.load_digits(n_class=8,as_frame=True)
print(digits.data.shape)

plt.figure(1, figsize=(5,5), facecolor=('red'), edgecolor=('blue'))
plt.imshow(digits.images[5], cmap=plt.cm.gray_r, interpolation="bicubic")
plt.show()
************************************************************************************************
digits2 = load_digits()
print(digits2.data.shape)

plt.gray()
plt.matshow(digits2.images[0])
plt.show()
************************************************************************************************
digits = pd.DataFrame(datasets.load_digits().data)
digits['target'] = datasets.load_digits().target
digits.tail()

digits_matrix = datasets.load_digits().data

plt.figure(figsize=(10,10))
plt.imshow(digits_matrix[0].reshape(8,8))
plt.show()
