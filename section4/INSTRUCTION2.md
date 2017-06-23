# 機械学習はじめの一歩
## XOR演算を学習させる
論理演算の排他的論理和(XOR)は、下記のような表のように出力される。

|P|Q|P xor Q|
|:--:|:--:|:--:|
|0|0|0|
|1|0|1|
|0|1|1|
|1|1|0|

これを機械学習で学習させる。

[プログラム](./programs/xor_train.ipynb)

## アヤメを品種ごとに分類する
機械学習で、花びらやがく片の長さからアヤメの品種を分類する。  

アヤメのデータをダウンロードする  
[URL](https://github.com/pydata/blob/master/pandas/tests/data/iris.csv)

データを見ると、アヤメが「Iris-setosa」「Iris-versicollor」「Iris-virginica」の三品種に分類されている。また、それぞれのアヤメについて、「SepalLength」「SepalWidth」「PetalLength」「PetalWidth」の情報がある。

[プログラム](./programs/iris_train.ipynb)
