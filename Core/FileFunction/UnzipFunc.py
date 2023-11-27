#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName :UnzipFunc.py
# @Time :2023-10-9 下午 05:54
# @Author :Qiao
"""
解压文件模块
"""
from pathlib import Path
import zipfile


class UnzipFile:

    @staticmethod
    def unzip(zipPath: Path, destinationPath: Path):
        """解压zip文件"""
        with zipfile.ZipFile(zipPath, "r") as zipObj:
            zipObj.extractall(destinationPath)
