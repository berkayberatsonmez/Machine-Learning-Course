from sklearn import datasets
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = datasets.load_digits(n_class=8,as_frame=True)
print(digits.data.shape)

plt.figure(1, figsize=(5,5), facecolor=('red'), edgecolor=('blue'))
plt.imshow(digits.images[5], cmap=plt.cm.gray_r, interpolation="bicubic")
plt.show()

digits2 = load_digits()
print(digits2.data.shape)

plt.gray()
plt.matshow(digits2.images[0])
plt.show()
