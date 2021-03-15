import xlwt
import os
import json
summary = xlwt.Workbook()
sheet1 = summary.add_sheet('sheet1')

with open('zhihu.json',encoding='utf8') as f:
    data=json.loads(f.read())

titles=['昵称', '性别', '签名', '回答内容', '点赞', '评论']
for col_idx, stuff in enumerate(titles):
    print("writing:", 0, col_idx, stuff)
    sheet1.write(0, col_idx, stuff)

for row_idx,item in enumerate(data["data"]):
    if item is None: continue

    author=item.get('author').get('name')
    gender_id=item.get('author').get('gender')
    gender='M' if gender_id==1 else 'F'
    headline=item.get('author').get('headline')

    content=item.get("content")

    n_like=item.get("voteup_count")
    n_comment=item.get("comment_count")


    content=[author,gender,headline,content,n_like,n_comment]

    for col_idx,stuff in enumerate(content):
        print("writing:",row_idx+1,col_idx,stuff)
        sheet1.write(row_idx+1, col_idx, stuff)

summary.save('zhihu-summary.xls')