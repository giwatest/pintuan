from flask import Blueprint, render_template, redirect,request
from app import db
from app.models import User
import json

user = Blueprint('user',__name__)



@user.route('/getUserInfo',methods=['POST'])
def getUserInfo():


    if request.method == 'POST':
        p_uid = request.form.get('uid', None)
        print(p_uid)

        if not p_uid:
            return json.dumps({'ERRORCODE':'0003'})#输入有误

        #goods = Goods().query.get(goods_id=p_id)
        user = db.session.query(User).filter_by(uid=p_uid)
        print(type(user))

        msgs = []
        for msg in user:
            msgs.append(msg)

        if len(msgs)<1:
            return json.dumps({'ERRORCODE':'0004'})#用户不存在




        return json.dumps({'ERRORCODE':'0001','uid':msgs[0].uid, 'nickname':msgs[0].nick_name, 'images':msgs[0].avatarUrl},)

    return ''


