from app import db #db是在app/__init__.py生成的关联后的SQLAlchemy实例

class Goods(db.Model):
    __tablename__ = 'goods'
    goods_id = db.Column(db.Integer, primary_key=True)  #商品id
    info_img = db.Column(db.String(320), unique=False)  #商品图片url
    goods_name = db.Column(db.String(320), unique=False)   #商品名称
    group_person = db.Column(db.Integer, nullable=False)  #商品成团人数
    goods_sale_num = db.Column(db.Integer, nullable=False)  #商品已售数量
    goods_num = db.Column(db.Integer, nullable=False)  # 商品库存数量
    goods_now_price = db.Column(db.Float, nullable=False) #商品现价
    goods_price = db.Column(db.Float, nullable=False)  # 商品原价
    goods_low_price = db.Column(db.Float, nullable=False)  # 商品拼团底价
    goods_brief = db.Column(db.Text, nullable=False) #商品详情图

    def __repr__(self):

        return self


    def __str__(self):  # 定义打印对象时打印的字符串
        return " ".join(str(item) for item in (
            self.goods_id, self.info_img, self.goods_name, self.group_person, self.goods_sale_num,self.goods_num,self.goods_now_price,self.goods_price,self.goods_low_price))

