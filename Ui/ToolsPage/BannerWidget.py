#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :BannerWidget.py
# @Time :2023-11-27 下午 05:41
# @Author :Qiao
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPainterPath, QLinearGradient
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame
from creart import it
from qfluentwidgets.common import isDarkTheme, FluentIconBase, TextWrap
from qfluentwidgets.components import IconWidget, TitleLabel, StrongBodyLabel
from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush

from Ui.StyleSheet import ToolsPageStyleSheet
from Ui.icon import MainWindowIcon


class BannerWidget(QWidget):
    """主页上方的 Banner Widget"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setFixedHeight(140)

        self.setObjectName("ToolsHomePageBanner")
        self.createControls()
        self.setupControls()
        self.setupLayout()

        ToolsPageStyleSheet.HOME_PAGE.apply(self)

    def createControls(self) -> None:
        """创建子控件"""
        self.banner = AcrylicBrush(self, 0.1)
        self.iconLabel = IconCard(MainWindowIcon.LOGO, self)
        self.titleLabel = TitleLabel("PDF Toolbox", self)
        content = self.tr(
            "If you are dealing with PDFs on a regular basis, "
            "PDF-Toolbox would be an excellent tool to make "
            "your life easier. By leveraging its robust features, "
            "you can streamline your workflow, save time, and "
            "focus more on what matters most - your work."
        )
        self.contentLabel = StrongBodyLabel(
            TextWrap.wrap(content, 160, False)[0]
        )
        self.topColor = QColor(255, 255, 255, 0)
        self.lightBottomColor = QColor(247, 249, 252, 255)
        self.darkBottomColor = QColor(33, 40, 49, 255)
        self.darkFocusBottomColor = QColor(39, 39, 39, 255)

        # 创建gradient
        self.gradient = QLinearGradient(0, self.height() - 70, 0, self.height())

    def setupControls(self) -> None:
        """设置控件"""
        # 设置banner
        self.banner.setImage(
            QPixmap(":ToolsPage/image/ToolsPage/Header.jpg").scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
        )
        # 设置iconLabel
        self.titleLabel.setObjectName("NameLabel")
        self.contentLabel.setObjectName("ContentLabel")

    def setupLayout(self) -> None:
        """设置Layout"""
        # 创建总布局
        self.hBoxLayout = QHBoxLayout(self)

        # 创建子布局
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(2)
        self.vBoxLayout.addWidget(self.contentLabel)
        self.vBoxLayout.setContentsMargins(10, 50, 10, 0)

        # 添加到总布局
        self.hBoxLayout.addWidget(self.iconLabel)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        # 设置布局属性
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(30, 10, 0, 0)
        self.hBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

    def _setupRadius(self) -> QPainterPath:
        """创建圆角"""
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        w, h = self.width(), self.height()
        path.addRoundedRect(QRectF(0, 0, w, h), 10, 10)
        path.addRect(QRectF(0, h - 50, 50, 50))
        path.addRect(QRectF(w - 50, 0, 50, 50))
        path.addRect(QRectF(w - 50, h - 50, 50, 50))
        path = path.simplified()
        self.banner.setClipPath(path)

    def updateGradient(self) -> None:
        """更新渐变"""
        from Ui import MainWindow
        # 根据主题绘制背景颜色
        if not isDarkTheme():
            self.gradient.setColorAt(0, self.topColor)  # 顶部透明
            self.gradient.setColorAt(0.15, self.lightBottomColor)  # 中间过度
            self.gradient.setColorAt(1, self.lightBottomColor)  # 底部浅色
        else:
            if not it(MainWindow).isActiveWindow():
                self.gradient.setColorAt(0, self.topColor)  # 顶部透明
                self.gradient.setColorAt(0.15, self.darkFocusBottomColor)  # 中间过度
                self.gradient.setColorAt(1, self.darkFocusBottomColor)  # 底部浅色
            else:
                self.gradient.setColorAt(0, self.topColor)  # 顶部透明
                self.gradient.setColorAt(0.15, self.darkBottomColor)  # 中间过度
                self.gradient.setColorAt(1, self.darkBottomColor)  # 底部深色

    def paintEvent(self, event) -> None:
        """paintEvent方法用于绘制部件的外观"""
        self.banner.paint()
        super().paintEvent(event)
        self.updateGradient()
        painter = QPainter(self)
        painter.setRenderHints(QPainter.SmoothPixmapTransform | QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.gradient)
        rect = QRectF(0, self.height() - 70, self.width(), 70)
        painter.drawRect(rect)

    def resizeEvent(self, event):
        """当窗口大小改变时，更新裁剪路径和渐变效果"""
        self._setupRadius()
        self.updateGradient()
        super().resizeEvent(event)


class IconCard(QFrame):

    def __init__(self, icon: FluentIconBase, parent=None) -> None:
        """初始化"""
        super().__init__(parent=parent)
        self.setFixedSize(130, 130)

        # 创建子控件并设置属性
        self.iconWidget = IconWidget(icon, self)
        self.iconWidget.setFixedSize(70, 70)

        # 添加到控件
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addWidget(self.iconWidget, 0, Qt.AlignCenter)

        ToolsPageStyleSheet.HOME_PAGE.apply(self)
