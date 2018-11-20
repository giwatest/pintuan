from flask import Blueprint, render_template, redirect,request
from app import db
from app.models import User
import requests
import config
import json

login = Blueprint('login',__name__)




@login.route('/getUid',methods=['POST'])
def getUid():



    p_openId = request.form.get('openId', None)


    if not p_openId:
        return json.dumps({'ERRORCODE':'0003'})#输入有误

    # if p_openId.strip()=='':
    #     return json.dumps({'ERRORCODE': '0002'})  #输入不能为空


    #goods = Goods().query.get(goods_id=p_id)
    user = db.session.query(User).filter_by(openid=p_openId)
    print(type(user))

    msgs = []
    for msg in user:
        msgs.append(msg)

    if len(msgs)<1:
        return json.dumps({'ERRORCODE':'0004'})#用户不存在



    return json.dumps({'uid':msgs[0].uid,'ERRORCODE':'0001'})#登录成功






@login.route('/regSmallUser',methods=['POST'])
def regSmallUser():


    if request.method == 'POST':
        p_code = request.form.get('code', None)
        p_nick_name = request.form.get('nick_name', None)
        p_avatarUrl = request.form.get('avatarUrl', None)
        p_gender = request.form.get('gender', None)
        p_city = request.form.get('city', None)



        if not p_code or not p_nick_name :
            return 'input error'

        form = {"appid": config.APPID, "secret": config.APPSECRET, "js_code": p_code, "grant_type": "authorization_code"}
        r = requests.post(config.GET_OPENID_URL, data=form)

        r_json = r.json()
        r_openid = r_json['openid']
        r_session_key = r_json['session_key']
        #往db插入一条新user数据
        newobj = User(openid=r_openid, nick_name=p_nick_name, avatarUrl=p_avatarUrl, gender=p_gender, city=p_city )
        db.session.add(newobj)
        db.session.commit()

        #goods = Goods().query.get(goods_id=r_openid)
        user = db.session.query(User).filter_by(openid=r_openid)

        msgs = []
        for msg in user:
            msgs.append(msg)


        uid = msgs[0].uid

        r_json = json.dumps({'uid': msgs[0].uid, 'openid': msgs[0].openid, 'secretkey': r_session_key})

        return r_json

    return ''


