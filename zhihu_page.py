# -*- coding: utf-8 -*-

"""
@File    : zhihuJokesSpider.py
@Author  : fungis@163.com
@Time    : 2020/03/07 17:41
@notice  : 爬取知乎回答的内容
"""
import re
import os
import time
import random
import pandas
import requests
import requests
import pandas
import openpyxl

class zhihuJokesSpider():
    def __init__(self, question_id, **kwargs):
        self.question_id = question_id
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate'
        }
        self.api_url = 'https://www.zhihu.com/node/QuestionAnswerListV2'
        self.session = requests.Session()
        self.pointer = 0
        self.limits = 2000

    '''开始运行'''

    def start(self):
        offset = -1
        size = 1
        jokes = []
        while self.pointer <= self.limits:
            offset += size
            data = {
                'method': 'next',
                'params': '{"url_token":%s,"page_size":%s,"offset":%s}' % (self.question_id, size, offset)
            }
            response = self.session.post(self.api_url, headers=self.headers, data=data)
            try:
                joke = eval(response.text)['msg'][0].replace('\\', '')
                joke = re.findall(r'<p>(.*?)</p>', joke)
                joke_filtered = []
            except:
                break
            for item in joke:
                if '<br>' in item: item = item.replace('<br>', '')
                if '<b>' in item: item = item.replace('<b>', '')
                if '</b>' in item: item = item.replace('</b>', '')
                if len(item) < 8: continue;
                if 'www.zhihu.com' in item: continue;
                joke_filtered.append(item)
            joke = '\n'.join(joke_filtered)
            print(joke)
            jokes.append(joke)
            time.sleep(random.randint(0, 1) + random.random())
            self.pointer += 1
        if not os.path.exists(str(self.question_id)):
            os.mkdir(str(self.question_id))
        jokes = list(filter(None, jokes))  # 只能过滤空字符和None
        data = pandas.DataFrame(jokes, columns=['内容'])
        # data.dropna(axis=0, how='any', inplace=True)  # 删除空值的行数据
        data.to_excel(os.path.join(str(self.question_id)) + os.sep + 'show.xlsx', encoding='gbk')  # 写入excel中进行输出


'''run'''
if __name__ == '__main__':
    question_id = '24279087'  # 问题的ID
    client = zhihuJokesSpider(question_id)
    client.start()

