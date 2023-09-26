import requests
from bs4 import BeautifulSoup

html = """
<div> ... </div>
"""

soup = BeautifulSoup(html, 'html.parser')

# 絵文字のURLとエイリアスを抽出
emojis = []
for row in soup.select('.emojiRow-1aPaM-'):
    emoji_url = row.select_one('.emojiImage-1sHmM-')['style'].split('"')[1]
    alias = row.select_one('.emojiInput-B8MGXq')['value']
    emojis.append((emoji_url, alias))

# 絵文字をダウンロードし、エイリアス名で保存
for url, alias in emojis:
    response = requests.get(url)
    file_extension = url.split('.')[-1].split('?')[0]  # webpなどの拡張子を取得
    with open(f"{alias}.{file_extension}", 'wb') as f:
        f.write(response.content)

print("絵文字のダウンロードが完了しました。")
