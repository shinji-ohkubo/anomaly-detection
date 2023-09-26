# -*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2

df = pd.read_csv("Davis.csv")
# df.describe()

# 体重のヒストグラム
#plt.hist(df["weight"], normed=True)
plt.hist(df["weight"], 20, density=True)
plt.title("Histgram of weight")
plt.xlabel("weight")
plt.ylabel("frequency")
plt.show()

# 2.2.4 ホテリングT2法（1次元）
mu = df["weight"].mean()

x_mu2 = (df["weight"] - mu)**2

# s2 = ((df["weight"] - mu)**2).mean()
s2 = x_mu2.mean()
print("標本平均: {0}".format(mu))   # sample mean
print("標本分散: {0}".format(s2))   # sample variance

plt.hist(x_mu2**0.5, 30, density=True)
plt.title("Histgram of (x - mu)")
plt.xlabel("(x - mu)")
plt.ylabel("frequency")
plt.show()

# a = (df["weight"] - mu)**2 / s2
a = x_mu2 / s2
print("異常度: {0}".format(a))   # anomaly score

th = chi2.isf(1 - 0.99, 1)
print("カイ２乗分布による1%水準の閾値: {0}".format(a))   # threshold

# 異常度をプロット
#plt.plot(range(200), a, "bo")
plt.plot(range(199), a, "bo")
plt.axhline(y=th,color='red')
plt.show()
