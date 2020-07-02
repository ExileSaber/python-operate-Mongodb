import pymongo

#创建数据库连接，host和port自己补充
client = pymongo.MongoClient(host=, port=)
#另一种连接方式，host、port同上，替换掉下面的host和port
#client = pymongo.MongoClient('mongodb://host:port/')

#指定数据库
db = client.test
# 或者
#db = client['test']

#指定集合
collection = db.students
#collection = db['students']

count = collection.find().count()
print(count)
