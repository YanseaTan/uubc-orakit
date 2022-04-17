#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
from tkinter import *
from tkinter import ttk


def init_func_file_compress(menu: Menu, func_frm: ttk.LabelFrame):
    Label(func_frm, text='init_func_file_compress').pack(fill=BOTH, expand=1)
    menu.add_command(label='File Compress')


