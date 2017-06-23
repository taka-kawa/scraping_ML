# 画像の文字認識
## MNIST
手書き数字のデータは、MNISTが公開している手書きデータを利用することにする。学習用に６万点、テスト用に１万点の手書き数字のデータが公開されている。  
[URL](http://yann.lecun.com/exdb/mnist)  

|ファイル名|説明|
|:--:|:--|
|train-images-idx3-ubyte.gz|学習用画像データ|
|train-labels-idx1-ubyte.gz|学習用ラベルデータ|
|t10k-images-idx3-ubyte.gz|テスト用画像データ|
|t10k-labels-idx1-ubyte.gz|テスト用ラベルデータ|

[ダウンロードプログラム](./programs/mnist_download.ipynb)

MNISTデータセットのデータは、独自のデータベース形式でデータが格納されており、実際の画像は、そのデータベースの中に保存されている。

TRAINIG SET LABEL FILE

|offset|type|value|description|
|:--:|:--:|:--:|:--:|
|0000|32 bit integer|0x00000801|マジックナンバー|
|0004|32 bit integer|60000|ラベルアイテムの数|
|0008|unsigned byte|??|１つ目のデータのラベル|
|0009|unsigned byte|??|２つ目のデータのラベル|
|...|...|...|...|

TRAINING SET IMAGE FILE

|offset|type|value|description|
|0000|32 bit integer|0x00000803|マジックナンバー|
|0004|32 bit integer|60000|画像アイテムの数|
|0008|32 bit integer|28|画像のピクセル行数|
|0012|32 bit integer|28|画像のピクセル列数|
|0016|unsigned byte|??|１枚目の画像データ(0,0)|
|0017|unsigned byte|??|１枚目の画像データ(0,1)|
|...|...|...|...|

0が背景で1-255が黒。数値が大きくなるほど濃い黒。  
下記のようなCSVに変換する。

~~~
答えのラベル, 28x28のピクセルデータ
5, 0,0,0,0,0,0,30,80,100,120,0,0,0,0,...
~~~

[プログラム](./mnist_to_csv.ipynb)

## 画像データの学習

[プログラム](./mnist_train.ipynb)
