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
        params.load_parents_request_params('gallery.json')
        cls.params_dict = params

    """素材分类属性列表"""
    def test_gallery_attrlist_success(self):
        params = self.params_dict.__getitem__('test_gallery_attrlist_success')
        r =  hello_parents_get(const.parents_gallery_attrlist, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_gallery_attrlist_success error")

    """素材列表"""
    def test_gallery_list_success(self):
        params = self.params_dict.__getitem__('test_gallery_list_success')
        r =  hello_parents_post(const.parents_gallery_list, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_gallery_list_success error")

    @classmethod
    def tearDownClass(cls):
        pass