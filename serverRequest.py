import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from requestHandler.user.mySession import Session
import MysqlOrm

def judgeIsLogin(func):
    def is_login(self_request,*args):
        mySession=Session(self_request)
        username=mySession['getname']
        if username==None:
            del mySession
            self_request.finish({"status": 0, "errorInfo": "请先登录"})
        else:
            username=username.decode('utf-8')
            args=args+(username,)
            func(self_request,*args)
    return is_login





def getErrorMessage(post):
    def diyPost(self_request, *args):
        try:
            post(self_request, *args)
        except Exception as e:
            # logger.warning(errorMessage(e))
            self_request.finish({"status": 0, "errorInfo": "服务器出错，请稍后再试"})

    return diyPost

class BaseHandler(web.RequestHandler):  # 每个请求的基类
    def initialize(self):
        self.set_header("Access-Control-Max-Age", 3628800)
        self.set_header('Content-type', 'multipart/form-data')
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,authorization")
        self.set_header('Access-Control-Allow-Methods', 'POST,GET,PUT,DELETE,OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', True)
        self.set_header("Access-Control-Allow-Origin", "*")


class TestHandler(BaseHandler):
    def post(self):
        print(self.request.headers['Origin'])
        self.set_cookie(Session.session_id, '1231312312')
        print('i am get')
        self.finish({'status': 1})

    def get(self, *args, **kwargs):
        print(self.request)