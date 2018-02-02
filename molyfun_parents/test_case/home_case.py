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
        params.load_parents_request_params('home.json')
        cls.params_dict = params

    """添加文章"""
    def test_home_addArticle_success(self):
        params = self.params_dict.__getitem__('test_home_addArticle_success')
        r =  hello_parents_post(const.parents_home_addArticle, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_home_addArticle_success error")

    """文章列表"""
    def test_home_articleList_success(self):
        params = self.params_dict.__getitem__('test_home_articleList_success')
        r =  hello_parents_get(const.parents_home_articleList, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_home_articleList_success error")

    """话题列表"""
    def test_home_topicList_success(self):
        params = self.params_dict.__getitem__('test_home_topicList_success')
        r =  hello_parents_get(const.parents_home_topicList, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_home_topicList_success error")

    """评论列表"""
    def test_home_commentList_success(self):
        params = self.params_dict.__getitem__('test_home_commentList_success')
        # 删除参数中的articleid
        articleid = params['articleid']
        # url路径上带有参数,在这里进行拼装
        params.pop('articleid')
        r =  hello_parents_get(const.parents_home_commentList+"/"+articleid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_home_commentList_success error")

    """添加评论"""
    def test_home_commentAdd_success(self):
        params = self.params_dict.__getitem__('test_home_commentAdd_success')
        r =  hello_parents_post_url_params(const.parents_home_commentAdd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_home_commentAdd_success error")

    """添加建议"""
    def test_home_articleSuggestionAdd_success(self):
        params = self.params_dict.__getitem__('test_home_articleSuggestionAdd_success')
        r =  hello_parents_post_url_params(const.parents_home_articleSuggestionAdd, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_home_articleSuggestionAdd_success error")

    """文章详情"""
    def test_home_info_success(self):
        params = self.params_dict.__getitem__('test_home_info_success')
        # 删除参数中的articleid
        articleid = params['articleid']
        # url路径上带有参数,在这里进行拼装
        params.pop('articleid')
        r =  hello_parents_get(const.parents_home_info+"/"+articleid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_home_info_success error")

    """文章点赞"""
    def test_home_likea_success(self):
        params = self.params_dict.__getitem__('test_home_likea_success')
        # 删除参数中的articleid
        articleid = params['articleid']
        # url路径上带有参数,在这里进行拼装
        params.pop('articleid')
        r =  hello_parents_get(const.parents_home_like+"/"+articleid, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_home_likea_success error")

    """文章取消点赞"""
    def test_home_likeCancel_success(self):
        params = self.params_dict.__getitem__('test_home_likeCancel_success')
        # 删除参数中的likeid
        likeid = params['likeid']
        # url路径上带有参数,在这里进行拼装
        params.pop('likeid')
        r =  hello_parents_get(const.parents_home_likeCancel+"/"+likeid, params)
        sleep(0.5)
        self.assertEqual(r.code,300,"test_home_likeCancel_success error")

    """我的评论文章移除"""
    def test_home_commentRelCancel_success(self):
        params = self.params_dict.__getitem__('test_home_commentRelCancel_success')
        # 删除参数中的articleid
        articleid = params['articleid']
        # url路径上带有参数,在这里进行拼装
        params.pop('articleid')
        r =  hello_parents_get(const.parents_home_commentRelCancel+"/"+articleid, params)
        sleep(0.5)
        self.assertEqual(r.code,200,"test_home_commentRelCancel_success error")

    # """删除文章"""
    # def test_home_delete_success(self):
    #     params = self.params_dict.__getitem__('test_home_delete_success')
    #     # 删除参数中的articleid
    #     articleid = params['articleid']
    #     # url路径上带有参数,在这里进行拼装
    #     params.pop('articleid')
    #     r =  hello_parents_get(const.parents_home_delete+"/"+articleid, params)
    #     sleep(0.5)
    #     self.assertEqual(r.code,200,"test_home_delete_success error")

    @classmethod
    def tearDownClass(cls):
        pass