import requests

url = "https://www.bbc.com/news/articles/c2d7rk0865go"

res = requests.get(url=url)

html = res.text

# print(html)

urls = html.split('<img sizes="(min-width: 1280px) 50vw, (min-width: 1008px) 66vw, 96vw" srcSet="')[1].split('" loading="eager" alt="')[0].split(",")[0].split(" ")[0]
print(urls)

img = requests.get(url=urls)
open("1.webp", "wb").write(img.content)