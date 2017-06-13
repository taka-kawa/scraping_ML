# Webのデータの様々なデータフォーマット
## テキストデータとバイナリデータ
### テキストデータ
一般的なテキストエディタを利用して編集することのできるフォーマット。英数字、漢字、ひらがななどの文字から構成される。改行やタブなどの制御文字が含まれるが、それ以外はエディタで視認できる。文字コードに注意。

### バイナリデータ
テキストデータ以外のデータ。文字と関係なく本来データが利用できるデータ領域をフルに活用したデータ形式。人間が視認できる文字列が現れるとは限らない。バイナリデータは、データを効率よく格納した形式。画像ファイルでよく使われる。

|データの種類|説明|
|::|::|
|テキストデータ|[長所]テキストエディタであれば編集できる。また、説明を含めることができるので可読性が高い。<br>[短所]バイナリデータに比べてサイズが大きい。|
|バイナリデータ|[長所]テキストデータに比べてサイズが小さい。<br>[短所]テキストエディタで編集できない。何バイト目に何のデータを指定するのか定義が必要。|

## XMLの解析
XML(Extensible Markup Language)：個別の目的に応じて、データをタグづけするマークアップ言語のための汎用的な仕様。データを階層的に表現できる。

基本的な構造

~~~
<要素名 属性="属性値">内容</要素名>
~~~

複数の値を指定

~~~
<商品 id="S001" 値段="4500">SDカード</商品>
~~~

グループ化

~~~
<商品グループ type="電子機器">
  <商品 id="S001" 値段="4500">SDカード</商品>
  <商品 id="S002" 値段="3200">マウス</商品>
</商品グループ>
~~~

### 地域防災拠点データを読み込む
[横浜市>総務局>防災関連データ](http://www.city.yokohama.lg.jp/somu/org/kikikanri/data/)

XML形式の地域防災拠点データを読み込んで、区ごとに防災拠点の名前一覧を出力するプログラム

[プログラム](./programs/xml_bousai.ipynb)

## JSONの解析
JSON(JavaScript Object Notation)：テキストデータをベースとした軽量なデータ形式。拡張子は「.json」

### 構造
|データ型|表現方法|利用例|
|::|::|::|
|数値|数字|30|
|文字列|ダブルクウォートで括る|"str"|
|真偽型|trueかfalse|true|
|配列|[n1,n2,n3,...]|[1,2,4,5]|
|オブジェクト|["key";value, "key":value,...]|["org":50, "com":10]
|null|null|null|

### 読み込みと書き込み
読み込み

~~~
json.load(open(jsonfile, "r", encoding="utf-8"))
~~~

書き込み

~~~
json.dumps(obj)
~~~

## YAMLを解析
インデントを利用して階層構造を表現するという特徴を持ったデータ形式。テキストデータ。Ruby on Railsに使われる。スペース文字によるインデントを利用。

|関数名|説明|
|::|::|
|yaml.load(str)|文字列str(YAML)を解析|
|yaml.dump(v)|PythonデータvをYAML形式で出力|

### データ形式
配列

~~~
- banana
- kiwi

- mango
~~~

配列の中に配列(半角スペースでインデント)

~~~
- Yellow
-
  - banana
  - orange
- Red
-
  - apple
  - strawberry
~~~

ハッシュ

~~~
name: Taro
age: 4
color: brown
~~~

インデントで階層構造を表現

~~~
name: Taro
property:
  age: 4
  color: brown
~~~

jsonのような記述方法も

~~~
# コメントもかける
- name: Taro
  favorites: ["banana", "miso soup"]
- name:Mike
  favorites: ["orange", "candy"]
~~~

アンカーとエイリアスの利用
「&name」で印付。「\*name」で参照。

~~~
# 色を定義
color_define:
  - &color1 "#FF0000"
  - &color2 "#00FF00"
  - &color1 "#0000FF"

# 色設定を記述
frame_color:
  title: *color1
  logo: *color2
~~~

## CSV/TSV
Excelで作成されることが多い。
CSV(Comma-Separated Values)：各フィールドがカンマで区切られているデータ
TSV(Tab-Separated Vlaues)：CSVのタブバージョン

書き方

~~~
"姓","名","生年月日","郵便番号","住所","電話番号"
"山田","太郎","2001/1/1","100-0002","東京都千代田区皇居外苑","03-1234-5678"
"山田","次郎","2001/1/2","251-0036","神奈川県藤沢市江の島１丁目","03-9999-9999"
~~~

|姓|名|生年月日|郵便番号|住所|電話番号|
|::|::|::|::|::|::|
|山田|太郎|2001/1/1|100-0002|東京都千代田区皇居外苑|03-1234-5678|
|山田|次郎|2001/1/2|251-0036|神奈川県藤沢市江の島１丁目|03-9999-9999|

PythonでCSVを読み込むときはcsvモジュールを利用する。

読み込み

~~~
import csv, codecs

# CSVファイルを開く
filename = "file.csv"
fp = codecs.open(filename, "r", "utf-8")

# 1行ずつ読む
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
  print(cells[1], cells[2])
~~~

書き込み

~~~
import csv, codecs

with codecs.open("file.csv", "w", "shift-jis") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "商品名", "値段"])
    writer.writerow(["1000", "SDカード", "300"])
~~~

## Excelファイル解析
[読み込みプログラム](./programs/excel_read.ipynb)

[書き込みプログラム](./programs/excel_write.ipynb)

[Pandasを利用](./programs/exce_read_pd.ipynb)
