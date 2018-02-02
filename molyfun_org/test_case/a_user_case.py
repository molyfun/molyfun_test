import unittest
from const import const
from request_common import hello_org_post
from request_common import hello_org_get
import random
from request_params import Params
from utils.idcard_util import gen_id_card_random

class user(unittest.TestCase):
    '''用户模块测试'''

    @classmethod
    def setUpClass(cls):
        params = Params()
        params.load_org_request_params('user.json')
        cls.params_dict = params


    """方法名中加入字母a 保证执行顺序"""
    def test_a_login_pawd_null(self):
        '''密码为空登录'''
        params = self.params_dict.__getitem__('test_a_login_pawd_null')
        r =  hello_org_post(const.org_user_login, params)
        self.assertEqual(r.status,str(300),"test_login_success error")

    """方法名中加入字母a 保证执行顺序"""
    def test_a_login_success(self):
        """用户名,密码正确,登陆成功"""
        params = self.params_dict.__getitem__('test_a_login_success')
        r =  hello_org_post(const.org_user_login, params)
        if(r.status == str(200)):
            user_dict = r.data
            #取出返回的user_id
            user_id = user_dict['id']
            session_id = user_dict['sessionId']
            #先清理一下user_id的全局变量
            const.__delattr__('uid')
            const.__delattr__('session_id')
            #将userid添加到全局变量中 其它请求都会用到uid
            const.__setattr__('uid',user_id)
            const.__setattr__('session_id',session_id)
        self.assertEqual(r.status, str(200), "test_login_success error")

    def test_user_function(self):
        """ 菜单权限列表"""
        params = {}
        r = hello_org_get(const.org_user_function, params)
        self.assertEqual(r.status, str(200), "test_user_function error")

    def test_user_add(self):
        """ 老师录入"""
        user_name =  ''
        #随机生成名字 不能够同名
        for i in range(5):
            user_name += chr(random.randint(97, 122))
        idcard_number = gen_id_card_random()
        params = self.params_dict.__getitem__('test_user_add')
        params['cardId'] = idcard_number
        params['userName'] = user_name
        r = hello_org_post(const.org_user_add, params)
        self.assertEqual(r.status, str(200), "test_user_add error")

    def test_user_listbyorg(self):
        """ 老师列表"""
        params = self.params_dict.__getitem__('test_user_listbyorg')
        r = hello_org_get(const.org_user_listbyorg, params)
        self.assertEqual(r.status, str(200), "test_user_listbyorg error")

    @classmethod
    def tearDownClass(cls):
        pass
