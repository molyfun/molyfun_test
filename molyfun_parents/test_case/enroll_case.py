import unittest
from const import const
from request_common import hello_parents_post_url_params
from request_common import hello_parents_post_url_body
from request_common import hello_parents_get
from request_common import hello_parents_post
from time import sleep
import random
import pymysql

# 打开数据库连接
db = pymysql.connect(
    host='192.168.3.30',
    port=3306,
    user='root',
    passwd='molyfun',
    db='hello_yilin',
    charset='utf8'
    )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

from request_params import Params
from utils.idcard_util import gen_id_card_random

class user(unittest.TestCase):
    '''课程模块测试'''

    @classmethod
    def setUpClass(cls):
        params = Params()
        params.load_parents_request_params('enroll.json')
        cls.params_dict = params

    """报名须知-departcode=A0001930"""
    def test_enroll_notice_success(self):
        params = self.params_dict.__getitem__('test_enroll_notice_success')
        r =  hello_parents_get(const.parents_enroll_notice, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_notice_success error")

    """容错1：报名须知-departcode大写转小写"""
    def test_enroll_notice_error_01(self):
        params = self.params_dict.__getitem__('test_enroll_notice_error_01')
        r =  hello_parents_get(const.parents_enroll_notice, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_notice_error_01 error")

    """容错2：报名须知-departcode为空"""
    def test_enroll_notice_error_02(self):
        params = self.params_dict.__getitem__('test_enroll_notice_error_02')
        r =  hello_parents_get(const.parents_enroll_notice, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_notice_error_02 error")

    """容错3：报名须知-departcode为null"""
    def test_enroll_notice_error_03(self):
        params = self.params_dict.__getitem__('test_enroll_notice_error_03')
        r =  hello_parents_get(const.parents_enroll_notice, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_notice_error_03 error")

    """容错4：报名须知-departcode前有空格"""
    def test_enroll_notice_error_04(self):
        params = self.params_dict.__getitem__('test_enroll_notice_error_04')
        r =  hello_parents_get(const.parents_enroll_notice, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_notice_error_04 error")

    """容错5：报名须知-departcode后有空格"""
    def test_enroll_notice_error_05(self):
        params = self.params_dict.__getitem__('test_enroll_notice_error_05')
        r =  hello_parents_get(const.parents_enroll_notice, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_notice_error_05 error")

    # """容错6：报名须知-departcode设定范围外"""
    # def test_enroll_notice_error_06(self):
    #     params = self.params_dict.__getitem__('test_enroll_notice_error_06')
    #     r =  hello_parents_get(const.parents_enroll_notice, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,300,"test_enroll_notice_error_06 error")

    """报名中列表"""
    def test_enroll_enrollinglist_success(self):
        params = self.params_dict.__getitem__('test_enroll_enrollinglist_success')
        r =  hello_parents_get(const.parents_enroll_enrollinglist, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_enrollinglist_success error")

    """报名详情"""
    def test_enroll_info_success(self):
        params = self.params_dict.__getitem__('test_enroll_info_success')
        # 删除参数中的id
        id = params['id']
        # url路径上带有参数,在这里进行拼装
        params.pop('id')
        r =  hello_parents_get(const.parents_enroll_info+"/"+id, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_info_success error")

    """容错1：报名详情-大小写字母"""
    def test_enroll_info_error_01(self):
        params = self.params_dict.__getitem__('test_enroll_info_error_01')
        # 删除参数中的id
        id = params['id']
        # url路径上带有参数,在这里进行拼装
        params.pop('id')
        r =  hello_parents_get(const.parents_enroll_info+"/"+id, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_info_error_01 error")

    # """容错2：报名详情-id为空"""
    # def test_enroll_info_error_02(self):
    #     params = self.params_dict.__getitem__('test_enroll_info_error_02')
    #     # 删除参数中的id
    #     id = params['id']
    #     # url路径上带有参数,在这里进行拼装
    #     params.pop('id')
    #     r =  hello_parents_get(const.parents_enroll_info+"/"+id, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,300,"test_enroll_info_error_02 error")
    #
    # """容错3：报名详情-id为null"""
    # def test_enroll_info_error_03(self):
    #     params = self.params_dict.__getitem__('test_enroll_info_error_03')
    #     # 删除参数中的id
    #     id = params['id']
    #     # url路径上带有参数,在这里进行拼装
    #     params.pop('id')
    #     r =  hello_parents_get(const.parents_enroll_info+"/"+id, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,300,"test_enroll_info_error_03 error")

    """容错4：报名详情-id前有空格"""
    def test_enroll_info_error_04(self):
        params = self.params_dict.__getitem__('test_enroll_info_error_04')
        # 删除参数中的id
        id = params['id']
        # url路径上带有参数,在这里进行拼装
        params.pop('id')
        r =  hello_parents_get(const.parents_enroll_info+"/"+id, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_info_error_04 error")

    """容错5：报名详情-id后有空格"""
    def test_enroll_info_error_05(self):
        params = self.params_dict.__getitem__('test_enroll_info_error_05')
        # 删除参数中的id
        id = params['id']
        # url路径上带有参数,在这里进行拼装
        params.pop('id')
        r =  hello_parents_get(const.parents_enroll_info+"/"+id, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_info_error_05 error")

    """报名信息提交"""
    def test_enroll_infosubmit_success(self):
        params = self.params_dict.__getitem__('test_enroll_infosubmit_success')
        departid = params['departid']
        params.pop('departid')
        r =  hello_parents_post(const.parents_enroll_infosubmit+"?departid="+departid, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_infosubmit_success error")

    """入学通知详情"""
    def test_enroll_entrancenotice_success(self):
        params = self.params_dict.__getitem__('test_enroll_entrancenotice_success')
        # 删除参数中的enrollstudnetid
        enrollstudnetid = params['enrollstudnetid']
        # url路径上带有参数,在这里进行拼装
        params.pop('enrollstudnetid')
        r =  hello_parents_get(const.parents_enroll_entrancenotice+"/"+enrollstudnetid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_entrancenotice_success error")

    """修改报名学生信息"""
    def test_enroll_infoupdate_success(self):
        params = self.params_dict.__getitem__('test_enroll_infoupdate_success')
        r =  hello_parents_post(const.parents_enroll_infoupdate, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_infoupdate_success error")

    """容错1：修改报名学生信息-id为空"""
    def test_enroll_infoupdate_error_01(self):
        params = self.params_dict.__getitem__('test_enroll_infoupdate_error_01')
        r =  hello_parents_post(const.parents_enroll_infoupdate, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_infoupdate_error_01 error")

    """容错2：修改报名学生信息-sex为空"""
    def test_enroll_infoupdate_error_02(self):
        params = self.params_dict.__getitem__('test_enroll_infoupdate_error_02')
        r =  hello_parents_post(const.parents_enroll_infoupdate, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_infoupdate_error_02 error")

    """容错3：修改报名学生信息-birthdatetime为空"""
    def test_enroll_infoupdate_error_03(self):
        params = self.params_dict.__getitem__('test_enroll_infoupdate_error_03')
        r =  hello_parents_post(const.parents_enroll_infoupdate, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_infoupdate_error_03 error")

    """容错4：修改报名学生信息-parity为空"""
    def test_enroll_infoupdate_error_04(self):
        params = self.params_dict.__getitem__('test_enroll_infoupdate_error_04')
        r =  hello_parents_post(const.parents_enroll_infoupdate, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_infoupdate_error_04 error")

    """容错5：修改报名学生信息-cardid为空"""
    def test_enroll_infoupdate_error_05(self):
        params = self.params_dict.__getitem__('test_enroll_infoupdate_error_05')
        r =  hello_parents_post(const.parents_enroll_infoupdate, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_infoupdate_error_05 error")

    """容错6：修改报名学生信息-address为空"""
    def test_enroll_infoupdate_error_06(self):
        params = self.params_dict.__getitem__('test_enroll_infoupdate_error_06')
        r =  hello_parents_post(const.parents_enroll_infoupdate, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_enroll_infoupdate_error_06 error")

    """修改联系人信息"""
    def test_enroll_contactupdate_success(self):
        params = self.params_dict.__getitem__('test_enroll_contactupdate_success')
        r =  hello_parents_post(const.parents_enroll_contactupdate, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_contactupdate_success error")

    """添加放弃原因"""
    def test_enroll_abandoncauseadd_success(self):
        params = self.params_dict.__getitem__('test_enroll_abandoncauseadd_success')
        r =  hello_parents_post_url_params(const.parents_enroll_abandoncauseadd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_abandoncauseadd_success error")

    """评测列表"""
    def test_enroll_evaluatelist_success(self):
        params = self.params_dict.__getitem__('test_enroll_evaluatelist_success')
        r =  hello_parents_get(const.parents_enroll_evaluatelist, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_evaluatelist_success error")

    """评测结果列表"""
    def test_enroll_evaluateresultlist_success(self):
        params = self.params_dict.__getitem__('test_enroll_evaluateresultlist_success')
        r =  hello_parents_get(const.parents_enroll_evaluateresultlist, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_evaluateresultlist_success error")

    """判断报名记录是否是放弃状态"""
    def test_enroll_judgestatus_success(self):
        params = self.params_dict.__getitem__('test_enroll_judgestatus_success')
        # 删除参数中的enrollstudnetid
        enrollstudnetid = params['enrollstudnetid']
        # url路径上带有参数,在这里进行拼装
        params.pop('enrollstudnetid')
        r =  hello_parents_get(const.parents_enroll_judgestatus+"/"+enrollstudnetid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_enroll_judgestatus_success error")

    @classmethod
    def tearDownClass(cls):
        pass








































