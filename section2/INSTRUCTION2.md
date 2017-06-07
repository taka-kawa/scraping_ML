# ブラウザーを経由したスクレイピング
## Webブラウザーを遠隔操作するSelenium
- Selenium：Webブラウザーを遠隔操作するツール。Webアプリのテストを自動化するのに利用。画面キャプチャを撮ったり、HTMLの任意の部分を取り出せる。複数のWebブラウザーに対応(Google Chrome,IE,Firefox...)
- PhantomJS：コマンドラインから使えるWebブラウザー

## 画面キャプチャ
[プログラム](./programs/selenium_capture.ipynb)

## 会員制サイトにログイン
[プログラム](./programs/selenium_login.ipynb)

## SeleniumでDOM要素を選択する
DOMの中から最初に見つかった要素を一つだけ取得

|メソッド名|説明|
|--|--|
|find_element_by_name(name)|name属性から要素を一つ取得|
|find_element_by_link_text(text)|リンクのテキストから要素を一つ取得|
|find_element_by_class_name(name)|クラス名nameから要素を一つ取得|
|...|...|

DOMの中にある全ての要素を取得

|メソッド名|説明|
|--|--|
|find_elements_by_css_selector(query)|CSSセレクタを指定して複数要素取得|
|find_elements_by_tag_name(name)|タグ名nameの要素を複数取得|
|find_elements_by_class_name(name)|クラス名nameから要素を複数取得|
|...|...|

## Seleniumで要素に対して行う操作
|メソッド名|説明|
|--|--|
|clear()|テキスト入力できる要素でテキストをクリアする|
|click()|要素をクリックする|
|send_keys(value)|キーを送信|
|screenshot()|スクショ|
|...|...|

## より詳しいSeleniumのマニュアル
[Python](http://selenium-python.readthedocs.io/index.html)
[Documentation](http://docs.seleniumhq.org/docs)

## JSを実行
execute_script()：あれがやりたいのにメソッドが用意されてないときにJSを実行する
~~~
from selenium import Webdriver

# PhantomJSのドライバを得る
browser = Webdriver.PhantomJS()
browser.implicitly_wait(3)

# 適当なWebサイトを開く
browser.get("https://google.com")

# JS実行
r = browser.execute_script("return 100 + 50")
print(r)
~~~
