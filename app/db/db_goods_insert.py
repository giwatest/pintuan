
import re
from flask import render_template, redirect,request
import json
from app import db
from app.models import Goods


# 打开文件，读取所有文件存成列表
with open("../../db_text/goods.txt", "r") as file:
    # 可以选择readline或者read的方式,但下面的代码要有所变化
    data_list = file.readlines()
    # 遍历列表
    for t in data_list:
        # 正则方式匹配处理字符串
        text_list = re.split(r'\n', t)
        text = re.split(r'\t', text_list[0])
        for t1 in text:
            print('*****')
            print('t1')
            print(t1)
            print('\n')
        #print(text_list)
        print('text')
        print(text)
        # sql语句
        #sql = "insert into test_db values (0,%s,%s,%s,%s,%s)"
        #print(sql)
        # 参数化方式传参
        #row_count = cur.execute(sql, [text[0], text[1], text[2], text[3], text[4]])
        # 显示操作结果
        #print("SQL语句影响的行数为%d" % row_count)

        newgoods = Goods(info_img=text[0], goods_name=text[1], group_person=text[2],goods_sale_num=text[3], goods_num=text[4], goods_now_price=text[5], goods_price=text[6], goods_low_price=text[7],goods_brief=text[8])
        db.session.add(newgoods)
        db.session.commit()
    goods = Goods().query.all()

    # for i in goods:
    #
    #     print(i)
        #print(i[0])

    #json.dumps(goods)
        #print(goods)
#统一提交
#conn.commit()
# 关闭游标　
#cur.close()
# 关闭连接
#conn.close()