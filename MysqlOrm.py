# coding=utf-8
import pymysql


class MysqlOrm:
    def __init__(self):
        self.conn=None
        self.cursor=None

    # 数据库链接信息
    def connect(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                password='admin',
                port=3306,
                db='project',
                charset='utf8'
            )
            self.cursor=self.conn.cursor()
            print('mysql access success')
        except:
            print('mysql access error')

    def execute_no_return(self, sql):
        """
        执行SQL语句,不获取返回结果
        :param sql: SQL语句
        """
        try:
            self.cursor.execute(sql)
            print('execute success')
        except:
            print('execute error')
        return 'execute success'

    def execute(self, sql):
        """
        执行SQL语句
        :param sql: SQL语句
        :return: 获取SQL执行并取回的结果
        """
        result = None
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print('execute success')
        except:
            print('execute error')
        return result if result else None
    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__=='__main__':
    db=MysqlOrm()
    db.connect()
    a='5000'
    b='k'
    sql="""insert into student_login (student_number,student_password) values ("%s" ,"%s")"""%(a,b)
    db.execute_no_return(sql)
    db.commit()
    db.close()