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
        params.load_parents_request_params('iep.json')
        cls.params_dict = params

    """iep计划列表"""
    def test_iep_queryIepPlanList_success(self):
        params = self.params_dict.__getitem__('test_iep_queryIepPlanList_success')
        # 删除参数中的evaluateid
        evaluateid = params['evaluateid']
        # url路径上带有参数,在这里进行拼装
        params.pop('evaluateid')
        r =  hello_parents_get(const.parents_iep_queryIepPlanList+"/"+evaluateid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_iep_queryIepPlanList_success error")

    """iep内容分页列表"""
    def test_iep_queryIepTempList_success(self):
        params = self.params_dict.__getitem__('test_iep_queryIepTempList_success')
        # 删除参数中的ieptempid
        ieptempid = params['ieptempid']
        # url路径上带有参数,在这里进行拼装
        params.pop('ieptempid')
        r =  hello_parents_get(const.parents_iep_queryIepTempList+"/"+ieptempid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_iep_queryIepTempList_success error")

    @classmethod
    def tearDownClass(cls):
        pass