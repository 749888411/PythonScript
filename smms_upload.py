#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import click
import requests

upload_url = "https://sm.ms/api/upload"


def upload(file):
    files = {"smfile": (os.path.basename(file), open(file, "rb"))}
    data = {"ssl": True, "format": "json"}
    r = requests.post(upload_url, files=files, data=data)
    result = r.json()
    if "success" == result['code']:
        print("上传成功! 链接为: " + result['data']['url'])
    else:
        print("上传失败! ")


def upload_folder(dir):
    if not os.path.isdir(dir):
        print("这不是文件夹")
        return
    for root, dirs, files in os.walk(dir):
        upload_count = 1
        size = files.__len__()
        for name in files:
            if name.startswith("."):
                size -= 1
                continue
            file = dir + "/" + name
            print("正在上传%s  %d/%d" % (name, upload_count, size))
            upload(file)
            upload_count += upload_count


@click.command()
@click.option("-f", "--file", default=None, help="上传单文件")
@click.option("-d", "--dir", default=None, help="上传文件夹里所有文件")
def smms_upload(file, dir):
    if file is not None:
        upload(file)
    elif dir is not None:
        upload_folder(dir)


if __name__ == '__main__':
    smms_upload()
