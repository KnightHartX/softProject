# -*- coding:utf-8 -*-
import tornado

from serverRequest import *

class MyApplication(tornado.web.Application):
    def __init__(self):
        handlers = [

            (r"/test", TestHandler),


        ]

        settings = {

        }
        tornado.web.Application.__init__(self, handlers,debug = False,**settings)
                #使用多进程的时候，记得设置为false