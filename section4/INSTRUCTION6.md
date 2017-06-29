# ランダムフォレスト
## ランダムフォレストとは
ランダムフォレスト(Random Forest, Randomized Trees)は、学習用のデータから多数の決定木を元に多数決で結果を決めるため、高い精度。学習データをランダムにサンプリングし、それによって学習した多数の決定木を使用する。

[ランダムフォレスト](./image/randomforest.png)

## ランダムフォレストを使う
[毒キノコのデータ](https://archive.ics.uco.edu/ml/datasets/Mushroom):8124種類のキノコの特徴と毒の有無が記載されているデータセット

~~~python
import urllib.request as req
local = "mushroom.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
req.urlretrieve(url, local)
print("ok")
~~~

一行が一種類のキノコを表す。一列目は毒の有無。

### データを数値に直す時に気をつけること
もしも、次のようにデータに数値を割り振ったとする。

~~~
赤=1, 青=2, 緑=3, 白=4
~~~

数値が連続していると考えたなら、青(2)の二倍が白(4)ということになり、赤(1)と青(2)は値が近いということになる。  
値が分類のための「分類変数」なのか、値が「連続変数」なのかを考えないといけない。  
下記のような例もある。

~~~
赤 = 1000
青 = 0100
緑 = 0010
白 = 0001
~~~


[プログラム](./programs/mushroom_train.ipynb)
