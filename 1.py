# 1.使用tensorflow2.0完成以下操作（每小题10分）
import tensorflow as tf
# (1)矩阵创建
# ①创建一个维度为3*3的全1矩阵
to=tf.ones([3,3])
# ②使用range，创建一个1-9的1阶张量
tr=tf.range(start=1,limit=10)
# ③打印上题的维度
print(tr.shape)
# ④将上题维度修改为3,1,3
tr1=tf.reshape(tr,shape=[3,1,3])
# ⑤使用函数，去除维度中函数1的维度
ts=tf.squeeze(tr1)
# (2)切片及其他
# ①使用1-9的向量，使用切片，打印3,4,5,6  1，2，3，4，5，6，7，8，9 a[2:5]
t1=ts[2:6]
tf.print(t1)
# ②打印上题向量的均值
tf.print(tf.reduce_mean(t1))
# ③创见一个2行2列的标准正态分布矩阵
t3=tf.random.normal([2,2])
tf.print(t3)
# ④创建一个2行2列的全0矩阵
t2=tf.zeros([2,2])
tf.print(t2)
# ⑤将3,4问的结果拼接成一个4行2列的结果
tf.print(tf.concat([t3, t2], axis=0))