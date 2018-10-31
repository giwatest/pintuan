from app import app

from app.goods import goods
#这里分别给app注册了蓝图goods
#参数url_prefix='/xxx'的意思是设置request.url中的url前缀，
#即当request.url是以/Home/Goods的情况下才会通过注册的蓝图的视图方法处理请求并返回
app.register_blueprint(goods, url_prefix='/Home/Goods')