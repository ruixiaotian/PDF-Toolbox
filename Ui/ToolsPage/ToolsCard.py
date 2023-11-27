#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :ToolsCard.py
# @Time :2023-11-27 下午 06:52
# @Author :Qiao
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget
from creart import it
from qfluentwidgets.common import FluentIconBase
from qfluentwidgets.components import (
    IconWidget, CardWidget, TabBar, TabItem, TabCloseButtonDisplayMode,
    SubtitleLabel
)

from Ui.StyleSheet import ToolsPageStyleSheet
from Ui.icon import ToolsIcon as Ti


class ToolsCardBase(CardWidget):
    text: str
    routeKey: str
    titleLabel: QLabel
    iconWidget: IconWidget
    icon: FluentIconBase
    page: QWidget

    def __init__(self) -> None:
        """初始化控件"""
        super().__init__()
        # 设置卡片属性
        self.setFixedSize(200, 200)
        self.setCursor(Qt.PointingHandCursor)

        # 创建子控件
        self.iconWidget = IconWidget(self)
        self.titleLabel = SubtitleLabel(self)

        # 设置子控件
        self.iconWidget.setFixedSize(64, 64)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        # 设置布局
        self.BoxLayout = QGridLayout(self)
        self.BoxLayout.setVerticalSpacing(0)
        self.BoxLayout.addWidget(self.iconWidget, 0, 0, 1, 1,  Qt.AlignHCenter)
        self.BoxLayout.addWidget(self.titleLabel, 1, 0, 1, 1, Qt.AlignHCenter)
        self.BoxLayout.setContentsMargins(0, 50, 0, 20)
        self.setLayout(self.BoxLayout)

        # 引用样式表
        ToolsPageStyleSheet.TOOLS_CARD.apply(self)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """重构鼠标事件实现点击效果"""
        super().mouseReleaseEvent(event)
        from Ui import MainWindow
        from Ui.ToolsPage import ToolsWidget
        if self.routeKey in it(MainWindow).titleBar.tabBar.itemMap:
            # 判断routeKey是否重复
            it(ToolsWidget).setCurrentWidget(self.page)
            it(MainWindow).titleBar.tabBar.setCurrentTab(self.routeKey)
        else:
            self.addTab()

    def addTab(self):
        """添加Tab"""
        from Ui import MainWindow
        self.tabBar: TabBar = it(MainWindow).titleBar.tabBar

        self.item = TabItem(self.text, self.tabBar.view, self.icon)
        self.item.setRouteKey(self.routeKey)

        # 设置Tab大小
        self.item.setMinimumWidth(it(MainWindow).titleBar.tabWidth)
        self.item.setMaximumWidth(self.tabBar.tabMaximumWidth())

        # 设置样式
        self.item.setShadowEnabled(self.tabBar.isTabShadowEnabled())
        self.item.setCloseButtonDisplayMode(TabCloseButtonDisplayMode.ON_HOVER)
        self.item.setSelectedBackgroundColor(
            self.tabBar.lightSelectedBackgroundColor,
            self.tabBar.darkSelectedBackgroundColor
        )

        # 链接信号
        self.item.pressed.connect(self.tabTrough)
        self.item.closed.connect(self.tabCloseTrough)

        # 添加进tab
        index = self.tabBar.count() + 1
        self.tabBar.itemLayout.insertWidget(index, self.item, 1)
        self.tabBar.items.insert(index, self.item)
        self.tabBar.itemMap[self.routeKey] = self.item

        # 静止滚动
        self.tabBar.setScrollable(False)

        # 切换至tab和切换至相对应页面
        self.tabTrough()

    def tabTrough(self) -> None:
        """tab标签被点击时的槽函数"""
        from Ui import MainWindow
        from Ui.ToolsPage import ToolsWidget
        self.tabBar.setCurrentTab(self.routeKey)
        it(MainWindow).stackedWidget.setCurrentWidget(it(ToolsWidget))
        it(ToolsWidget).setCurrentWidget(it(ToolsWidget).findChild(QWidget, self.routeKey))

    def tabCloseTrough(self) -> None:
        """tab标签关闭时槽函数"""
        from Ui.CheatsPage import ToolsWidget
        it(ToolsWidget).setCurrentWidget(it(ToolsWidget).HomePage)
        self.tabBar.setCurrentTab("HomeTab")
        self.tabBar.tabCloseRequested.emit(self.tabBar.items.index(self.item))


class ToWordCard(ToolsCardBase):

    def __init__(self) -> None:
        """初始化控件"""
        super().__init__()
        # 设置子控件
        self.iconWidget.setIcon(Ti.WORD)
        self.titleLabel.setText(self.tr("PDF To Word"))

        from Ui.ToolsPage import ToolsWidget
        self.routeKey = 'toWord'
        self.text = 'PDF TO Word'
        self.icon = Ti.WORD
        self.page = it(ToolsWidget).toWordPage


class ToPPTCard(ToolsCardBase):

    def __init__(self) -> None:
        """初始化控件"""
        super().__init__()
        # 设置子控件
        self.iconWidget.setIcon(Ti.PPT)
        self.titleLabel.setText(self.tr("PDF To PPT"))

        from Ui.ToolsPage import ToolsWidget
        self.routeKey = 'toPPT'
        self.text = 'PDF TO PPT'
        self.icon = Ti.PPT
        self.page = it(ToolsWidget).toPPTPage


class FlatteningCard(ToolsCardBase):

    def __init__(self) -> None:
        """初始化控件"""
        super().__init__()
        # 设置子控件
        self.iconWidget.setIcon(Ti.PDF)
        self.titleLabel.setText(self.tr("PDF Flattening"))

        from Ui.ToolsPage import ToolsWidget
        self.routeKey = 'PDF Flattening'
        self.text = 'PDF Flattening'
        self.icon = Ti.PDF
        self.page = it(ToolsWidget).flatteningPage


class MergeCard(ToolsCardBase):

    def __init__(self) -> None:
        """初始化控件"""
        super().__init__()
        # 设置子控件
        self.iconWidget.setIcon(Ti.PDF)
        self.titleLabel.setText(self.tr("PDF Merge"))

        from Ui.ToolsPage import ToolsWidget
        self.routeKey = 'PDF Merge'
        self.text = 'PDF Merge'
        self.icon = Ti.PDF
        self.page = it(ToolsWidget).mergePage


class PartitionCard(ToolsCardBase):

    def __init__(self) -> None:
        """初始化控件"""
        super().__init__()
        # 设置子控件
        self.iconWidget.setIcon(Ti.PDF)
        self.titleLabel.setText(self.tr("PDF Partition"))

        from Ui.ToolsPage import ToolsWidget
        self.routeKey = 'PDF Partition'
        self.text = 'PDF Partition'
        self.icon = Ti.PDF
        self.page = it(ToolsWidget).partitionPage
