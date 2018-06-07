# code=utf-8
from bs4 import BeautifulSoup
import requests
import os
#创建文件目录
#exist_ok=True python3.2引入，默认False，当存在目录发生异常，抛出；设置为True，目录存在不抛出异常
os.makedirs('./ifanr/imgs', exist_ok=True)

URL = 'http://www.ifanr.com/'
#get，requests方法，使用get方法获得网页
html = requests.get(URL).text
#使用beautifulSoup，解析为Lxml
soup = BeautifulSoup(html, 'lxml')
#查找需要资源。找到img项目，class=‘tranform-img’的
#这一步一般先观察网页资源的规律，然后使用方法找到资源
imgs = soup.find_all('img', {'class': 'tranform-img'})

#取出对应图片，存储到对应的文件夹中
#stream=True,推迟下载，不是立刻下载。只有当所有数据都下载完了，或者response.close时，才进行下载。
#配合chunk，可以让流媒体文件加载一段时间后，就进行下载，下面格式牢记
for img in imgs:
    url = img['src']
    r = requests.get(url, stream=True)
    image_name = url.split('/')[-1]
    with open('./ifanr/imgs/%s' % image_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)
    print('saved %s' % image_name)
