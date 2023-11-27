#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :icon.py
# @Time :2023-9-10 下午 04:49
# @Author :Qiao
from enum import Enum

from qfluentwidgets.common import getIconColor, Theme, FluentIconBase


class MainWindowIcon(FluentIconBase, Enum):
    LOGO = "Logo"

    def path(self, theme=Theme.AUTO) -> str:
        return f":MainWindow/image/MainWindow/{self.value}_{getIconColor(theme)}.svg"


class ToolsIcon(FluentIconBase, Enum):
    WORD = "Word"
    PPT = "PPT"
    PDF = "PDF"

    def path(self, theme=Theme.AUTO) -> str:
        return f":ToolsPage/image/ToolsPage/{self.value}.svg"
