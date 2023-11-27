#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :__init__.py.py
# @Time :2023-11-27 下午 05:31
# @Author :Qiao
from abc import ABC

from PyQt5.QtWidgets import QStackedWidget, QWidget
from creart import add_creator, exists_module
from creart.creator import CreateTargetInfo, AbstractCreator
from Ui.ToolsPage.HomeWidget import ToolsHome


class ToolsWidget(QStackedWidget):
    """工具界面"""

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("ToolsPage")

    def initialize(self, parent) -> None:
        """初始化"""
        self.parentClass = parent
        self.addPage()

    def addPage(self) -> None:
        """添加子页面"""
        # 获取页面
        self.toWordPage = QWidget()
        self.toPPTPage = QWidget()
        self.flatteningPage = QWidget()
        self.mergePage = QWidget()
        self.partitionPage = QWidget()
        self.HomePage = ToolsHome(self.parentClass)
        # 添加页面
        self.addWidget(self.HomePage)
        self.addWidget(self.toWordPage)
        self.addWidget(self.toPPTPage)
        self.addWidget(self.flatteningPage)
        self.addWidget(self.mergePage)
        self.addWidget(self.partitionPage)


class ToolsWidgetClassCreator(AbstractCreator, ABC):
    # 定义类方法targets，该方法返回一个元组，元组中包含了一个CreateTargetInfo对象，
    # 该对象描述了创建目标的相关信息，包括应用程序名称和类名。
    targets = (CreateTargetInfo("Ui.ToolsPage", "ToolsWidget"),)

    # 静态方法available()，用于检查模块"ToolsWidget"是否存在，返回值为布尔型。
    @staticmethod
    def available() -> bool:
        return exists_module("Ui.ToolsPage")

    # 静态方法create()，用于创建ToolsWidget类的实例，返回值为ToolsWidget对象。
    @staticmethod
    def create(create_type: [ToolsWidget]) -> ToolsWidget:
        return ToolsWidget()


add_creator(ToolsWidgetClassCreator)
