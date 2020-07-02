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

#插入数据
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])  #insert_one方法用于插入一条数据，不推荐使用insert方法
print(result)
print(result.inserted_ids)
