#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import time

from rm_duplication.file_info_persist import store_file_info

# 遍历指定目录，显示目录下的所有文件名


def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        if os.path.isdir(child):
            eachFile(child)
        else:
            file=os.stat(child)
            file_path = filepath
            file_name = allDir
            file_create_time = time.localtime(file.st_ctime)
            file_modify_time = time.localtime(file.st_mtime)
            file_size = file.st_size
            file_jason = {
                'path' : file_path,
                'name' : file_name,
                'create_time' : file_create_time,
                'modify_time' : file_modify_time,
                'size' : file_size
            }
            json_str = json.dumps(file_jason)
            #print('json_str is %s' % (json_str))
            store_file_info('picture','dup_pic', json_str)


if __name__ == '__main__':
    filePathC = "/Users/Jarvis/Pictures"
    eachFile(filePathC)