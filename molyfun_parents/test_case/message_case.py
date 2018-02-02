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
        params.load_parents_request_params('message.json')
        cls.params_dict = params

    """批量删除消息"""
    def test_message_batchdel_success(self):
        params = self.params_dict.__getitem__('test_message_batchdel_success')
        r =  hello_parents_post(const.parents_message_batchdel, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_message_batchdel_success error")


    @classmethod
    def tearDownClass(cls):
        pass