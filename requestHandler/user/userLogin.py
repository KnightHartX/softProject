from MysqlOrm import MyBaseModel,User
from requestHandler.user.mySession import Session
from logConfig import logger
'''
请求数据格式：
{
    'username':name,
    'pwd':pwd
}

'''
class UserLogin():
    def entry(self,receiveRequest):
        # username=receiveRequest.get_argument('username','nohave')
        # pwd=receiveRequest.get_argument('pwd','null')
        userName=receiveRequest['userName']
        pwd=receiveRequest['pwd']
        return self.judge(receiveRequest,userName,pwd)

    def judge(self,receiveRequest,userName,pwd):
        try:
            nowUser = MyBaseModel.returnList(User.select(User.userName,User.userPwd).where(User.userName==userName))
            if len(nowUser) > 0:
                if nowUser[0]['userPwd'] == pwd:

                    my_session = Session(receiveRequest)
                    session_id = my_session.getSessionId()
                    my_session['name'] = userName
                    logger.info('用户：%s 登录' % userName)
                    return {"status": 1,'session_id': session_id,'username':userName}
                else:
                    logger.info('用户：%s 登录失败，原因：密码错误' % userName)
                    return {"status": 0, "errorInfo": "密码错误"}

            else:
                logger.info('用户：%s 登录失败，原因：该用户不存在' % userName)
                return {"status": 0, "errorInfo": "该用户名不存在"}
        except:
            raise