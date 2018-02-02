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
        params.load_parents_request_params('mission.json')
        cls.params_dict = params

    """每日签到"""
    def test_mission_dailySign_success(self):
        params = self.params_dict.__getitem__('test_mission_dailySign_success')
        r =  hello_parents_post_url_params(const.parents_mission_dailySign, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_mission_dailySign_success error")

    """任务类型列表"""
    def test_mission_typeList_success(self):
        params = self.params_dict.__getitem__('test_mission_typeList_success')
        r =  hello_parents_get(const.parents_mission_typeList, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_mission_typeList_success error")

    """刷新日排行榜"""
    def test_mission_refreshCharts_success(self):
        params = self.params_dict.__getitem__('test_mission_refreshCharts_success')
        r =  hello_parents_post_url_params(const.parents_mission_refreshCharts, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_mission_refreshCharts_success error")

    """任务列表"""
    def test_mission_list_success(self):
        params = self.params_dict.__getitem__('test_mission_list_success')
        r =  hello_parents_get(const.parents_mission_list, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_mission_list_success error")

    @classmethod
    def tearDownClass(cls):
        pass