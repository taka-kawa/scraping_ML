# データベースについて
データが大量になったり、複雑になった時には、データベースに保存してしまうのが便利。

- データを一元管理できる
- 様々なデータを関連づけて格納できる
- 重複データを認めないなど制約をつけてデータを格納できる
- データの一貫性を確保できる
- 複数人でデータを共有できる
- データへの同時アクセスを処理できる
- 大量のデータでも、少しずつ読み出したり並べ替えたりできる

## データベースの種類
- MySQL/MarinaDB
- PostgreSQL
- MongoDB
- TinyDB
- Microsoft SQL Server
- Oracle Database
- SOLite

## SQLite
お手軽。Webブラウザー内部やAndroid/iOSでも利用されている。データベースのために専用アプリを起動しておく必要がない。

[プログラム](./programs/sqlite_test.ipynb)

## MySQL
高速で使いやすい。ブログやWikiなどさまざまなWebアプリケーションの大規模なデータ保存をするのにも利用されている。

### docker

~~~
$ docker pull ubuntu:16.04
$ docker run -it ubuntu:16.04
$ apt-get update
$ apt-get install -y python3 python3-pip
$ apt-get install -y mysql-server
~~~

MySQLをインストールしている途中で、ルートパスワードを決めるように求められる。pipでmysqlclientをインストール。

~~~
$ apt-get install -y libmysqlclient-dev
$ pip3 install mysqlclient
~~~

以上で環境構築された。

起動

~~~
$ service mysql start
$ mysql -u root -p
~~~

ログインができたら...

~~~
mysql> CREATE DATABASE test;
~~~

### mac
~~~
$ brew update
$ brew install mysql
~~~

起動

~~~
$ mysql.server start

Starting MySQL
. SUCCESS!
~~~

~~~
$ mysql -uroot
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1
Server version: 5.6.20 Homebrew

Copyright (c) 2000, 2014, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
~~~

これで接続できた。

[プログラム](./programs/mysql_test.ipynb)

## TinyDB
SQliteやMySQLはRDBMS。ドキュメント指向データベースは、特にスキーマを定義する必要がない。ドキュメント指向データベースを利用するためのライブラリ。

~~~
pip3 install tinyDB
~~~

[プログラム](./programs/tinydb_test.ipynb)
