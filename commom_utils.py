#! python3
# -*- coding:utf-8 -*-
from pypinyin import pinyin,lazy_pinyin
import pypinyin


# 提取中文拼音首字母
# 【参数说明】
#  - param：中文汉字
def get_first_letter(param):
    if param is not None and len(param) > 0:
        piny_list = pinyin(param, style=pypinyin.INITIALS)
        first_letter = piny_list[0][0]
        if len(first_letter) > 0:
            first_letter = first_letter[0: 1]
        return first_letter
    else:
        return None


# 获取总页数
# 【参数说明】
#  - totalNum：总行数
#  - pageSize：每页大小
def get_total_page_num(totalNum, pageSize):
    totalPageNum = 0
    if totalNum % pageSize == 0:
        totalPageNum = totalNum / pageSize
    else:
        totalPageNum = totalNum / pageSize + 1
    return int(totalPageNum)


# 获取当前页码开始的位置
# 【参数说明】
#  - currentPage：当前页码
#  - pageSize：每页大小
def get_current_page_start_index(currentPage, pageSize):
    return int((currentPage - 1) * pageSize)
