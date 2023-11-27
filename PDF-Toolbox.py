#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :main.py
# @Time :2023-11-27 下午 03:48
# @Author :Qiao
import os
import sys

from Core.ConfigFunction import cfg
from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtWidgets import QApplication
from creart import it
from qfluentwidgets import FluentTranslator

from Ui import MainWindow

if __name__ == "__main__":
    if cfg.get(cfg.dpiScale) == "Auto":
        #  如果为自动则设置自适应适高DPI
        QApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
        )
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    else:
        # 否则设置缩放
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
        os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

    # 创建app实例
    app = QApplication(sys.argv)

    # 加载翻译
    locale = cfg.get(cfg.language).value
    fluentTranslator = FluentTranslator(locale)
    settingTranslator = QTranslator()
    settingTranslator.load(locale, "MenuInstaller", "_", "Ui/resource/i18n")
    app.installTranslator(fluentTranslator)
    app.installTranslator(settingTranslator)

    # 显示窗体
    it(MainWindow)
    # 进入循环
    app.exec_()
