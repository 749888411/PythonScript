#! python3
# -*- coding:utf-8 -*-

import configparser

# 加载现有配置文件
conf = configparser.ConfigParser()
conf.read("./config/database-conf.ini")

# mysql配置文件
mysqlHostUrl = conf.get('MySQL', 'hostUrl')
mysqlPort = conf.getint('MySQL', 'port')
mysqlUsername = conf.get('MySQL', 'username')
mysqlPassword = conf.get('MySQL', 'password')
mysqlUseDatabase = conf.get('MySQL', 'useDatabase')

# mongo配置文件
mongoHostUrl = conf.get('Mongo', 'hostUrl')
mongoReplicaSet = conf.get('Mongo', 'replicaSet')
mongoUsername = conf.get('Mongo', 'username')
mongoPassword = conf.get('Mongo', 'password')
mongoUseDatabase = conf.get('Mongo', 'useDatabase')
