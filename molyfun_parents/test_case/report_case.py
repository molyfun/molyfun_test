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
    '''报告模块测试'''

    @classmethod
    def setUpClass(cls):
        params = Params()
        params.load_parents_request_params('report.json')
        cls.params_dict = params

    """报告列表"""
    def test_report_list_success(self):
        params = self.params_dict.__getitem__('test_report_list_success')
        r =  hello_parents_get(const.parents_report_list, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_report_list_success error")

    """报告详情"""
    def test_report_info_success(self):
        params = self.params_dict.__getitem__('test_report_info_success')
        # 删除参数中的id
        id = params['id']
        # url路径上带有参数,在这里进行拼装
        params.pop('id')
        r =  hello_parents_get(const.parents_report_info+"/"+id, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_report_info_success error")

    """添加反馈"""
    def test_report_feedbackAdd_success(self):
        params = self.params_dict.__getitem__('test_report_feedbackAdd_success')
        # 删除参数中的reportid
        reportid = params['reportid']
        # url路径上带有参数,在这里进行拼装
        params.pop('reportid')
        r =  hello_parents_get(const.parents_report_feedbackAdd+"/"+reportid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_report_feedbackAdd_success error")

    """修改反馈"""
    def test_report_feedbackUpdate_success(self):
        params = self.params_dict.__getitem__('test_report_feedbackUpdate_success')
        # 删除参数中的id
        id = params['id']
        # url路径上带有参数,在这里进行拼装
        params.pop('id')
        r =  hello_parents_get(const.parents_report_feedbackUpdate+"/"+id, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_report_feedbackUpdate_success error")

    """报告反馈列表"""
    def test_report_feedbacklist_success(self):
        params = self.params_dict.__getitem__('test_report_feedbacklist_success')
        # 删除参数中的reportid
        reportid = params['reportid']
        # url路径上带有参数,在这里进行拼装
        params.pop('reportid')
        r =  hello_parents_get(const.parents_report_feedbacklist+"/"+reportid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_report_feedbacklist_success error")

    """结果和日期接口（适用于折线图）"""
    def test_report_resultAndDate_success(self):
        params = self.params_dict.__getitem__('test_report_resultAndDate_success')
        r =  hello_parents_get(const.parents_report_resultAndDate, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_report_resultAndDate_success error")

    """报告统计接口（适用于饼柱图）"""
    def test_report_statistic_success(self):
        params = self.params_dict.__getitem__('test_report_statistic_success')
        # 删除参数中的reportid
        reportid = params['reportid']
        # url路径上带有参数,在这里进行拼装
        params.pop('reportid')
        r =  hello_parents_get(const.parents_report_statistic+"/"+reportid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_report_statistic_success error")

    """课程目标和课程名称接口（适用于折线图）"""
    def test_report_targetAndCourseList_success(self):
        params = self.params_dict.__getitem__('test_report_targetAndCourseList_success')
        # 删除参数中的reportid
        reportid = params['reportid']
        # url路径上带有参数,在这里进行拼装
        params.pop('reportid')
        r =  hello_parents_get(const.parents_report_targetAndCourseList+"/"+reportid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_report_targetAndCourseList_success error")

    @classmethod
    def tearDownClass(cls):
        pass