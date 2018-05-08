from MysqlOrm import MyBaseModel,User

class GetAllUser():
    def __init__(self):
        self.users=MyBaseModel.returnList(User.select(User.userName))

    def getAllUserName(self):
        usersname=set()
        for user in self.users:
            usersname.add(user['userName'])

        return usersname
