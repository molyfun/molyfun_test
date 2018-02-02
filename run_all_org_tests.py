#!/user/bin/python

from molyfun_org.test_case.a_user_case import user
import time
import unittest
from HTMLTestRunner3 import HTMLTestRunner
import sys

"""入口启动函数"""
if __name__ == '__main__':
    # 定义测试应用 机构版
    test_app = "./molyfun_org"
    #unittest自动化测试
    discover = unittest.defaultTestLoader.discover(test_app+"/test_case", pattern='*_case.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)



    # unittest结合HTMLTestRunner生成测试报告html
    # 定义测试应用 机构版
    now_time =  time.strftime("%Y_%m_%d_%H_%M_%S")
    fp = open(test_app+"/report/"+now_time+"result.html",'wb')
    runner = HTMLTestRunner(fp,
    title="机构版接口测试报告",verbosity=2)
    discover = unittest.defaultTestLoader.discover(test_app+"/test_case", pattern='*_case.py')
    runner.run(discover)
    fp.close()


