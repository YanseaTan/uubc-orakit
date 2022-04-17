#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import author_util as aut
from author_util import Role


def help_callback():
    msg.showinfo('OraKit Help', 'no help')


def init_func(root, menu_bar, account):
    """根据用户角色初始化功能菜单"""
    # 首先将Function菜单下内容清空
    menu_func = menu_bar.winfo_children()[1]
    menu_func.delete(0, 9999)

    # 查询用户角色
    role = aut.select_role_by_account(account)
    # print(role)
    # 根据角色处理菜单项
    def available_for_this_role(_role):
        if str(_role) == role:
            return tk.NORMAL
        return tk.DISABLED
    menu_func.add_command(label='[TEST] Available for Role.Admin', state=available_for_this_role(Role.Admin))
    menu_func.add_command(label='[TEST] Available for Role.Visitor', state=available_for_this_role(Role.Visitor))
    menu_func.add_command(label='[TEST] Available for Role.Developer', state=available_for_this_role(Role.Developer))


def hidden_func_for_admin(root):
    hidden_win = tk.Toplevel(root)
    hidden_win.title('Hidden Func for Admin')
    hidden_win.geometry('500x400')

    # 新增用户
    lfrm = ttk.Labelframe(hidden_win, text='Account Insert', padding='5p')
    lfrm.pack(pady='5p')
    account = tk.StringVar()
    password = tk.StringVar()
    roles = tk.StringVar()
    ttk.Label(lfrm, text='Account:').grid(column=0, row=0, sticky=tk.W)
    ttk.Label(lfrm, text='Password:').grid(column=0, row=1, sticky=tk.W)
    ttk.Label(lfrm, text='Role:').grid(column=0, row=2, sticky=tk.W)
    ttk.Entry(lfrm, textvariable=account).grid(column=1, row=0)
    ttk.Entry(lfrm, textvariable=password).grid(column=1, row=1)
    role_input = ttk.Combobox(lfrm, textvariable=roles)
    role_input.grid(column=1, row=2)
    role_input['values'] = [role for role in Role]
    ttk.Button(lfrm, text='Submit', command=lambda: aut.create_account(account.get(), password.get(), roles.get())).grid(column=1, row=4, sticky=tk.E)

    # 查询用户
    lfrm2 = ttk.Labelframe(hidden_win, text='Search Account', padding='5p')
    lfrm2.pack(pady='10p')
    ttk.Label(lfrm2, text='Account:').grid(column=0, row=0, sticky=tk.W)
    ttk.Entry(lfrm2).grid(column=1, row=0)
    ttk.Button(lfrm2, text='Search').grid(column=1, row=1, sticky=tk.E)
    ttk.Label(lfrm2, text='(not impled)').grid(column=1, row=2, sticky=tk.E)


def login(root, menu_bar):
    def login_successful():
        """登录成功后显示功能项"""
        # print('login successful')
        root.title(f'OraKit 0.2, login with {account.get()}')
        msg.showinfo('login successful', 'login successful')
        if account.get() == aut.DEFAULT_ADMIN_ACCOUNT:
            menu_bar.add_command(label='[*hidden-func-for-admin]', command=lambda: hidden_func_for_admin(root))
        login_win.destroy()
        init_func(root, menu_bar, account.get())

    def login_fail():
        login_win.destroy()
        msg.showwarning('login fail', 'account or password error')

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

    login_win.bind('<Key-Return>', lambda event: login_successful() if aut.login_sys(account.get(), password.get()) else login_fail())


def init_menu(root):
    root.option_add('*tearOff', tk.FALSE)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # 系统
    menu_sys = tk.Menu(menu_bar)
    menu_bar.add_cascade(label='System', underline=3, menu=menu_sys)
    menu_sys.add_command(label='Login', underline=0, command=lambda: login(root, menu_bar))
    menu_sys.add_command(label='Exit', underline=0, command=lambda: root.destroy())

    # 功能
    menu_func = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="Function", menu=menu_func, underline=0)
    menu_func.add_command(label='Login First Please')

    # init_func(root, menu_bar, 'Role.Admin')

    # 关于
    menu_bar.add_cascade(label='About',
                         underline=0,
                         command=lambda: msg.showinfo('About', 'OraKit 0.2 Gui and Database Version\n'
                                                               'Read more in my blog ~ pwz.wiki\n'
                                                               'That\'s all ...'))


def show_main_window():
    win = tk.Tk()
    win.title('OraKit 0.2')
    win.geometry('800x600')

    aut.init_db()
    init_menu(win)

    win.mainloop()


if __name__ == '__main__':
    show_main_window()
