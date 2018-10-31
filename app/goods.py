from flask import Blueprint, render_template, redirect,request
from app import db
from app.models import Goods
import json
from app.AlchemyJsonEncoder import AlchemyJsonEncoder

from flask import jsonify
goods = Blueprint('goods',__name__)



@goods.route('/getGoods',methods=['GET','POST'])
def getGoods():
    goods = Goods().query.all()
    jsonGoods = json.dumps(goods, cls=AlchemyJsonEncoder)

    return jsonGoods

@goods.route('/OpenGroup',methods=['POST'])
def openGroup():


    if request.method == 'POST':
        p_id = request.form.get('goods_id', None)
        print(p_id)

        if not p_id:
            return 'input error'


        #goods = Goods().query.get(goods_id=p_id)
        goods = db.session.query(Goods).filter_by(goods_id=p_id)
        print(type(goods))

        msgs = []
        for msg in goods:
            msgs.append(msg)
        jsonGoods = json.dumps(msg, cls=AlchemyJsonEncoder)

        return jsonGoods

    return ''
