import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import time
import xlwt

# 设置代理等（新浪微博的数据是用ajax异步下拉加载的，network->xhr）
host = 'm.weibo.cn'
base_url = 'https://%s/api/container/getIndex?' % host
user_agent = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36'
topic_target="我也拒绝月经羞耻"
# end is possible the last one received, to get more, just increase it.
end=20

# 设置请求头
headers = {
    'Host': host,
    'Referer': 'https://m.weibo.cn/search?containerid=231522type%3D1%26q%3D%23%E7%BE%8E%E5%9B%BD%E7%96%AB%E6%83%85%23',
    'User-Agent': user_agent
}


# 按页数抓取数据
def get_single_page(page):
    # 请求参数
    params = {
        'containerid': '231522type=1&q=#{}#'.format(topic_target),
        'page_type': 'searchall',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('抓取错误', e.args)


# 解析页面返回的json数据
global count
count = 0

# 长文本爬取代码段
def getLongText(lid):  # lid为长文本对应的id
    # 长文本请求头
    headers_longtext = {
        'Host': host,
        'Referer': 'https://m.weibo.cn/status/' + lid,
        'User-Agent': user_agent
    }
    params = {
        'id': lid
    }
    url = 'https://m.weibo.cn/statuses/extend?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers_longtext)
        if response.status_code == 200:  # 数据返回成功
            jsondata = response.json()
            tmp = jsondata.get('data')
            return pq(tmp.get("longTextContent")).text()  # 解析返回结构，获取长文本对应内容
    except requests.ConnectionError as e:
        print('抓取错误', e.args)


'''
修改后的页面爬取解析函数
'''
def parse_page(json):
    global count
    items = json.get('data').get('cards')
    for item in items:
        item = item.get('mblog')
        if item:
            if item.get('isLongText') is False:  # 不是长文本
                data = {
                    'id': item.get('id'),
                    'name': item.get('user').get('screen_name'),
                    'created': item.get('created_at'),
                    'text': pq(item.get("text")).text(),  # 仅提取内容中的文本
                    'attitudes': item.get('attitudes_count'),
                    'comments': item.get('comments_count'),
                    'reposts': item.get('reposts_count')
                }
            else:  # 长文本涉及文本的展开
                tmp = getLongText(item.get('id'))  # 调用函数
                data = {
                    'id': item.get('id'),
                    'name': item.get('user').get('screen_name'),
                    'created': item.get('created_at'),
                    'text': tmp,  # 仅提取内容中的文本
                    'attitudes': item.get('attitudes_count'),
                    'comments': item.get('comments_count'),
                    'reposts': item.get('reposts_count')
                }

            yield data
            count += 1
if __name__ == '__main__':
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个表格
    worksheet = workbook.add_sheet('话题')

    for page in range(1, end):  # 瀑布流下拉式，加载200次
        json = get_single_page(page)
        former = count
        results = parse_page(json)
        tmp_list = []
        print(count)
        # if count==former:
        #     print('terminated, gained {}'.format(count))
        #     break

        for result in results:  # 需要存入的字段
            worksheet.write(count, 0, label=result.get('name').strip('\n'))
            worksheet.write(count, 1, label=result.get('created').strip('\n'))
            worksheet.write(count, 2, label=result.get('text').strip('\n'))
            worksheet.write(count, 3, label=result.get('comments'))
            worksheet.write(count, 4, label=result.get('reposts'))
            worksheet.write(count, 5, label=result.get('attitudes'))


        time.sleep(1)  # 爬取时间间隔
        workbook.save('weibo_topic.xls')