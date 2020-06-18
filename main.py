import json

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from down_music import Spider


class Item(BaseModel):
    # 请求体内容，包含请求歌曲名、请求歌曲序号（下载）、请求歌手（功能暂定）
    id: int = None
    name: str = None
    artist: str = None


app = FastAPI()
spider = Spider()


@app.post("/name")
def search_by_name(item: Item):
    if item.name:
        songs_list = spider.get_songs_list(item.name)
        return json.dumps(songs_list, unsure_ascii=False)
    else:
        return None


# @app.post("/id")
# def search_by_id(item: Item):
#     if item.id:
#         song_downpath = spider.
#     else:
#         error_text = '没有搜到此歌曲，请换个关键字'
#         return error_text


if __name__ == '__main__':
    uvicorn.run(app)
