#! python3
# -*- coding:utf-8 -*-
import pymysql
import LoadConf
import logging.config
from commonUtils import CommonUtil

# log配置
logging.config.fileConfig('logger.conf')
logger = logging.getLogger('logger')


# 打开数据库连接
def getMysqlConn():
    mysqlConn = pymysql.connect(host=LoadConf.mysqlHostUrl, port=LoadConf.mysqlPort, user=LoadConf.mysqlUsername,
                              passwd=LoadConf.mysqlPassword, db=LoadConf.mysqlUseDatabase, charset="utf8")
    return mysqlConn


# 查询Mysql多条数据
# 【参数说明】
# - querySQL：查询语句
# - isPrintLog：是否打印日志
# - msg：打印日志
def queryList(querySQL, isPrintLog=True, msg="Mysql fetch result size: %d "):
    try:
        mysqlConn = getMysqlConn()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = mysqlConn.cursor()
        cursor.execute('SET NAMES UTF8')
        mysqlConn.commit()
        cursor.execute(querySQL)
        # 执行 SQL 查询
        result = cursor.fetchall()
        if isPrintLog:
            logger.info(msg % len(result))
        return result
    except Exception as ex:
        logger.error('Insert operation error：%s' % str(ex))
        raise
    finally:
        # 关闭数据库连接
        cursor.close()
        mysqlConn.close()


# 查询Mysql分页查询多条数据
# 【参数说明】
# - querySQL：查询语句
# - currentPage：当前页码
# - pageSize：每页大小
# - isPrintLog：是否打印日志
# - msg：打印日志
def queryPage(querySQL, currentPage=1, pageSize=10, isPrintLog=True, msg="Mysql fetch result size: %d "):
    try:
        mysqlConn = getMysqlConn()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = mysqlConn.cursor()
        cursor.execute('SET NAMES UTF8')
        mysqlConn.commit()
        startIndex = CommonUtil.get_current_page_start_index(currentPage, pageSize)
        querySQL = querySQL + " LIMIT %d,%d " % (startIndex, pageSize)
        cursor.execute(querySQL)
        # 执行 SQL 查询
        result = cursor.fetchall()
        if isPrintLog:
            logger.info(msg % len(result))
        return result
    except Exception as ex:
        logger.error('Insert operation error：%s' % str(ex))
        raise
    finally:
        # 关闭数据库连接
        cursor.close()
        mysqlConn.close()


# mysql单条查询
# 【参数说明】
# - querySQL：查询语句
# - isPrintLog：是否打印日志
# - msg：打印日志
def queryOne(querySQL, isPrintLog=False, msg="Mysql fetch one result"):
    try:
        mysqlConn = getMysqlConn()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = mysqlConn.cursor()
        cursor.execute('SET NAMES UTF8')
        mysqlConn.commit()
        cursor.execute(querySQL)
        # 执行 SQL 查询
        result = cursor.fetchone()
        if isPrintLog:
            logger.info(msg)
        return result
    except Exception as ex:
        logger.error('Query operation exception ：%s' % str(ex))
        raise
    finally:
        # 关闭数据库连接
        cursor.close()
        mysqlConn.close()


# 更新Mysql数据
# 【参数说明】
# - updateSQL：更新语句
# - isPrintLog：是否打印日志
# - msg：打印日志
def updateOne(updateSQL, isPrintLog=True, msg="Update success, Affect row size: %d, Execute SQL: %s"):
    try:
        mysqlConn = getMysqlConn()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = mysqlConn.cursor()
        cursor.execute('SET NAMES UTF8')
        mysqlConn.commit()
        # 使用 execute()  方法执行 SQL 查询
        updateSQL = updateSQL.replace("'null'", "null")
        rowcount = cursor.execute(updateSQL)
        mysqlConn.commit()
        if isPrintLog:
            logger.info(msg % (rowcount, updateSQL))
    except Exception as ex:
        logger.error("Unable to update mysql data：%s" % str(ex))
        mysqlConn.rollback()
        raise
    finally:
        # 关闭数据库连接
        cursor.close()
        mysqlConn.close()


# 批量更新Mysql数据
# 【参数说明】
# - updateSQLlist：更新语句list
# - msg：打印日志
def updateBatch(updateSQLlist, isPrintLog=True, msg="Update success, Affect row size: %d"):
    try:
        rowcount = 0
        mysqlConn = getMysqlConn()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = mysqlConn.cursor()
        cursor.execute('SET NAMES UTF8')
        mysqlConn.commit()
        # 使用 execute()  方法执行 SQL 查询
        for index in range(len(updateSQLlist)):
            logger.info(updateSQLlist[index])
            updateSQLlist[index] = updateSQLlist[index].replace("'null'", "null")
            n = cursor.execute(updateSQLlist[index])
            rowcount += n
        mysqlConn.commit()
        if isPrintLog:
            logger.info(msg % rowcount)
    except Exception as ex:
        logger.error("Unable to update mysql data：%s" % str(ex))
        mysqlConn.rollback()
        raise
    finally:
        # 关闭数据库连接
        cursor.close()
        mysqlConn.close()
