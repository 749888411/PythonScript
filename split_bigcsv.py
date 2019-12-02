#! /usr/bin/env python 
# -*- coding:utf-8 -*-
# @File    : test.py
# @Time    : 2019/11/29 18:07
# @Desc    : 将大的csv文件按行切成小文件
import os
import time


def splitByLineCount(filename, count):
    fin = open(filename, 'r' ,encoding='UTF-8')
    try:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf, head, filename, sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf, head, filename, sub)
            print('total file number:' + str(sub))
    finally:
        fin.close()


def mkSubFile(lines, head, filename, sub):
    [des_filename, extname] = os.path.splitext(filename)
    filename = des_filename + '_' + str(sub) + extname
    print('make file: %s' % filename)
    f_out = open(filename, 'w', encoding='UTF-8')
    try:
        f_out.writelines([head])
        f_out.writelines(lines)
        return sub + 1
    finally:
        f_out.close()


if __name__ == '__main__':
    begin = time.time()
    splitByLineCount('D:\\temp\XXX.csv', 60000)
    end = time.time()
    print('time is %d seconds ' % (end - begin))
