"""家长版用户模块-登录"""

import unittest
from const import const
from request_common import hello_parents_post_url_params
from request_common import hello_parents_post
from request_common import hello_parents_get

from time import sleep

import random
from request_params import Params
from utils.idcard_util import gen_id_card_random

class user(unittest.TestCase):
    '''用户模块测试'''

    @classmethod
    def setUpClass(cls):
        params = Params()
        params.load_parents_request_params('user.json')
        cls.params_dict = params

    """方法名中加入字母a 保证执行顺序"""
    def test_a_login_pawd_null(self):
        '''密码为空登录'''
        params = self.params_dict.__getitem__('test_a_login_pawd_null')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        #程序睡眠500毫秒，否则请求同一个结果过快服务器会做验证，返回207错误
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    """密码为null登录"""
    def test_a_login_pawd_null_01(self):
        params = self.params_dict.__getitem__('test_a_login_pawd_null_01')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        #程序睡眠500毫秒，否则请求同一个结果过快服务器会做验证，返回207错误
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    """容错1：用户名前包含空格"""
    def test_a_login_error_phone_01(self):
        params = self.params_dict.__getitem__('test_a_login_error_phone_01')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_login_success error")

    """容错2：用户名后包含空格"""
    def test_a_login_error_phone_02(self):
        params = self.params_dict.__getitem__('test_a_login_error_phone_02')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_login_success error")

    """容错3：用户名中包含空格"""
    def test_a_login_error_phone_03(self):
        params = self.params_dict.__getitem__('test_a_login_error_phone_03')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    """容错4：用户名前包含特殊符号%"""
    def test_a_login_error_phone_04(self):
        params = self.params_dict.__getitem__('test_a_login_error_phone_04')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    # """容错5：用户名后包含特殊符号%"""
    # def test_a_login_error_phone_05(self):
    #     params = self.params_dict.__getitem__('test_a_login_error_phone_05')
    #     r =  hello_parents_post_url_params(const.parents_user_login, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,300,"test_login_success error")

    """容错6：用户名中包含特殊符号%"""
    def test_a_login_error_phone_06(self):
        params = self.params_dict.__getitem__('test_a_login_error_phone_06')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    """容错7：密码前包含空格"""
    def test_a_login_error_password_01(self):
        params = self.params_dict.__getitem__('test_a_login_error_password_01')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    """容错8：密码后包含空格"""
    def test_a_login_error_password_02(self):
        params = self.params_dict.__getitem__('test_a_login_error_password_02')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    """容错9：密码中包含空格"""
    def test_a_login_error_password_03(self):
        params = self.params_dict.__getitem__('test_a_login_error_password_03')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    """容错10：密码前包含特殊符号%"""
    def test_a_login_error_password_04(self):
        params = self.params_dict.__getitem__('test_a_login_error_password_04')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    # """容错11：密码后包含特殊符号%"""
    # def test_a_login_error_password_05(self):
    #     params = self.params_dict.__getitem__('test_a_login_error_password_05')
    #     r =  hello_parents_post_url_params(const.parents_user_login, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,300,"test_login_success error")

    """容错12：密码中包含特殊符号%"""
    def test_a_login_error_password_06(self):
        params = self.params_dict.__getitem__('test_a_login_error_password_06')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    """容错14：密码中小写大写复合"""
    def test_a_login_error_password_08(self):
        params = self.params_dict.__getitem__('test_a_login_error_password_08')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_login_success error")

    """用户名密码正确"""
    def test_a_login_success(self):
        params = self.params_dict.__getitem__('test_a_login_success')
        r =  hello_parents_post_url_params(const.parents_user_login, params)
        if(r.code == 200):
            user_dict = r.data
            #取出返回的token
            token = user_dict['token']
            #先清理一下token的全局变量
            const.__delattr__('token')
            #将token添加到全局变量中 其它请求都会用到token
            const.__setattr__('token',token)
        self.assertEqual(r.code,200,"test_a_login_success error")

    # """用户名登出"""
    # def test_user_logout(self):
    #     params = self.params_dict.__getitem__('test_user_logout')
    #     r =  hello_parents_post_url_params(const.parents_user_logout, params)
    #     self.assertEqual(r.code,200,"test_user_logout error")
    #
    # """用户名密码正确"""
    # def test_a_login_success(self):
    #     params = self.params_dict.__getitem__('test_a_login_success')
    #     r =  hello_parents_post_url_params(const.parents_user_login, params)
    #     if(r.code == 200):
    #         user_dict = r.data
    #         #取出返回的token
    #         token = user_dict['token']
    #         #先清理一下token的全局变量
    #         const.__delattr__('token')
    #         #将token添加到全局变量中 其它请求都会用到token
    #         const.__setattr__('token',token)
    #     self.assertEqual(r.code,200,"test_a_login_success error")

    """用户信息"""
    def test_user_info(self):
        params = self.params_dict.__getitem__('test_user_info')
        r =  hello_parents_get(const.parents_user_info, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_info error")

    """关于我们"""
    def test_user_about(self):
        params = self.params_dict.__getitem__('test_user_about')
        r =  hello_parents_post_url_params(const.parents_user_about, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_about error")

    """验证码参数type为reg"""
    def test_user_captcha_reg(self):
        params = self.params_dict.__getitem__('test_user_captcha_reg')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_captcha_reg error")

    """验证码参数type为recoverpass"""
    def test_user_captcha_recoverpass(self):
        params = self.params_dict.__getitem__('test_user_captcha_recoverpass')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_captcha_recoverpass error")

    """容错1：验证码参数type-recoverpass大写"""
    def test_user_captcha_recoverpass_error_01(self):
        params = self.params_dict.__getitem__('test_user_captcha_recoverpass_error_01')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_captcha_recoverpass error")

    """容错2：验证码参数type-recoverpass大小写"""
    def test_user_captcha_recoverpass_error_02(self):
        params = self.params_dict.__getitem__('test_user_captcha_recoverpass_error_02')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_captcha_recoverpass error")

    """容错3：验证码参数type为空"""
    def test_user_captcha_recoverpass_error_03(self):
        params = self.params_dict.__getitem__('test_user_captcha_recoverpass_error_03')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_captcha_recoverpass error")

    """容错4：验证码参数type为空格"""
    def test_user_captcha_recoverpass_error_04(self):
        params = self.params_dict.__getitem__('test_user_captcha_recoverpass_error_04')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_captcha_recoverpass error")

    """容错5：验证码参数type为null"""
    def test_user_captcha_recoverpass_error_05(self):
        params = self.params_dict.__getitem__('test_user_captcha_recoverpass_error_05')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_captcha_recoverpass error")

    """容错6：验证码参数type为特殊字符%"""
    def test_user_captcha_recoverpass_error_06(self):
        params = self.params_dict.__getitem__('test_user_captcha_recoverpass_error_06')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_captcha_recoverpass error")

    """验证码change"""
    def test_user_captcha_change(self):
        params = self.params_dict.__getitem__('test_user_captcha_change')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_captcha_change error")

    """验证码regthirdparty"""
    def test_user_captcha_regthirdparty(self):
        params = self.params_dict.__getitem__('test_user_captcha_regthirdparty')
        phone = params['phone']
        #删除参数中的phone
        params.pop('phone')
        #url路径上带有参数,在这里进行拼装
        r =  hello_parents_get(const.parents_user_captcha+"/"+phone, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_captcha_regthirdparty error")

    """我的消息列表"""
    def test_user_messageList_success(self):
        params = self.params_dict.__getitem__('test_user_messageList_success')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_messageList_success error")

    """容错1：我的消息列表pageNum为空"""
    def test_user_messageList_error_01(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_01')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错2：我的消息列表pageNum为null"""
    def test_user_messageList_error_02(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_02')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错3：我的消息列表pageNum为1.0"""
    def test_user_messageList_error_03(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_03')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    # """容错4：我的消息列表pageNum为0"""
    # def test_user_messageList_error_04(self):
    #     params = self.params_dict.__getitem__('test_user_messageList_error_04')
    #     r =  hello_parents_get(const.parents_user_messageList, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,300,"test_user_messageList_success error")

    # """容错5：我的消息列表pageNum为负数-1"""
    # def test_user_messageList_error_05(self):
    #     params = self.params_dict.__getitem__('test_user_messageList_error_05')
    #     r =  hello_parents_get(const.parents_user_messageList, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错6：我的消息列表pageNum的maxvalue为4294967296"""
    def test_user_messageList_error_06(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_06')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

        """容错7：我的消息列表pageNum的minvalue为-4294967296"""
    def test_user_messageList_error_07(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_07')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错8：我的消息列表pageNum为空格"""
    def test_user_messageList_error_08(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_08')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错9：我的消息列表pageNume前包含空格"""
    def test_user_messageList_error_09(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_09')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错10：我的消息列表pageNum后包含空格"""
    def test_user_messageList_error_10(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_10')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错11：我的消息列表pageNum前包含特殊字符%"""
    def test_user_messageList_error_11(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_11')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错12：我的消息列表pageNum后包含特殊字符%"""
    def test_user_messageList_error_12(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_12')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错13：我的消息列表pageSize为小数10.0"""
    def test_user_messageList_error_13(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_13')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错14：我的消息列表pageSize为空"""
    def test_user_messageList_error_14(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_14')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错15：我的消息列表pageSize为null"""
    def test_user_messageList_error_15(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_15')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错16：我的消息列表pageSize为空格"""
    def test_user_messageList_error_16(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_16')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错17：我的消息列表pageSize为100"""
    def test_user_messageList_error_17(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_17')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_messageList_success error")

    """容错18：我的消息列表pageSize的maxvalue为4294967296"""
    def test_user_messageList_error_18(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_18')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错19：我的消息列表pageSize的minvalue为-4294967296"""
    def test_user_messageList_error_19(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_19')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错20：我的消息列表pageSize为0"""
    def test_user_messageList_error_20(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_20')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_messageList_success error")

    """容错21：我的消息列表pageSize前包含空格"""
    def test_user_messageList_error_21(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_21')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错22：我的消息列表pageSize后包含空格"""
    def test_user_messageList_error_22(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_22')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错23：我的消息列表pageSize中包含空格"""
    def test_user_messageList_error_23(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_23')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错24：我的消息列表pageSize前包含特殊字符%"""
    def test_user_messageList_error_24(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_24')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错25：我的消息列表pageSize后包含特殊字符%"""
    def test_user_messageList_error_25(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_25')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错26：我的消息列表pageSize中包含特殊字符%"""
    def test_user_messageList_error_26(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_26')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错27：我的消息列表pageNum、pageSize为空"""
    def test_user_messageList_error_27(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_27')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错28：我的消息列表pageNum为空，pageSize为null"""
    def test_user_messageList_error_28(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_28')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错29：我的消息列表pageNum、pageSize为null"""
    def test_user_messageList_error_29(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_29')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """容错30：我的消息列表pageNum为null、pageSize为空"""
    def test_user_messageList_error_30(self):
        params = self.params_dict.__getitem__('test_user_messageList_error_30')
        r =  hello_parents_get(const.parents_user_messageList, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_user_messageList_success error")

    """修改密码"""
    def test_user_updatePassword(self):
        params = self.params_dict.__getitem__('test_user_updatePassword')
        r =  hello_parents_post_url_params(const.parents_user_updatePassword, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_updatePassword error")

    """建议反馈-content输入转义字符"""
    def test_user_feedbackAdd(self):
        params = self.params_dict.__getitem__('test_user_feedbackAdd')
        r =  hello_parents_post_url_params(const.parents_user_feedbackAdd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_feedbackAdd error")

    """建议反馈-content输入汉字"""
    def test_user_feedbackAdd_error_01(self):
        params = self.params_dict.__getitem__('test_user_feedbackAdd_error_01')
        r =  hello_parents_post_url_params(const.parents_user_feedbackAdd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_feedbackAdd error")

    """建议反馈-content输入字母"""
    def test_user_feedbackAdd_error_02(self):
        params = self.params_dict.__getitem__('test_user_feedbackAdd_error_02')
        r =  hello_parents_post_url_params(const.parents_user_feedbackAdd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_feedbackAdd error")

    """建议反馈-content输入数字"""
    def test_user_feedbackAdd_error_03(self):
        params = self.params_dict.__getitem__('test_user_feedbackAdd_error_03')
        r =  hello_parents_post_url_params(const.parents_user_feedbackAdd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_feedbackAdd error")

    """建议反馈-content为空"""
    def test_user_feedbackAdd_error_04(self):
        params = self.params_dict.__getitem__('test_user_feedbackAdd_error_04')
        r =  hello_parents_post_url_params(const.parents_user_feedbackAdd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_feedbackAdd error")

    """建议反馈-content为null"""
    def test_user_feedbackAdd_error_05(self):
        params = self.params_dict.__getitem__('test_user_feedbackAdd_error_05')
        r =  hello_parents_post_url_params(const.parents_user_feedbackAdd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_feedbackAdd error")

    """版本检查-versionnum=v0.0.0"""
    def test_user_checkVersion(self):
        params = self.params_dict.__getitem__('test_user_checkVersion')
        r =  hello_parents_post_url_params(const.parents_user_checkVersion, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_checkVersion error")

    """容错1：版本检查-versionnum为空"""
    def test_user_checkVersion_error_01(self):
        params = self.params_dict.__getitem__('test_user_checkVersion_error_01')
        r =  hello_parents_post_url_params(const.parents_user_checkVersion, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_checkVersion error")
    #
    # """容错2：版本检查-versionnum为null"""
    # def test_user_checkVersion_error_02(self):
    #     params = self.params_dict.__getitem__('test_user_checkVersion_error_02')
    #     r =  hello_parents_post_url_params(const.parents_user_checkVersion, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,200,"test_user_checkVersion error")

    """容错3：版本检查-versionnum=V0.0.0"""
    def test_user_checkVersion_error_03(self):
        params = self.params_dict.__getitem__('test_user_checkVersion_error_03')
        r =  hello_parents_post_url_params(const.parents_user_checkVersion, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_checkVersion error")

    # """容错4：版本检查-versionnum为空格"""
    # def test_user_checkVersion_error_04(self):
    #     params = self.params_dict.__getitem__('test_user_checkVersion_error_04')
    #     r =  hello_parents_post_url_params(const.parents_user_checkVersion, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,200,"test_user_checkVersion error")

    """学生信息"""
    def test_user_studentInfo(self):
        params = self.params_dict.__getitem__('test_user_studentInfo')
        r =  hello_parents_get(const.parents_user_studentInfo, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_studentInfo error")

    """修改学生信息"""
    def test_user_updateStudentInfoFull(self):
        params = self.params_dict.__getitem__('test_user_updateStudentInfoFull')
        r =  hello_parents_post(const.parents_user_updateStudentInfoFull, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_updateStudentInfoFull error")

    """修改用户信息"""
    def test_user_updateInfo(self):
        params = self.params_dict.__getitem__('test_user_updateInfo')
        r =  hello_parents_post_url_params(const.parents_user_updateInfo, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_updateInfo error")

    """更新邮箱-转义"""
    def test_user_updateemail_zy(self):
        params = self.params_dict.__getitem__('test_user_updateemail_zy')
        r =  hello_parents_post_url_params(const.parents_user_updateemail, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_updateemail_zy error")

    """更新邮箱"""
    def test_user_updateemail(self):
        params = self.params_dict.__getitem__('test_user_updateemail')
        r =  hello_parents_post_url_params(const.parents_user_updateemail, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_updateemail error")

    """容错1：更新邮箱"""
    def test_user_updateemail(self):
        params = self.params_dict.__getitem__('test_user_updateemail')
        r =  hello_parents_post_url_params(const.parents_user_updateemail, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_user_updateemail error")

    @classmethod
    def tearDownClass(cls):
        pass
