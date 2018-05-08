from MysqlOrm import MyBaseModel,Conference
import pandas as pd

result=MyBaseModel.returnList(Conference.select())
result=result[0:10]
result=pd.DataFrame(result)
print(result)