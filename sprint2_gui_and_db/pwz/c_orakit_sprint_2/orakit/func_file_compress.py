#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
from tkinter import *
from tkinter import ttk


def init_func_file_compress(menu: Menu, func_frm: ttk.LabelFrame):
    print(f'container size: width={func_frm.winfo_width()}, height={func_frm.winfo_height()}')
    # Label(func_frm, text='init_func_file_compress').pack(fill=BOTH, expand=1)

    def init_compress():
        pass

    menu.add_command(label='File Compress')

