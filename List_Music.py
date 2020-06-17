import json
import requests
from bs4 import BeautifulSoup
import urllib.request


def get_html(target_url):
    '''伪装头部，向目标url发出请求，获取页面内容'''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'http://music.163.com/',
        'Host': 'music.163.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    req = urllib.request.Request(target_url, headers=headers)
    req = urllib.request.urlopen(req)
    html = req.read().decode('utf-8')
    return html


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    main = soup.find('ul', {'class': 'f-hide'})
    music_url_list = []
    for music in main.find_all('a'):
        # one_music = ()
        # print('{} : {}'.format(music.text, music['href']))
        musicUrl = 'http://music.163.com/song/media/outer/url' + \
            music['href'][5:]+'.mp3'
        musicName = music.text
        # 单首歌曲的名字和地址放在list列表中
        one_music = (musicName, musicUrl)
        # list.append(musicUrl)
        # 全部歌曲信息放在lists列表中
        music_url_list.append(one_music)
    return music_url_list


def down_music(url_list):
    # 下载列表中的全部歌曲，并以歌曲名命名下载后的文件，文件位置为当前文件夹
    for i in lists:
        name, url = i[0], i[1]
        try:
            print('正在下载', name)
            urllib.request.urlretrieve(
                url, '/Users/money666/Desktop/msc-crawler/down_music/%s.mp3' % name)
            print('下载成功')
        except:
            print('下载失败')


if __name__ == "__main__":
    play_url = 'http://music.163.com/playlist?id=420317034'
    con = get_html(play_url)
    lists = get_content(con)
    down_music(lists)
