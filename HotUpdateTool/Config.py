#!/usr/bin/python
# -*- coding: UTF-8 -*-

#远程资源下载根路径
PACKAGE_URL = "http://127.0.0.1:10086/update"

#远程配置文件project.manifest的路径,包含版本信息和所有的资源信息
REMOTE_MANIFEST_URL = "http://127.0.0.1:10086/update/project.manifest"

#project.manifest的简化版本,用来判断是否有新版本需要热更
REMOTE_VERSION_URL = "http://127.0.0.1:10086/update/version.manifest"

#配置文件对应的游戏版本
VERSION = "1.0.0"

#配置文件对应的引擎版本
ENGINE_VERSION = "3.1"
