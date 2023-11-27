#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :StyleSheet.py
# @Time :2023-7-20 下午 09:13
# @Author :Qiao
from enum import Enum
from pathlib import Path

from qfluentwidgets import StyleSheetBase, Theme, qconfig


class MainWindowStyleSheet(StyleSheetBase, Enum):
    """主页样式表"""
    TITLE_BAR = "main_window"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return Path(f":MainWindow/qss/{theme.value.lower()}/MainWindow/{self.value}.qss").__str__()


class HomePageStyleSheet(StyleSheetBase, Enum):
    """主页样式表"""
    HOME_WIDGET = "home_widget"
    LINK_CARD = "link_card"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return Path(f":HomePage/qss/{theme.value.lower()}/HomePage/{self.value}.qss").__str__()


class SettingPageStyleSheet(StyleSheetBase, Enum):
    """设置页面样式表"""

    SETTING_PAGE = "setting_page"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return Path(f":SettingPage/qss/{theme.value.lower()}/SettingPage/{self.value}.qss").__str__()
