# cronと定期的なクローリング
## 定期的なクローリングについて
定期的に処理を実行する仕掛けとして、cronというデーモンプロセス(処理要求を待ち続け、要求があると自分自身をコピーしたプロセスを作り、コピーしたプロセスに処理を実行させる)がある。
cronを利用すると、スクリプトを自動実行することができる。同様の機能を持つものとして、Windowsなら「タスク　スケジューラ」がある。

## cronの機能
- データ収集などアプリ内で必要となる定期的処理
  - クローリング、DB集計など
- ログやバックアップなどシステム関連の定期的処理
  - ログファイル差し替え、バックアップなど
- システムが正しく動作しているか定期的に監視する処理
  - システムが止まっていれば、管理者にメール通知など

## 為替情報を毎日保存
[クジラ外国為替確認API](http://api.aoikujira.com/kawase/)を利用  
[プログラム](./programs/everyday_kawase.py)

## cronの設定
本書では「nano」エディタをインストールしているが、今回はvimで行う。  
[vimの使い方](http://qiita.com/honeniq/items/201156650310c4968c3a)
- cronの設定を行う時は、「crontab」コマンドを使う
- 起動するときは、「-e」オプションをつける

~~~
$ crontab -e
~~~

毎日、朝の７時に[プログラム](./programs/everyday_kawase.py)を実行するプログラムを起動するように設定

~~~
0 7 * * * /path/to/python3 /path/to/everyday_kawase.py
~~~

注意する点として、cronの実行時には、環境変数が最低限しか設定されてないということ。設定ファイルの冒頭で環境変数を設定できる。
PATHを指定するとコマンドで絶対パスを指定しなくてもよくなる。

~~~
PATH=/usr/local/bin/:/usr/bin:/bin
PYTHONIOENCODING='utf-8'

0 7 * * * python3 /home/test/everyday_kawase.py
~~~

何もいじらないと...

~~~
SHELL=/bin/sh
USER=kawashimatakashi
PATH=/usr/bin:/bin
PWD=/Users/kawashimatakashi
SHLVL=1
HOME=/Users/kawashimatakashi
LOGNAME=kawashimatakashi
_=/usr/bin/env
~~~
cdで移動しないと為替情報(.json)がPWDの場所で作られるので注意
~~~
* * * * * cd DIR ; ./PROGRAM
~~~

## crontabの記述方法の詳細
基本的な書式

~~~
（分）（時）（日）（月）（曜日）実行するコマンドのパス
~~~

|項目|説明|
|:--:|:--:|
|分|0-59|
|時|0-23|
|日|1-31|
|月|1-12|
|曜日|0-7(0または7は日曜日)|

|名前|利用例|説明|
|:--:|:--:|:--:|
|リスト|0,10,30|0,10,30という値をそれぞれ指定する|
|範囲|1-5|1,2,3,4,5という範囲を指定|
|間隔|*/10|10,20,30と10間隔で指定|
|ワイルドカード|*|ワイルドカードで指定|

月末のみ処理を行いたい場合
~~~
50 23 28-31 * * /usr/bin/test $(date -d '+1 day' +%d) -eq 1 && 実行したいコマンド
~~~
