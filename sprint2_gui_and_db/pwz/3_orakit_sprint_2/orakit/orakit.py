#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

import tkinter as tk
from tkinter import messagebox as msg


def help_callback():
    msg.showinfo('OraKit Help', 'no help')


def show_main_window():
    win = tk.Tk()
    win.title('OraKit 0.2')
    win.geometry('800x600')

    # menu config
    # create a menu bar
    menu_bar = tk.Menu(win)
    win.config(menu=menu_bar)
    # create menu and add menu items
    func_menu = tk.Menu(menu_bar, tearoff=0)
    func_menu.add_command(label='New File')
    menu_bar.add_cascade(label="File", menu=func_menu)

    # help_menu = tk.Menu(menu_bar)
    # help_menu.add_command(label='About', command=help_callback)
    # menu_bar.add_cascade(label="Help", menu=help_menu)
    menu_bar.add_cascade(label='About',
                         command=lambda: msg.showinfo('About', 'OraKit 0.2 Gui and Database Version\n'
                                                               'Read more in my blog ~ pwz.wiki\n'
                                                               'That\'s all ...'))

    win.mainloop()


if __name__ == '__main__':
    show_main_window()
