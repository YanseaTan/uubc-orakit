#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import author_util as aut


def help_callback():
    msg.showinfo('OraKit Help', 'no help')


def login(root):
    def login_successful():
        """登录成功后显示功能项"""
        print('login successful')
        pass

    login_win = tk.Toplevel(root)
    login_win.title('Login')
    login_win.geometry('300x100')

    frm = ttk.Frame(login_win)
    frm.pack(pady='10p')

    account = tk.StringVar()
    password = tk.StringVar()
    ttk.Label(frm, text='Account:').grid(column=0, row=0)
    ttk.Label(frm, text='Password:').grid(column=0, row=1)
    ttk.Entry(frm, textvariable=account).grid(column=1, row=0)
    ttk.Entry(frm, textvariable=password).grid(column=1, row=1)

    ttk.Separator(login_win, orient=tk.HORIZONTAL).pack(fill='x', pady='3p')
    ttk.Label(login_win, text='Enter to login').pack()

    login_win.bind('<Key-Return>', lambda event: login_successful() if aut.login_sys(account.get(), password.get()) else print('account or password error'))

    # aut.login_sys()


def init_menu(root):
    root.option_add('*tearOff', tk.FALSE)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # 系统
    menu_sys = tk.Menu(menu_bar)
    menu_bar.add_cascade(label='System', underline=3, menu=menu_sys)
    menu_sys.add_command(label='Login', underline=0, command=lambda: login(root))
    menu_sys.add_command(label='Exit', underline=0, command=lambda: root.destroy())

    # 功能
    menu_func = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="Function", menu=menu_func, underline=0)
    # todo add real funcs

    # 关于
    menu_bar.add_cascade(label='About',
                         underline=0,
                         command=lambda: msg.showinfo('About', 'OraKit 0.2 Gui and Database Version\n'
                                                               'Read more in my blog ~ pwz.wiki\n'
                                                               'That\'s all ...'))


def init_func(root):
    pass


def show_main_window():
    win = tk.Tk()
    win.title('OraKit 0.2')
    win.geometry('800x600')

    init_menu(win)
    ttk.Label(win, text='TEST').pack()
    ttk.Separator(win, orient=tk.HORIZONTAL).pack(fill='x')

    win.mainloop()


if __name__ == '__main__':
    show_main_window()
