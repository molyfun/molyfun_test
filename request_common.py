import requests
import json
from response_result import ResultOrg
from response_result import ResultParents
import random
import time
from const import const
import hashlib
from molyfun_org.except_paths import org_paths
from molyfun_parents.except_paths import parents_paths
from const import ConstError
import os

"""机构版post请求"""
def hello_org_post(url,params):
    #添加header
    headers = {'content-type': 'application/json' }
    assembly_params_org(params, url)
    response =  requests.post(const.baseurl_org+url, data=json.dumps(params),headers=headers)
    check_response_status(response)
    result = ResultOrg(**json.loads(response.text))
    return result



"""机构版get请求"""
def hello_org_get(url,params):
    assembly_params_org(params, url)
    params_str = ''
    for (d,x) in params.items():
        params_str += '&'+ d + '=' + str(x)
    response =  requests.get(const.baseurl_org+url+params_str)
    check_response_status(response)
    result_txt = response.text
    result_txt = result_txt[2:-2]
    result = ResultOrg(**json.loads(result_txt))
    return result

"""机构版组装sign参数"""
def assembly_params_org(params,url):
    """验证该接口需不需要uid"""
    if url not in org_paths:
        uid = ''
        try:
            uid = const.__getattr__('uid')
        except ConstError:
            print("uid 取值错误,确认是否已经登陆")
        session_id = const.__getattr__("session_id")
        params['uid'] = uid
        m = hashlib.md5()
        m.update((uid+session_id).encode('utf-8'))
        md5value = m.hexdigest()
        params['sid'] = md5value

    nonce = ''
    # 生成10位随机字母
    for i in range(10):
        nonce += chr(random.randint(97, 122))
    params['nonce'] = nonce.upper()
    params['timestamp'] = int(round(time.time() * 1000))
    params['mobile'] = 'html'
    gen_sign(params)


"""根据nonce timestamp signature生成sign"""
def gen_sign(params):
    sign_list = [params['nonce'],const.sign_str]
    sign_list.sort()
    sign_str = ''
    for signstr in sign_list:
        sign_str += signstr
    sign_str = str(params['timestamp']) + sign_str
    sign_sha1 = hashlib.sha1()
    sign_sha1.update(sign_str.encode('utf-8'))
    #对拼接好的字符串进行sha1加密
    params['signature'] = sign_sha1.hexdigest()

def check_response_status(response):
    #检查服务器状态 如果返回的状态值不是200 程序退出
    if(response.status_code != 200):
        print("==============================================")
        print("程序异常退出,退出原因:")
        print("服务器连接异常,http错误码是:"+ str(response.status_code) +",请联系管理员")
        print("==============================================")
        # os._exit(0)




"""家长版post请求 参数拼接在url上"""
def hello_parents_post_url_params(url,params):
    #添加header
    headers =  assembly_params_parents( url)
    params_str = assembly_paramsstr_parents(params)
    response =  requests.post(const.baseurl_parents+url+params_str,headers=headers)
    check_response_status(response)
    result = ResultParents(**json.loads(response.text))
    return result


"""家长版post请求 body体提交"""
def hello_parents_post(url,params):
    #添加header
    headers =  assembly_params_parents(url)
    response =  requests.post(const.baseurl_parents+url,data=json.dumps(params),headers=headers)
    check_response_status(response)
    result = ResultParents(**json.loads(response.text))
    return result


"""家长版post请求 既有参数拼接在url上 又有body体提交"""
def hello_parents_post_url_body(url,params):
    #添加header
    headers =  assembly_params_parents( url)
    params_str = assembly_paramsstr_parents(params)
    response =  requests.post(const.baseurl_parents+url+params_str,data=json.dumps(params),headers=headers)
    check_response_status(response)
    result = ResultParents(**json.loads(response.text))
    return result


"""家长版get请求"""
def hello_parents_get(url,params):
    #添加header
    headers =  assembly_params_parents( url)
    params_str = assembly_paramsstr_parents(params)
    response =  requests.get(const.baseurl_parents+url+params_str,headers=headers)
    check_response_status(response)
    result = ResultParents(**json.loads(response.text))
    return result



"""家长版组装参数"""
def assembly_params_parents(url):
    headers = {'content-type': 'application/json'}
    """验证该接口需不需要uid"""
    if url not in parents_paths:
        token = ''
        try:
            token = const.__getattr__('token')
            headers['token'] = token
        except ConstError:
            print("token 取值错误,确认是否已经登陆")
    return headers

#url上带参数时,拼装url参数
def assembly_paramsstr_parents(params):
    params_str = '?'
    i = 0
    for (d,x) in params.items():
        if i == 0:
            params_str += d + '=' + str(x)
        else:
            params_str += '&' + d + '=' + str(x)
        i += 1
    return params_str