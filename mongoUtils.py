#! python3
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import logging
import logging.config
import LoadConf


# log配置
logging.config.fileConfig('logger.conf')
logger = logging.getLogger('logger')

# 查询集合
# 【参数说明】
# - databaseName：数据库名称
# - collectionName：集合名称
def queryCollection(databaseName, collectionName):
    try:
        # 创建mongo链接
        client = MongoClient(LoadConf.mongoHostUrl, replicaset=LoadConf.mongoReplicaSet)
        # 连接数据库，没有则自动创建
        mongoDb = client[databaseName]
        mongoDb.authenticate(LoadConf.mongoUsername, LoadConf.mongoPassword)
        # 使用集合，没有则自动创建
        mongoCol = mongoDb[collectionName]
        return mongoCol
    except Exception as e:
        logger.error("Error: unable to update mongo data" + str(e))
    finally:
        client.close()
