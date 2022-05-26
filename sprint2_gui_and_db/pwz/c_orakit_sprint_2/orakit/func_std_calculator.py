#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
from tkinter import *
from tkinter import ttk


def init_func_simple_calculator(menu: Menu, func_frm: ttk.LabelFrame):
    print(f'container size: width={func_frm.winfo_width()}, height={func_frm.winfo_height()}')
    # Label(func_frm, text='init_func_simple_calculator').pack(fill=BOTH, expand=1)

    def init_calculator():
        """实现标准计算器的面板以及计算逻辑 \n
        1、创建一个显示框以及对应的变量，显示、存储计算表达式 \n
        2、数组存好按钮文本，for循环使用grid方法将面板显示出来 \n
        3、依旧用循环初始化每个按钮对应的命令（向显示框追加字符、计算结果） \n
        4、实现第三步绑定的命令（4个：追加、删除、清除字符，计算结果） \n
        """