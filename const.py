
"""
    全局常量文件
    请求的url都配置在这个文件中
"""
class ConstError(Exception): pass

class _const(object):
    def __setattr__(self, k, v):
        if k in self.__dict__:
            raise ConstError
        else:
            self.__dict__[k] = v

    def __getattr__(self, item):
        if item not in self.__dict__:
            raise ConstError
        else:
            return self.__dict__[item]

    def __delattr__(self, item):
        if item in self.__dict__:
             self.__dict__.pop(item)

const = _const()
#机构版baseurl
const.baseurl_org = "http://192.168.3.30/hello"
const.baseurl_parents = "http://192.168.3.30:8087"
#机构版sign验证常量字符串
const.sign_str = "MOLYFUN-GAMECOLLECTION"



"""机构版请求url"""
"""用户模块"""
#登陆
const.org_user_login = "/api/v1/user.do?login"
#用户菜单
const.org_user_function = "/api/v1/user.do?userFunction"
#用户录入
const.org_user_add = "/api/v1/user.do?add"
#老师列表
const.org_user_listbyorg = "/api/v1/user.do?userListByOrg"



"""家长版请求url"""
"""用户模块"""
#登陆
const.parents_user_login = "/api/v1/user/login"
#登出
const.parents_user_logout = "/api/v1/user/logout"
#用户信息
const.parents_user_info = "/api/v1/user/info"
#关于我们
const.parents_user_about = "/api/v1/user/about"
#短信验证码
const.parents_user_captcha = "/api/v1/user/captcha"
#我的消息列表
const.parents_user_messageList = "/api/v1/user/messageList"
#修改密码
const.parents_user_updatePassword = "/api/v1/user/updatePassword"
#建议反馈
const.parents_user_feedbackAdd = "/api/v1/user/feedbackAdd"
#版本检查
const.parents_user_checkVersion = "/api/v1/user/checkVersion"
#学生信息
const.parents_user_studentInfo = "/api/v1/user/studentInfo"
#修改学生信息
const.parents_user_updateStudentInfoFull = "/api/v1/user/updateStudentInfoFull"
#修改用户信息
const.parents_user_updateInfo = "/api/v1/user/updateInfo"
#更新邮箱
const.parents_user_updateemail = "/api/v1/user/updateemail"


"""报名模块"""
#报名须知
const.parents_enroll_notice = "/api/v1/enroll/notice"
#报名中列表
const.parents_enroll_enrollinglist = "/api/v1/enroll/enrollinglist"
#报名详情
const.parents_enroll_info = "/api/v1/enroll/info"
#报名信息提交
const.parents_enroll_infosubmit = "/api/v1/enroll/infosubmit"
#入学通知详情
const.parents_enroll_entrancenotice = "/api/v1/enroll/entrancenotice"
#修改报名学生信息
const.parents_enroll_infoupdate = "/api/v1/enroll/infoupdate"
#修改联系人信息
const.parents_enroll_contactupdate = "/api/v1/enroll/contactupdate"
#添加放弃原因
const.parents_enroll_abandoncauseadd = "/api/v1/enroll/abandoncauseadd"
#评测列表
const.parents_enroll_evaluatelist = "/api/v1/enroll/evaluatelist"
#评测结果列表
const.parents_enroll_evaluateresultlist = "/api/v1/enroll/evaluateresultlist"
#判断报名记录是否是放弃状态
const.parents_enroll_judgestatus = "/api/v1/enroll/judgestatus"


"""课程模块"""
#课程日期标识列表
const.parents_course_courseDateIdentifyList = "/api/v1/course/courseDateIdentifyList"
#我的下载列表
const.parents_course_courseUserList = "/api/v1/course/courseUserList"
#添加反馈
const.parents_course_fackbackadd = "/api/v1/course/feedbackAdd"
#修改反馈
const.parents_course_feedbackUpdate = "/api/v1/course/feedbackUpdate"
#课程反馈列表
const.parents_course_feedbacklist = "/api/v1/course/feedbacklist"
#课程详情
const.parents_course_info = "/api/v1/course/info"
#课程列表
const.parents_course_list = "/api/v1/course/list"
#课程总结
const.parents_course_summary = "/api/v1/course/summary"
#我的下载删除
const.parents_course_courseRelCancel = "/api/v1/course/courseRelCancel"


"""报告模块"""
#报告列表
const.parents_report_list = "/api/v1/report/list"
#报告详情
const.parents_report_info = "/api/v1/report/info"
#添加反馈
const.parents_report_feedbackAdd = "/api/v1/report/feedbackAdd"
#修改反馈
const.parents_report_feedbackUpdate = "/api/v1/report/feedbackUpdate"
#报告反馈列表
const.parents_report_feedbacklist = "/api/v1/report/feedbacklist"
#结果和日期接口（适用于折线图）
const.parents_report_resultAndDate = "/api/v1/report/resultAndDate"
#报告统计接口（适用于饼柱图）
const.parents_report_statistic = "/api/v1/report/statistic"
#课程目标和课程名称接口（适用于折线图）
const.parents_report_targetAndCourseList = "/api/v1/report/targetAndCourseList"


"""作业模块"""
#作业列表
const.parents_task_list = "/api/v1/task/list"
#作业日期标识列表
const.parents_task_taskDateIdentifyList = "/api/v1/task/taskDateIdentifyList"
#编辑作业
const.parents_task_update = "/api/v1/task/update"


"""评估模块"""
#评估列表
const.parents_evaluate_list = "/api/v1/evaluate/list"
#评估分析结果列表
const.parents_evaluate_analysisResultlist = "/api/v1/evaluate/analysisResultlist"
#分析结果文件列表
const.parents_evaluate_evaluateAnalysislist = "/api/v1/evaluate/evaluateAnalysislist"
#分析结果列表
const.parents_evaluate_evaluteProjectList = "/api/v1/evaluate/evaluteProjectList"


"""iep计划模块"""
#iep计划列表
const.parents_iep_queryIepPlanList = "/api/v1/iep/queryIepPlanList"
#iep内容分页列表
const.parents_iep_queryIepTempList = "/api/v1/iep/queryIepTempList"


"""咨询定制模块"""
#咨询定制列表
const.parents_custom_planlist = "/api/v1/custom/planlist"
#咨询定制创建
const.parents_custom_customplanCreate = "/api/v1/custom/customplanCreate"
#咨询定制资料数量
const.parents_custom_docNum = "/api/v1/custom/docNum"
#添加消息
const.parents_custom_msgAdd = "/api/v1/custom/msgAdd"
#消息列表
const.parents_custom_msgList = "/api/v1/custom/msgList"
#咨询定制评价
const.parents_custom_eval = "/api/v1/custom/eval"
#咨询定制资料列表
const.parents_custom_doclist = "/api/v1/custom/doclist"
#修改咨询定制资料
const.parents_custom_docUpdate = "/api/v1/custom/docUpdate"


"""个训模块"""
#个训列表
const.parents_training_list = "/api/v1/training/list"
#个训详情
const.parents_training_info = "/api/v1/training/info"
#个训反馈列表
const.parents_training_feedbackList = "/api/v1/training/feedbackList"
#个训目标
const.parents_training_targetinfo = "/api/v1/training/targetinfo"


"""素材模块"""
#素材分类属性列表
const.parents_gallery_attrlist = "/api/v1/gallery/attrlist"
#素材列表
const.parents_gallery_list = "/api/v1/gallery/list"


"""家园模块"""
#添加文章
const.parents_home_addArticle = "/api/v1/home/addArticle"
#文章列表
const.parents_home_articleList = "/api/v1/home/articleList"
#话题列表
const.parents_home_topicList = "/api/v1/home/topicList"
#评论列表
const.parents_home_commentList = "/api/v1/home/commentList"
#添加评论
const.parents_home_commentAdd = "/api/v1/home/commentAdd"
#添加建议
const.parents_home_articleSuggestionAdd = "/api/v1/home/articleSuggestionAdd"
#文章详情
const.parents_home_info = "/api/v1/home/info"
#文章点赞
const.parents_home_like = "/api/v1/home/like"
#文章取消点赞
const.parents_home_likeCancel = "/api/v1/home/likeCancel"
#我的评论文章移除
const.parents_home_commentRelCancel = "/api/v1/home/commentRelCancel"
#删除文章
const.parents_home_delete = "/api/v1/home/delete"


"""记录模块"""
#记录列表
const.parents_impression_list = "/api/v1/impression/list"
#添加记录
const.parents_impression_add = "/api/v1/impression/add"
#删除记录
const.parents_impression_delete = "/api/v1/impression/delete"


"""任务模块"""
#每日签到
const.parents_mission_dailySign = "/api/v1/mission/dailySign"
#任务类型列表
const.parents_mission_typeList = "/api/v1/mission/typeList"
#刷新日排行榜
const.parents_mission_refreshCharts = "/api/v1/mission/refreshCharts"
#任务列表
const.parents_mission_list = "/api/v1/mission/list"


"""通知模块"""
#通知详情
const.parents_notice_info = "/api/v1/notice/info"


"""消息模块"""
#批量删除消息
const.parents_message_batchdel = "/api/v1/message/batchdel"


"""机构信息模块"""
#机构老师详情
const.parents_org_user = "/api/v1/org/user"


"""机构模块"""
#投票列表
const.parents_depart_votelist = "/api/v1/depart/votelist"
#机构申请
const.parents_depart_validation = "/api/v1/depart/validation"
#添加机构评论
const.parents_depart_adddepartcomment = "/api/v1/depart/adddepartcomment"
#切换机构
const.parents_depart_changedepartfull = "/api/v1/depart/changedepartfull"
#学生机构列表
const.parents_depart_list = "/api/v1/depart/list"


"""排行榜模块"""
#排行榜列表
const.parents_charts_list = "/api/v1/charts/list"



























