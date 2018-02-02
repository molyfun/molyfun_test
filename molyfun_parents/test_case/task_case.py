import unittest
from const import const
from request_common import hello_parents_post_url_params
from request_common import hello_parents_post_url_body
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
        params.load_parents_request_params('task.json')
        cls.params_dict = params

    """作业列表"""
    def test_task_list_success(self):
        params = self.params_dict.__getitem__('test_task_list_success')
        r =  hello_parents_get(const.parents_task_list, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_task_list_success error")

    """作业日期标识列表"""
    def test_task_taskDateIdentifyList_success(self):
        params = self.params_dict.__getitem__('test_task_taskDateIdentifyList_success')
        r =  hello_parents_get(const.parents_task_taskDateIdentifyList, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_task_taskDateIdentifyList_success error")

    """编辑作业"""
    def test_task_update_success(self):
        params = self.params_dict.__getitem__('test_task_update_success')
        r =  hello_parents_post(const.parents_task_update, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_task_update_success error")

    @classmethod
    def tearDownClass(cls):
        pass