import xlwt
import os
import json
summary = xlwt.Workbook()
sheet1 = summary.add_sheet('sheet1')

with open('douban.json',encoding='utf8') as f:
    data=json.loads(f.read())

for row_idx,item in enumerate(data["items"]):
    if item is None: continue
    tmp=item.get("target").get("status")
    if tmp is None: continue
    text=tmp.get('text')
    post_time=tmp.get("create_time")
    n_reshare=tmp.get("reshares_count")
    n_like=tmp.get("reactions_count")
    n_comment=tmp.get("comments_count")

    images=tmp.get('images')
    img_url=''
    if images:
        for img in images:
            url=img.get('large').get('url')
            img_url=img_url+url+'\n'

    author=tmp.get("author")
    if author:
        if author.get('loc'):
            location = author.get('loc').get('name')
        else:
            location=None
        poster=author.get('name')


    content=[poster,text,location,n_like,post_time,n_reshare,n_comment,img_url]
    for col_idx,stuff in enumerate(content):
        print("writing:",row_idx,col_idx,stuff)
        sheet1.write(row_idx, col_idx, stuff)

summary.save('summary.xls')