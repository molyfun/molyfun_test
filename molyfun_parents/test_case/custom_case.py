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
        params.load_parents_request_params('custom.json')
        cls.params_dict = params

    """咨询定制列表"""
    def test_custom_planlist_success(self):
        params = self.params_dict.__getitem__('test_custom_planlist_success')
        r =  hello_parents_get(const.parents_custom_planlist, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_custom_planlist_success error")

    """咨询定制创建"""
    def test_custom_customplanCreate_success(self):
        params = self.params_dict.__getitem__('test_custom_customplanCreate_success')
        r =  hello_parents_post(const.parents_custom_customplanCreate, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_custom_customplanCreate_success error")

    """咨询定制资料数量"""
    def test_custom_docNum_success(self):
        params = self.params_dict.__getitem__('test_custom_docNum_success')
        # 删除参数中的customplanid
        customplanid = params['customplanid']
        # url路径上带有参数,在这里进行拼装
        params.pop('customplanid')
        r =  hello_parents_get(const.parents_custom_docNum+"/"+customplanid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_custom_docNum_success error")

    """添加消息"""
    def test_custom_msgAdd_success(self):
        params = self.params_dict.__getitem__('test_custom_msgAdd_success')
        r =  hello_parents_post_url_params(const.parents_custom_msgAdd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_custom_msgAdd_success error")

    """消息列表"""
    def test_custom_msgList_success(self):
        params = self.params_dict.__getitem__('test_custom_msgList_success')
        # 删除参数中的customplanid
        customplanid = params['customplanid']
        # url路径上带有参数,在这里进行拼装
        params.pop('customplanid')
        r =  hello_parents_get(const.parents_custom_msgList+"/"+customplanid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_custom_msgList_success error")

    """咨询定制评价"""
    def test_custom_eval_success(self):
        params = self.params_dict.__getitem__('test_custom_eval_success')
        # 删除参数中的customplanid
        customplanid = params['customplanid']
        # url路径上带有参数,在这里进行拼装
        params.pop('customplanid')
        r =  hello_parents_post_url_params(const.parents_custom_eval+"/"+customplanid, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_custom_eval_success error")

    """咨询定制资料列表"""
    def test_custom_doclist_success(self):
        params = self.params_dict.__getitem__('test_custom_doclist_success')
        # 删除参数中的customplanid
        customplanid = params['customplanid']
        # url路径上带有参数,在这里进行拼装
        params.pop('customplanid')
        r =  hello_parents_get(const.parents_custom_doclist+"/"+customplanid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_custom_doclist_success error")

    """修改咨询定制资料"""
    def test_custom_docUpdate_success(self):
        params = self.params_dict.__getitem__('test_custom_docUpdate_success')
        r =  hello_parents_post(const.parents_custom_docUpdate, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_custom_docUpdate_success error")

    @classmethod
    def tearDownClass(cls):
        pass