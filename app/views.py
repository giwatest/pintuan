from app import app

from app.goods import goods

from app.login import login

from app.user import user
from app.address import address
#这里分别给app注册了蓝图goods
#参数url_prefix='/xxx'的意思是设置request.url中的url前缀，
#即当request.url是以/Home/Goods的情况下才会通过注册的蓝图的视图方法处理请求并返回

#注册商品路径
app.register_blueprint(goods, url_prefix='/Home/Goods')
#注册用户信息路径
app.register_blueprint(user, url_prefix='/Home/User')


#注册用户登录路径
app.register_blueprint(login, url_prefix='/Home/Login')

#注册收货地址路径
app.register_blueprint(address, url_prefix='/Home/Address')