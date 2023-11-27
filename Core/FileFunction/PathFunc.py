#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :FileFunctionBase.py
# @Time :2023-7-22 下午 08:25
# @Author :Qiao
"""
获取程序所需的所有路径
"""
import winreg
from abc import ABC
from pathlib import Path
from typing import List

from creart import add_creator, exists_module
from creart.creator import AbstractCreator, CreateTargetInfo


class PathFunc:
    """文件操作基类"""

    def __init__(self) -> None:
        """初始化"""
        # 系统路径
        self.system_base_path = self.getSystemPath()
        self.desktop_path = self.system_base_path[0]
        self.docs_path = self.system_base_path[1]

        # 软件路径
        self.base_path = self.docs_path / "Bridge Club" / "PDF ToolBox"
        self.data_path = self.base_path / "PDF ToolBox Data"
        self.tmp_path = self.base_path / "PDF ToolBox TmpFile"
        self.menu_path = self.base_path / "PDF ToolBox Menu File"
        # 配置文件路径
        self.config_path = self.data_path / "config.json"

    @staticmethod
    def getSystemPath() -> List[Path]:
        """获取系统的一些路径"""
        # 文档和桌面
        key = winreg.OpenKey(
            key=winreg.HKEY_CURRENT_USER,
            sub_key=r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders",
        )
        return [
            Path(winreg.QueryValueEx(key, "Desktop")[0]),
            Path(winreg.QueryValueEx(key, "Personal")[0])
        ]


class PathFuncClassCreator(AbstractCreator, ABC):
    # 定义类方法targets，该方法返回一个元组，元组中包含了一个CreateTargetInfo对象，
    # 该对象描述了创建目标的相关信息，包括应用程序名称和类名。
    targets = (CreateTargetInfo("Core.FileFunction.PathFunc", "PathFunc"),)

    # 静态方法available()，用于检查模块"PathFunc"是否存在，返回值为布尔型。
    @staticmethod
    def available() -> bool:
        return exists_module("Core.FileFunction.PathFunc")

    # 静态方法create()，用于创建PathFunc类的实例，返回值为PathFunc对象。
    @staticmethod
    def create(create_type: [PathFunc]) -> PathFunc:
        return PathFunc()


add_creator(PathFuncClassCreator)
