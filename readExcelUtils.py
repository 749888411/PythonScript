#! python3
# -*- coding:utf-8 -*-
import xlrd
import logging.config

# log配置
logging.config.fileConfig('logger.conf')
logger = logging.getLogger('logger')


# 打开Excel文件
def openExcel(fileName='excelFile.xls'):
    try:
        data = xlrd.open_workbook(fileName)
        return data
    except Exception as e:
        logger.error("Can not open filename：%s Exception info：%s " % (fileName, str(e)))


# 根据索引获取Excel表格中的数据
# 【参数说明】
# - fileName：Excel文件路径
# - colNameIndex：读取表头行的索引，从0开始
# - dataIndex：读取数据行数的索引
# - byIndex：表的索引，从0开始
def readExcelByIndex(fileName='excelFile.xls', colNameIndex=0, dataIndex=1, byIndex=0):
    data = openExcel(fileName)
    table = data.sheets()[byIndex]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colNames = table.row_values(colNameIndex)  # 某一行数据
    dataList = []
    for rowNum in range(dataIndex, nrows):
        row = table.row_values(rowNum)
        if row:
            app = {}
            for i in range(len(colNames)):
                if row[i] == "":
                    app[colNames[i]] = "null"
                else:
                    app[colNames[i]] = row[i]
            dataList.append(app)
    logger.info("Success get data from Excel, size:" + str(len(dataList)))
    return dataList


# 根据名称获取Excel表格中的数据
# 【参数说明】
#  - fileName：Excel文件路径
#  - colNameIndex：读取表头行的索引，从0开始
#  - dataIndex：读取数据行数的索引
#  - byName：Sheet1名称
def xcelByName(fileName='excelFile.xls', colNameIndex=0, dataIndex=1, byName=u'Sheet1'):
    data = openExcel(fileName)
    table = data.sheet_by_name(byName)
    nrows = table.nrows  # 行数
    colNames = table.row_values(colNameIndex)  # 某一行数据
    dataList = []
    for rowNum in range(dataIndex, nrows):
        row = table.row_values(rowNum)
        if row:
            app = {}
            for i in range(len(colNames)):
                if row[i] == "":
                    app[colNames[i]] = "null"
                else:
                    app[colNames[i]] = row[i]
            dataList.append(app)
    logger.info("Success get data from Excel, size:" + str(len(dataList)))
    return dataList
