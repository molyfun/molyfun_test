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
        params.load_parents_request_params('depart.json')
        cls.params_dict = params

    """投票列表"""
    def test_depart_votelist_success(self):
        params = self.params_dict.__getitem__('test_depart_votelist_success')
        r =  hello_parents_get(const.parents_depart_votelist, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_depart_votelist_success error")

    """机构申请"""
    def test_depart_validation_success(self):
        params = self.params_dict.__getitem__('test_depart_validation_success')
        r =  hello_parents_post_url_params(const.parents_depart_validation, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_depart_validation_success error")

    """添加机构评论"""
    def test_depart_adddepartcomment_success(self):
        params = self.params_dict.__getitem__('test_depart_adddepartcomment_success')
        r =  hello_parents_post_url_params(const.parents_depart_adddepartcomment, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_depart_adddepartcomment_success error")

    """切换机构"""
    def test_depart_changedepartfull_success(self):
        params = self.params_dict.__getitem__('test_depart_changedepartfull_success')
        r =  hello_parents_get(const.parents_depart_changedepartfull, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_depart_changedepartfull_success error")

    """学生机构列表"""
    def test_depart_list_success(self):
        params = self.params_dict.__getitem__('test_depart_list_success')
        r =  hello_parents_get(const.parents_depart_list, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_depart_list_success error")

    @classmethod
    def tearDownClass(cls):
        pass