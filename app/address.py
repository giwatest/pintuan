from flask import Blueprint, render_template, redirect,request
from app import db
from app.models import Address
import json
from app.AlchemyJsonEncoder import AlchemyJsonEncoder
address = Blueprint('address',__name__)



@address.route('/saveAddress',methods=['POST'])
def saveAddress():


    if request.method == 'POST':
        p_uid = request.form.get('uid', None)
        p_consignee = request.form.get('consignee', None)
        p_tel = request.form.get('tel', None)
        p_province = request.form.get('province', None)
        p_city = request.form.get('city', None)
        p_district = request.form.get('district', None)
        p_address = request.form.get('address', None)



        if not p_uid or not p_consignee or not p_tel or not p_province or not p_city or not p_district or not p_address:
            return 'input error'

        newobj = Address(uid=p_uid, consignee=p_consignee, tel=p_tel, province=p_province, city=p_city, district=p_district, address=p_address)
        db.session.add(newobj)
        db.session.commit()

        address = db.session.query(Address).filter_by(uid=p_uid)


        msgs = []
        for msg in address:
            msgs.append(msg)

        jsonAddressList = json.dumps(msgs, cls=AlchemyJsonEncoder)

        return jsonAddressList
    return ''


@address.route('/getAddress',methods=['POST'])
def getAddress():


    if request.method == 'POST':
        p_uid = request.form.get('uid', None)


        print(p_uid)

        if not p_uid:
            return 'input error'

        newobj = Address(uid=p_uid)
        db.session.add(newobj)
        db.session.commit()

        address = db.session.query(Address).filter_by(uid=p_uid)


        msgs = []
        for msg in address:
            msgs.append(msg)

        jsonAddressList = json.dumps(msgs, cls=AlchemyJsonEncoder)

        return jsonAddressList
    return ''



