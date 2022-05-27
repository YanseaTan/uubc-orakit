#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import (askopenfilename,
                                askopenfilenames,
                                askdirectory,
                                asksaveasfilename)


class HuffmanCodingUtil:
    """霍夫曼编码&解码工具

    霍夫曼树构建：不断从所有子树中选择权重最低的两课构建新的子树
    霍夫曼树构建完毕后，根节点到每一个叶子节点的路径及其编码
    """

    class Node:
        """树节点"""

        def __init__(self, info, w, lchild=None, rchild=None):
            self.info = info
            self.weight = w
            self.lch = lchild
            self.rch = rchild

    @staticmethod
    def compress(file_path: str):
        print('compressing... ' + file_path)
        return 'Aha'

    @staticmethod
    def decompress(file_path: str, code_path: str):
        print(f'decompressing... {file_path}')
        print(f'using code file... {code_path}')
        return 'hhhh'


def init_func_file_compressor(menu: Menu, func_frm: ttk.LabelFrame):
    print(f'container size: width={func_frm.winfo_width()}, height={func_frm.winfo_height()}')

    # Label(func_frm, text='init_func_file_compress').pack(fill=BOTH, expand=1)

    def init_compressor():
        # 初始化面板前，先清空面板上所有内容
        print('init calculator... start')
        print('clear panel...')
        for child in func_frm.winfo_children():
            child.destroy()
        print('clear panel... done')

        print('init compressor')
        # 说明文字以及分割线
        ttk.Label(func_frm, text='compress if code file exist else decompress').grid(row=0, columnspan=2, sticky=EW)
        ttk.Separator(func_frm, orient=HORIZONTAL).grid(row=1, columnspan=2, sticky=EW, pady=15)

        # 选择待处理文件
        path_input = tk.StringVar()
        open_file_entry = ttk.Entry(func_frm, textvariable=path_input, width=60)
        open_file_btn = ttk.Button(func_frm, text='select...', width=15,
                                   command=lambda: path_input.set(askopenfilename()))
        open_file_entry.grid(row=2, column=0)
        open_file_btn.grid(row=2, column=1)

        # 选择存储目录
        path_output = tk.StringVar()
        save_file_entry = ttk.Entry(func_frm, textvariable=path_output, width=60)
        save_file_btn = ttk.Button(func_frm, text='save to...', width=15,
                                   command=lambda: path_output.set(asksaveasfilename()))
        save_file_entry.grid(row=3, column=0)
        save_file_btn.grid(row=3, column=1)

        # 分割线
        ttk.Separator(func_frm, orient=HORIZONTAL).grid(row=4, columnspan=2, sticky=EW, pady=15)

        # 选择字典文件
        path_dict = tk.StringVar()
        save_file_entry = ttk.Entry(func_frm, textvariable=path_dict, width=60)
        save_file_btn = ttk.Button(func_frm, text='select code...', width=15,
                                   command=lambda: path_dict.set(askopenfilename()))
        save_file_entry.grid(row=5, column=0)
        save_file_btn.grid(row=5, column=1)

        # 分割线
        ttk.Separator(func_frm, orient=HORIZONTAL).grid(row=6, columnspan=2, sticky=EW, pady=15)

        # 压缩/解压缩按钮 ~及功能
        def compress_func_route():
            if path_dict.get() == '':
                print('start compressing...')
                result = HuffmanCodingUtil.compress(path_input.get())
                print(result)
            else:
                print('start decompressing...')
                result = HuffmanCodingUtil.decompress(path_input.get(), path_dict.get())
                print(result)

        start_btn = ttk.Button(func_frm, text='Start to compress/decompress!', command=compress_func_route)
        start_btn.grid(row=7, columnspan=2, rowspan=5, sticky=EW, pady=5, padx=15)

    menu.add_command(label='File Compress', command=init_compressor)
