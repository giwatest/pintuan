import unittest
import requests

class goods_test(unittest.TestCase):

    # def test_add(self):
    #     url = "http://localhost:5000/Home/Goods/getGoods"
    #     form = {"username":"bbbb","email":"12345@qq.com","password":"12345"}
    #     r = requests.post(url,data = form)
    #     return r

    def test_getGoods(self):
        url = "http://localhost:5000/Home/Goods/getGoods"
        r = requests.get(url)

        return r