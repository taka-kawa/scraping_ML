# 外国語の文章を判定
## 判定方法
言語はそれぞれの言語ごとにアルファベットの出現頻度が異なるということが知られている。言語とによく使う言い回しや単語が異なるので、それが出現頻度に現れる。そこで、ここでは、テキストデータに登場する「a」から「z」までの出現頻度を調べて、それを特徴量として利用する。

## サンプルデータ
英語、フランス語、インドネシア語、タガログ語  
学習データとして２０個、テストデータとして８個用意。

## 言語判別プログラム

[プログラム](./programs/lang_train.ipynb)

## データごとの分布をグラフにする

[プログラム](./lang_plot.ipynb)

DockerなどのGUIのない環境で実行すると以下のようなエラーが出る。これは、matplotlibに起因する問題。

~~~
_thinter.TclError: no display name and no $DISPLAY environment variable
~~~

この場合下記のように実行するとエラーを回避して、lang-plot.pngというpngファイルが生成される。

~~~
$ export MPLBACKEND="agg"
$ python3 lang_plot.py
~~~

## 学習済みのパラメータを保存する
~~~python
from sklearn import svm
from sklearn.externals import joblib
import json

# 各言語の頻出データ(JSON)を読み込む
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)
    data = d[0]

# データを学習する
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 学習データを保存する
joblib.dump(clf, "./cgi-bin/freq.pkl")
print("ok")
~~~

## Webから使える言語判定アプリ
[プログラム](./cgi-bin/lang-webapp.py)

Python内臓の簡易Webサーバー[(cgi)](https://docs.python.jp/3/library/cgi.html)を使って、プログラムを実行する。Python内臓Webサーバーでは、Pythonのプログラムを<cgi-bin>以下に配置しなければいけない。


実行時

~~~
python3 -m http.server --cgi 8080
~~~

dcokerの場合

~~~
$ docker run -it -v $HOME:$HOME -p 8080:8080 mlearn
~~~

webブラウザーから次のURLに接続

~~~
http://localhost:8080/cgi-bin/lang-webapp.py
~~~
