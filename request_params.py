import json
import os
import sys
class Params:

    def __init__(self):
        pass

    #机构版加载配置文件
    def load_org_request_params(self,name):
        # 获取当前工作环境
        path = os.getcwd() + "/molyfun_org/config_params/" + name
        self.load_requesst_params(name, path)

    #家长版加载配置文件
    def load_parents_request_params(self,name):
        path = os.getcwd() + "/molyfun_parents/config_params/" + name
        self.load_requesst_params(name, path)


    def load_requesst_params(self,name,path):
        try:
            with open(path,encoding='utf-8') as json_load:
                data = json.load(json_load)
                self.__dict__ = data
                self.params_name = name
        except FileNotFoundError:
            print("==============================================")
            print("程序异常退出,退出原因:")
            print("模块"+sys._getframe().f_back.f_code.co_filename+"第"+str(sys._getframe().f_back.f_lineno)+"行,函数"+sys._getframe().f_back.f_code.co_name+"未找到参数配置文件:" + name)
            print("==============================================")
            os._exit(0)

    def __getitem__(self, item):
        if item not in self.__dict__:
            print("==============================================")
            print("程序异常退出,退出原因:")
            eror_desc = "模块"+sys._getframe().f_back.f_code.co_filename+"第"+str(sys._getframe().f_back.f_lineno)+"行,函数"+sys._getframe().f_back.f_code.co_name+"调用"+self.params_name+"未找到"+item+"参数"
            print(eror_desc)
            print("==============================================")
            os._exit(0)
        else:
            return self.__dict__[item]
