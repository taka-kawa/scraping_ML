import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ユーザー名とパスワードの指定
USER = "JS-TESTER"
PASS = "ipCU12ySxI"

# セッション開始
session = requests.session()

# login *1
login_info = {
    "username_mmlbbs6":USER, # ユーザー名指定
    "password_mmlbbs6":PASS, # パスワード指定
    "back":"index.php", # ログイン時に指定する値
    "mml_id":"0" # ログイン時に指定する値
}
url_login = "http://uta.pw/sakusibbs/users.php?action=login&m=try"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外

# pick up url of my page *2
soup = BeautifulSoup(res.text, "html.parser")
a = soup.select_one(".islogin a")
if a is None:
    print("マイページが取得できませんでした")
    quit()
# 相対urlを絶対urlに変換
url_mypage = urljoin(url_login, a.attrs["href"])
print("マイページ=", url_mypage)

# access my page *3
res = session.get(url_mypage)
res.raise_for_status()

# お気に入りの詞のタイトルを列挙 *4
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select("#favlist li  > a")
for a in links:
    href = a.attrs["href"]
    title = a.get_text()
    print("-", title, ">", href)
