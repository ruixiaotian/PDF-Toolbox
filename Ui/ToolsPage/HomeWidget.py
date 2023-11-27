#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :HomeWidget.py
# @Time :2023-11-27 下午 05:34
# @Author :Qiao
from PyQt5.QtCore import QEasingCurve, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets.components import FlowLayout, SmoothScrollArea

from Ui.ToolsPage.BannerWidget import BannerWidget
from Ui.StyleSheet import ToolsPageStyleSheet
from Ui.ToolsPage.ToolsCard import (
    ToWordCard, ToPPTCard, FlatteningCard, MergeCard, PartitionCard
)


class ToolsHome(QWidget):
    """菜单页面的主页"""

    def __init__(self, parent) -> None:
        super().__init__()
        self.setObjectName("ToolsHome")
        self.banner = BannerWidget(parent)
        self.view = CardView(parent)

        self.setupLayout()

    def setupLayout(self) -> None:
        """设置布局"""
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.setSpacing(2)
        self.vBoxLayout.addWidget(self.banner)
        self.vBoxLayout.addWidget(self.view, 5)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.vBoxLayout)


class CardView(SmoothScrollArea):

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.setupView()
        self.setupViewLayout()

        self.setScrollAnimation(Qt.Vertical, 400, QEasingCurve.OutQuint)
        self.setWidgetResizable(True)
        self.setWidget(self.view)

        ToolsPageStyleSheet.HOME_PAGE.apply(self)

    def setupView(self) -> None:
        """创建视图"""
        # 创建控件
        self.view = QWidget()
        self.view.setObjectName("view")
        # 获取卡片
        self.toWordCard = ToWordCard()
        self.toPPTCard = ToPPTCard()
        self.flatteningCard = FlatteningCard()
        self.mergeCard = MergeCard()
        self.partitionCard = PartitionCard()

    def setupViewLayout(self) -> None:
        """设置布局"""
        self.flowLayout = FlowLayout(self, needAni=True)
        self.flowLayout.setAnimation(1000, QEasingCurve.OutQuad)

        self.flowLayout.setContentsMargins(30, 30, 30, 30)
        self.flowLayout.setHorizontalSpacing(15)
        self.flowLayout.setVerticalSpacing(25)

        self.flowLayout.addWidget(self.toWordCard)
        self.flowLayout.addWidget(self.toPPTCard)
        self.flowLayout.addWidget(self.flatteningCard)
        self.flowLayout.addWidget(self.mergeCard)
        self.flowLayout.addWidget(self.partitionCard)

        self.view.setLayout(self.flowLayout)
