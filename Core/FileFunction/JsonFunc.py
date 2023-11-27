#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :JsonFunc.py
# @Time :2023-7-25 下午 08:28
# @Author :Qiao
"""
对Json文件相关的增删改查, 进行接口封装
"""
import json
from abc import ABC
from pathlib import Path

from creart import add_creator, exists_module, it
from creart.creator import AbstractCreator, CreateTargetInfo

from Core.FileFunction import PathFunc, Template


class JsonFunc:

    def checkDataFile(self):
        """检查数据文件是否创建"""
        if not self.data_path.exists():
            # 检查文件夹是否存在
            self.data_path.mkdir(parents=True, exist_ok=True)
        if not it(PathFunc).config_path.exists():
            # 检查配置文件是否存在
            self.writeJson(it(PathFunc).config_path, Template.config_template)

    @staticmethod
    def writeJson(path: Path, data: list | dict):
        """写入json文件"""
        with open(path, mode="w", encoding="utf-8") as file:
            # 打开json文件并写入
            json.dump(obj=data, fp=file, indent=4)

    @staticmethod
    def readJson(path: Path):
        """读取Json文件"""
        with open(path, mode="r", encoding="utf-8") as file:
            # 读取json并返回
            return json.load(file)


class JsonFuncClassCreator(AbstractCreator, ABC):
    # 定义类方法targets，该方法返回一个元组，元组中包含了一个CreateTargetInfo对象，
    # 该对象描述了创建目标的相关信息，包括应用程序名称和类名。
    targets = (CreateTargetInfo("Core.FileFunction.JsonFunc", "JsonFunc"),)

    # 静态方法available()，用于检查模块"JsonFunc"是否存在，返回值为布尔型。
    @staticmethod
    def available() -> bool:
        return exists_module("Core.FileFunction.JsonFunc")

    # 静态方法create()，用于创建JsonFunc类的实例，返回值为JsonFunc对象。
    @staticmethod
    def create(create_type: [JsonFunc]) -> JsonFunc:
        return JsonFunc()


add_creator(JsonFuncClassCreator)
