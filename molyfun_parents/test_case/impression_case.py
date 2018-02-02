import unittest
from const import const
from request_common import hello_parents_post_url_params
from request_common import hello_parents_get
from request_common import hello_parents_post
from time import sleep
import random

from request_params import Params
from utils.idcard_util import gen_id_card_random

class user(unittest.TestCase):
    '''作业模块测试'''

    @classmethod
    def setUpClass(cls):
        params = Params()
        params.load_parents_request_params('impression.json')
        cls.params_dict = params

    """添加记录"""
    def test_impression_add_success(self):
        params = self.params_dict.__getitem__('test_impression_add_success')
        r =  hello_parents_post_url_params(const.parents_impression_add, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_impression_add_success error")

    """删除记录"""
    def test_impression_delete_success(self):
        params = self.params_dict.__getitem__('test_impression_delete_success')
        # 删除参数中的impressionid
        impressionid = params['impressionid']
        # url路径上带有参数,在这里进行拼装
        params.pop('impressionid')
        r =  hello_parents_get(const.parents_impression_delete+"/"+impressionid, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_impression_delete_success error")

    @classmethod
    def tearDownClass(cls):
        pass