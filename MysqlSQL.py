# encoding:utf-8

class SQL_general:
    def __init__(self):
        pass

    """
        插入学生注册信息：
        输入：input[]:账号、密码、邮箱、附加信息
        输出：插入的SQL语句
    """
    def student_login_insert_sql(self,input):
        sql="""insert into student_login (student_number,student_password,student_mail,student_details) 
            values('%s','%s','%s','%s')"""%(input['student_number'],input['student_password'],input['student_mail'],input['student_details'])
        return sql

    """
            插入教师注册信息：
            输入：input[]:账号、密码、邮箱、附加信息
            输出：插入的SQL语句
    """
    def teacher_login_insert_sql(self,input):
        sql = """insert into teacher_login (teacher_number,teacher_password,teacher_mail,teacher_details) 
                    values('%s','%s','%s','%s')""" % (input['teacher_number'], input['teacher_password'], input['teacher_mail'], input['teacher_details'])
        return sql

    """
    查询学生信息是否被注册：
    输入：input[]:账号
    输出：查询结果的SQL语句   （后续判断result是否未None）
    """
    def student_login_search_sql(self,input):
        sql="""select * from student_login where (student_number=%s)"""%(input['student_number'])
        return sql

    """
        查询教师信息是否被注册：
        输入：input[]:账号
        输出：查询结果的SQL语句   （后续判断result是否未None）
    """
    def teacher_login_search_sql(self,input):
        sql="""select * from teacher_login where (teacher_number=%s)"""%(input['teacher_number'])
        return sql