from urllib.request import urlopen

# pengambilan konten
url = "http://python.org/"
page = urlopen(url, encoding='utf-8')
html = page.read().decode()

# mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

# mengekstrak dan mencetak judul halaman 
title = html[start_index:end_index]
print(title)