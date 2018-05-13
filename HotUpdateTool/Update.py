#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Config
import json
import os
import sys
import hashlib

'''
思路:
1.读取配置文件
2.生成project.manifest
3.生成version.manifest
'''

#
IGNORE_FILES = ['.DS_Store', 'project.manifest', 'version.manifest']

# 生成的热更新文件信息路径
PROJECT_MANIFEST_PATH = os.path.join(sys.path[0] + "/../res", "project.manifest")

# 生成的热更新文件信息路径
VERSION_MANIFEST_PATH = os.path.join(sys.path[0] + "/../res", "version.manifest")

# src目录
RES_DIR_PATH = sys.path[0] + "/../res"

# res目录
SRC_DIR_PATH = sys.path[0] + "/../src"


#文件md5
def getFileMd5(fileName):
    if not os.path.isfile(fileName):
        return
    myHash = hashlib.md5()
    f = file(fileName, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myHash.update(b)
    f.close()
    return myHash.hexdigest()

#
def getDirFilesInfo(_fileInfo, _dirName):

    for dirPath, dirNames, fileNames in os.walk(_dirName):

        for fileName in fileNames:

            if not fileName in IGNORE_FILES:

                fileFullPath = os.path.join(dirPath, fileName)

                # print ("fileFullPath:", fileFullPath)

                md5 = getFileMd5(fileFullPath)
                # print ("md5:", md5)

                simplePath = fileFullPath.split(sys.path[0] + "/../")[1]
                # print ("simplePath:", simplePath)

                _fileInfo[simplePath] = {
                    "md5": getFileMd5(fileFullPath)
                }


#
def createProjectManifest():

    # project 配置文件
    projectConfigJson = {}

    # 固定配置
    projectConfigJson["packageUrl"] = Config.PACKAGE_URL
    projectConfigJson["remoteManifestUrl"] = Config.REMOTE_MANIFEST_URL
    projectConfigJson["remoteVersionUrl"] = Config.REMOTE_VERSION_URL
    projectConfigJson["version"] = Config.VERSION
    projectConfigJson["engineVersion"] = Config.ENGINE_VERSION

    # 资源src和res对应的md5
    projectConfigJson["assets"] = {}

    getDirFilesInfo(projectConfigJson["assets"], SRC_DIR_PATH)

    getDirFilesInfo(projectConfigJson["assets"], RES_DIR_PATH)


    # 固定搜索路径
    projectConfigJson["searchPaths"] = []

    # 生成配置
    jsonData = json.dumps(projectConfigJson)

    with open(PROJECT_MANIFEST_PATH, 'w') as f:
        f.write(jsonData)

    with open(VERSION_MANIFEST_PATH, 'w') as f:
        f.write(jsonData)



if __name__ == '__main__':
    print ("-----开始生成project.manifest-----")
    createProjectManifest()
    print ("-----生成project.manifest完成-----")














