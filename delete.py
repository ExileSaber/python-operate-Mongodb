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

#不推荐的方法remove
'''
result = collection.remove({'name': 'Kevin'})  #符合条件的全部删除
print(result)
'''

#推荐的方法delete_one / delete_many
result = collection.delete_one({'name': 'Mike'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 21}})
print(result.deleted_count)