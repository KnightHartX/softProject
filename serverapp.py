import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from MysqlOrm import MysqlOrm
from MysqlSQL import SQL_general

input_student_login={
    'student_number':'',
    'student_password':'',
    'student_mail':'',
    'student_details':''
}

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class registHandler(tornado.web.RequestHandler):
    def get(self):
        input_student_login['student_number'] = self.get_argument('inputnumber')
        input_student_login['student_password'] = self.get_argument('inputPassword')
        input_student_login['student_mail'] = self.get_argument('inputEmail')
        input_student_login['student_password'] = self.get_argument('inputPassword')

        db = MysqlOrm()
        db.connect()
        sql = SQL.student_login_insert_sql(input_student_login)
        db.execute_no_return(sql)
        db.commit()
        db.close()



# class IndexHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render('index.html')
#
# class PoemPageHandler(tornado.web.RequestHandler):
#     def post(self):
#         noun1 = self.get_argument('noun1')
#         noun2 = self.get_argument('noun2')
#         verb = self.get_argument('verb')
#         noun3 = self.get_argument('noun3')
#         self.render('poem.html', roads=noun1, wood=noun2, made=verb,
#                 difference=noun3)

if __name__ == '__main__':
    # 数据库链接
    db = MysqlOrm()
    SQL = SQL_general()
    db.connect()

    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/regist',registHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()