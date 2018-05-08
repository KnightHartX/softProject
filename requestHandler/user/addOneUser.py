from MysqlOrm import db,User
from commonFunc.getAllUser import GetAllUser
class AddOneUser():
    def entry(self,receiveRequest):
        # username = receiveRequest.get_argument('username')
        # pwd = receiveRequest.get_argument('pwd')
        userName = receiveRequest['userName']
        pwd = receiveRequest['pwd']
        result=self.judgeIsCanAdd(userName)
        if result['status']==0:
            return result

        with db.execution_context():
            User.create(**{"userName": userName, "userPwd": pwd,"userCollection":'[]'})

        return {"status":1,"info":"注册成功"}


    def judgeIsCanAdd(self,userName):
        getalluser=GetAllUser()
        if userName in getalluser.getAllUserName():
            return {"status":0,'errorinfo':"该用户名已被注册"}

        return {"status":1}


