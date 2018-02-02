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
        params.load_parents_request_params('training.json')
        cls.params_dict = params

    """个训列表"""
    def test_training_list_success(self):
        params = self.params_dict.__getitem__('test_training_list_success')
        r =  hello_parents_get(const.parents_training_list, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_training_list_success error")

    """个训详情"""
    def test_training_info_success(self):
        params = self.params_dict.__getitem__('test_training_info_success')
        # 删除参数中的id
        id = params['id']
        # url路径上带有参数,在这里进行拼装
        params.pop('id')
        r =  hello_parents_get(const.parents_training_info+"/"+id, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_training_info_success error")

    """个训反馈列表"""
    def test_training_feedbackList(self):
        params = self.params_dict.__getitem__('test_training_feedbackList')
        # 删除参数中的trainingid
        trainingid = params['trainingid']
        # url路径上带有参数,在这里进行拼装
        params.pop('trainingid')
        r =  hello_parents_get(const.parents_training_feedbackList+"/"+trainingid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_training_feedbackList error")

    """个训目标"""
    def test_training_targetinfo_success(self):
        params = self.params_dict.__getitem__('test_training_targetinfo_success')
        r =  hello_parents_get(const.parents_training_targetinfo, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_training_targetinfo_success error")

    @classmethod
    def tearDownClass(cls):
        pass