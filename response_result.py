"""机构版请求返回结果model"""
class ResultOrg(object):
    def __init__(self, status, msg, data=None):
        if data is None:
            response = []
        self.status = status
        self.msg = msg
        self.data = data

"""家长版请求返回结果model"""
class ResultParents(object):
    def __init__(self, code, msg, data=None):
        if data is None:
            response = []
        self.code = code
        self.msg = msg
        self.data = data




