#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import tinify
import click

import Config

tinify.tinify.key = Config.pinypng_key


# 判断是不是图片
def is_pic(name):
    # 获取文件名和文件类型
    filename, filetype = os.path.splitext(name)
    if filetype == ".png" or filetype == ".jpg" or filetype == ".jpeg":
        return "true"
    else:
        print(name + "不是图片")


# 压缩图片
def compressed(in_file, out_file):
    source = tinify.tinify.from_file(in_file)
    source.to_file(out_file)


# 遍历文件夹，压缩图片
def walk_folder(in_folder, out_filder):
    for root, dirs, files in os.walk(in_folder):
        size = files.__len__()
        count = 1
        for name in files:
            if not is_pic(name):
                size -= 1
                continue
            print("正在处理 %d/%d  %s " % (count, size, name))
            compressed(in_folder + "/" + name, out_filder + "/" + name)
            count += 1
        print("处理完成")
        break


# 没有任何参数，默认对预定文件夹操作
def default():
    source_dir = "/Users/zhe/Documents/_tinypng_file/uncompressed"
    save_dir = "/Users/zhe/Documents/_tinypng_file/compressed"
    walk_folder(source_dir, save_dir)


# 压缩单文件
def compressed_file(in_file):
    if not os.path.isfile(in_file):
        print("这不是文件")
        return
    # 文件路径
    dirname = os.path.dirname(in_file)
    # 文件名
    basename = os.path.basename(in_file)
    if not is_pic(basename):
        return
    print("开始处理" + basename)
    compressed(in_file, dirname + "/_" + basename)
    print("处理完成")


# 压缩文件夹下所有文件
def compressed_folder(dir):
    if not os.path.isdir(dir):
        print("这不是文件夹")
        return
    save_dir = dir + "/_tinypng"
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)
    walk_folder(dir, save_dir)


@click.command()
@click.option("-f", "--file", default=None, help="处理单文件")
@click.option("-d", "--dir", default=None, help="处理文件夹里所有文件")
def run(file, dir):
    if file is not None:
        compressed_file(file)
        pass
    elif dir is not None:
        compressed_folder(dir)
        pass
    else:
        default()
        pass


# 程序入口
if __name__ == "__main__":
    run()
