#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
from tkinter import *
from tkinter import ttk


def init_func_simple_calculator(menu: Menu, func_frm: ttk.LabelFrame):
    print(f'container size: width={func_frm.winfo_width()}, height={func_frm.winfo_height()}')
    # Label(func_frm, text='init_func_simple_calculator').pack(fill=BOTH, expand=1)

    def init_panel():
        ttk.Button(func_frm, text='1').grid(row=0, column=0)
        ttk.Button(func_frm, text='2').grid(row=0, column=1)
        ttk.Button(func_frm, text='3').grid(row=0, column=2)
        ttk.Button(func_frm, text='+').grid(row=0, column=3)

        ttk.Button(func_frm, text='4').grid(row=1, column=0)
        ttk.Button(func_frm, text='5').grid(row=1, column=1)
        ttk.Button(func_frm, text='6').grid(row=1, column=2)
        ttk.Button(func_frm, text='-').grid(row=1, column=3)

        ttk.Button(func_frm, text='7').grid(row=2, column=0)
        ttk.Button(func_frm, text='8').grid(row=2, column=1)
        ttk.Button(func_frm, text='9').grid(row=2, column=2)
        ttk.Button(func_frm, text='*').grid(row=2, column=3)

        ttk.Button(func_frm, text='0').grid(row=3, column=0)
        ttk.Button(func_frm, text='.').grid(row=3, column=1)
        ttk.Button(func_frm, text='/').grid(row=3, column=2)
        ttk.Button(func_frm, text='=').grid(row=3, column=3)

    menu.add_command(label='Simple Calculator', command=init_panel)



