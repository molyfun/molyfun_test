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
    '''课程模块测试'''

    @classmethod
    def setUpClass(cls):
        params = Params()
        params.load_parents_request_params('course.json')
        cls.params_dict = params

    """课程反馈添加"""
    def test_course_fackback_add(self):
        params = self.params_dict.__getitem__('test_course_fackback_add')
        r =  hello_parents_post(const.parents_course_fackbackadd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_course_fackback_add error")

    """课程日期标识列表"""
    def test_course_courseDateIdentifyList_success(self):
        params = self.params_dict.__getitem__('test_course_courseDateIdentifyList_success')
        r =  hello_parents_get(const.parents_course_courseDateIdentifyList, params)
        self.assertEqual(r.code,200,"test_course_courseDateIdentifyList_success error")

    """我的下载列表"""
    def test_course_courseUserList_success(self):
        params = self.params_dict.__getitem__('test_course_courseUserList_success')
        r =  hello_parents_get(const.parents_course_courseUserList, params)
        self.assertEqual(r.code,200,"test_course_courseUserList_success error")

    """课程列表"""
    def test_course_list_success(self):
        params = self.params_dict.__getitem__('test_course_list_success')
        r =  hello_parents_get(const.parents_course_list, params)
        self.assertEqual(r.code,200,"test_course_list_success error")

    """修改反馈"""
    def test_course_feedbackUpdate_success(self):
        params = self.params_dict.__getitem__('test_course_feedbackUpdate_success')
        r =  hello_parents_post(const.parents_course_feedbackUpdate, params)
        self.assertEqual(r.code,200,"test_course_feedbackUpdate_success error")

    """课程反馈列表"""
    def test_course_feedbacklist_success(self):
        params = self.params_dict.__getitem__('test_course_feedbacklist_success')
        #删除参数中的courseid
        courseid = params['courseid']
        # url路径上带有参数,在这里进行拼装
        params.pop('courseid')
        r = hello_parents_get(const.parents_course_feedbacklist+"/"+courseid, params)
        self.assertEqual(r.code, 200, "test_course_feedbacklist_success error")

    """课程详情"""
    def test_course_info_success(self):
        params = self.params_dict.__getitem__('test_course_info_success')
        #删除参数中的isdownload
        isdownload = params['isdownload']
        # url路径上带有参数,在这里进行拼装
        params.pop('isdownload')
        r = hello_parents_get(const.parents_course_info+"/"+isdownload, params)
        self.assertEqual(r.code,300,"test_course_info_success error")

    """课程总结"""
    def test_course_summary_success(self):
        params = self.params_dict.__getitem__('test_course_summary_success')
        r =  hello_parents_get(const.parents_course_summary, params)
        self.assertEqual(r.code,200,"test_course_summary_success error")

    """我的下载删除"""
    def test_course_courseRelCancel_success(self):
        params = self.params_dict.__getitem__('test_course_courseRelCancel_success')
        #删除参数中的relid
        relid = params['relid']
        # url路径上带有参数,在这里进行拼装
        params.pop('relid')
        r = hello_parents_get(const.parents_course_courseRelCancel+"/"+relid, params)
        self.assertEqual(r.code, 300, "test_course_courseRelCancel_success error")

    @classmethod
    def tearDownClass(cls):
        pass