import requests

question_id=24279087
howmany=10
url = 'https://www.zhihu.com/api/v4/questions/{}/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics;data[*].settings.table_of_content.enabled&limit={}&offset=5&platform=desktop&sort_by=default'.format(question_id,howmany)
headers = {

    "Host": "www.zhihu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.zhihu.com/question/{}".format(question_id),
    "x-ab-param": "li_sp_mqbk=0;li_paid_answer_exp=0;tp_dingyue_video=0;qap_question_author=0;li_vip_verti_search=0;li_panswer_topic=0;pf_noti_entry_num=2;top_test_4_liguangyi=1;zr_slotpaidexp=1;tp_topic_style=0;li_edu_page=old;se_ffzx_jushen1=0;zr_expslotpaid=5;qap_question_visitor= 0;pf_adjust=1;tp_zrec=1;tp_contents=1",
    "x-ab-pb": "ClT0C0cAawGIAdIBBwxAAXQBtQs/ALcAxQAbADcMlguJDM8LNAzcC1gBaQG0CggAZwC8AewKTwGrAZsLQwC0AI0BVgzgC0wLAQvXC+QKagEPC2ALUgsSKgAAAAAAAQEAAwAAAAABAAALAAAAAgACAAIBAAACFQAAAQAAAAAAAQEAAQ==",
    "x-requested-with": "fetch",
    "x-zse-83": "3_2.0",
    "x-zse-86": "2.0_a_x0HDUBngtY6_S8mMYye6LBQTFpk_NqMMtBnU90QH2f",
    "Connection": "keep-alive",
    "Cookie": 'q_c1=d478e747111f4b46a6799f2fb4bf84f3|1615634053000|1513237619000; _zap=a82336fd-0a0b-4b9d-8d1f-0d8ae79efa59; _xsrf=ALjrh6c2KxhT7M3qCOySpHU36hncuLjJ; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1614955498,1615262446,1615630213,1615631801; d_c0="AADX7qvVxxGPTpPJP5pVE9j-F3Ej3QlYrKU=|1598248452"; _ga=GA1.2.781777098.1598248451; z_c0="2|1:0|10:1603251468|4:z_c0|92:Mi4xUV91bUF3QUFBQUFBQU5mdXE5WEhFU1lBQUFCZ0FsVk5EUHQ4WUFDTHBOQ2ROSktXUkZKSnlISDNpVEpqQnZWbUtR|42a4dc813cdb96d64d306ca0b85cb43eea450f5e2e6aee140399ba73e6ea2e48"; tst=r; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1615634903|1615630210; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1615634903; SESSIONID=Mm5yS4C1OQQ9EuuyQh4yCPk11PyduwxtK0GNhYunZ64; JOID=V1oTB0gwXblC0tg2OTG8KbF7DPArejSOPIfrcQp5C-x5kKtERIrO8CPT2zA8eOiQOuO89vY5GTPRJ32ZCMem_ZA=; osd=UlwQCkI1W7pP2N0wOjy2LLd4AfoufDeDNoLtcgdzDup6naFBQonD-ibV2D02fe6TN-m58PU0EzbXJHCTDcGl8Jo=',
    "TE": "Trailers",
}

response=requests.get(url,headers=headers)
print(response.text)
with open('zhihu.json','w',encoding='utf8') as f:
    f.write(response.text)