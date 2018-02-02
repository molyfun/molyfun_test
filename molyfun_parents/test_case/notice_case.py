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
        params.load_parents_request_params('notice.json')
        cls.params_dict = params

    """通知详情"""
    def test_notice_info_success(self):
        params = self.params_dict.__getitem__('test_notice_info_success')
        # 删除参数中的id
        id = params['id']
        # url路径上带有参数,在这里进行拼装
        params.pop('id')
        r =  hello_parents_get(const.parents_notice_info+"/"+id, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_notice_info_success error")


    @classmethod
    def tearDownClass(cls):
        pass