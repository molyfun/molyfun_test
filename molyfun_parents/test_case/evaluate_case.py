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
        params.load_parents_request_params('evaluate.json')
        cls.params_dict = params

    """评估列表"""
    def test_evaluate_list_success(self):
        params = self.params_dict.__getitem__('test_evaluate_list_success')
        r =  hello_parents_get(const.parents_evaluate_list, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_evaluate_list_success error")

    """评估分析结果列表"""
    def test_evaluate_analysisResultlist_success(self):
        params = self.params_dict.__getitem__('test_evaluate_analysisResultlist_success')
        # 删除参数中的evaluateid
        evaluateid = params['evaluateid']
        # url路径上带有参数,在这里进行拼装
        params.pop('evaluateid')
        r =  hello_parents_get(const.parents_evaluate_analysisResultlist+"/"+evaluateid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_evaluate_analysisResultlist_success error")

    """分析结果文件列表"""
    def test_evaluate_evaluateAnalysislist(self):
        params = self.params_dict.__getitem__('test_evaluate_evaluateAnalysislist')
        # 删除参数中的evaluateid
        evaluateid = params['evaluateid']
        # url路径上带有参数,在这里进行拼装
        params.pop('evaluateid')
        r =  hello_parents_get(const.parents_evaluate_evaluateAnalysislist+"/"+evaluateid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_evaluate_evaluateAnalysislist error")

    """分析结果列表"""
    def test_evaluate_evaluteProjectList_success(self):
        params = self.params_dict.__getitem__('test_evaluate_evaluteProjectList_success')
        # 删除参数中的evaluateid
        evaluateid = params['evaluateid']
        # url路径上带有参数,在这里进行拼装
        params.pop('evaluateid')
        r =  hello_parents_get(const.parents_evaluate_evaluteProjectList+"/"+evaluateid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_evaluate_evaluteProjectList_success error")

    @classmethod
    def tearDownClass(cls):
        pass