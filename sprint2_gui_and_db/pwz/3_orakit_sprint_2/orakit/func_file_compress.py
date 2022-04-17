#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
from tkinter import *
from tkinter import ttk


def init_func_simple_calculator(menu: Menu, func_frm: ttk.LabelFrame):
    print(func_frm.winfo_width())
    Label(func_frm, text='init_func_simple_calculator').pack(fill=BOTH, expand=1)
    menu.add_command(label='Simple Calculator')


