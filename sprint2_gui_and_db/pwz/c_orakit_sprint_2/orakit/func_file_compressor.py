#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python version: 3.9
# created by pwz.wiki 2022
"""
通用文件压缩

refer：
https://zhuanlan.zhihu.com/p/37652118
https://github.com/tclxspy/Articles/blob/master/algorithm/MD/%E7%AE%97%E6%B3%95%2319--%E9%9C%8D%E5%A4%AB%E6%9B%BC%E5%8E%8B%E7%BC%A9%EF%BC%88%E6%95%B0%E6%8D%AE%E5%8E%8B%E7%BC%A9%EF%BC%89.md
"""
import json
import os.path
import pickle
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import (askopenfilename,
                                askopenfilenames,
                                askdirectory,
                                asksaveasfilename)

import six


class HuffmanCodingUtil:
    """霍夫曼编码&解码工具

    霍夫曼树构建：不断从所有子树中选择权重最低的两课构建新的子树
    霍夫曼树构建完毕后，根节点到每一个叶子节点的路径及其编码
    """

    @staticmethod
    def compress(file_path: str, save_path: str):
        """霍夫曼编码压缩过程"""
        print('-'*50 + '\nHuffmanCodingUtil.compress() >>>\n' + '-'*50)

        class Node:
            """树节点"""
            def __init__(self, info, w, parent=None, lchild=None, rchild=None):
                self.info = info
                self.weight = w
                self.parent = parent
                self.lch = lchild
                self.rch = rchild

        print('compressing... ' + file_path)
        file_size = os.path.getsize(file_path)
        print(f'original file size = {file_size} byte(s)')

        # 初始化霍夫曼编码
        huffman_code = {}
        def init_huffman_code():
            # 按照字节计算文件中编码权重
            weight = {}
            with open(file_path, mode='rb') as f:
                for i in range(file_size):
                    bin_input = f.read(1)
                    weight.setdefault(bin_input, 0)  # !
                    weight[bin_input] += 1
            print(f'weight result:\n{weight}')

            # 构建霍夫曼树
            root = None
            huffman_tree_nodes = []
            for item in weight.items():
                huffman_tree_nodes.append(Node(item[0], item[1]))

            n = len(huffman_tree_nodes)
            for i in range(n-1):
                """解释下这里这个for循环的结束条件：
                len()得出的是叶子节点的数量，记作n，根据结构特性，
                生成的霍夫曼树总结点数量m=2n-1，所以循环条件以huffman_tree_nodes中子树数量达到m为边界,
                计算一下，则需要循环m-n次，即n-1次
                """
                # 排序以及获取待合并的两棵子树（两棵权重最小且没有父节点的子树）
                huffman_tree_nodes = sorted(huffman_tree_nodes, key=lambda x: x.weight)
                # print(f'tree size = {len(huffman_tree_nodes)}')
                to_be_merged = []
                for node in huffman_tree_nodes:
                    if len(to_be_merged) >= 2:
                        break
                    if node.parent is None:
                        to_be_merged.append(node)

                # 合并两棵子树
                merged_node = Node(None, to_be_merged[0].weight + to_be_merged[1].weight, None, to_be_merged[0], to_be_merged[1])
                to_be_merged[0].parent = to_be_merged[1].parent = merged_node
                huffman_tree_nodes.append(merged_node)
                # print(f'tree size = {len(huffman_tree_nodes)}')

            for node in huffman_tree_nodes:
                if node.parent is None:
                    root = node
                node.weight = 0

            # 计算霍夫曼编码（遍历霍夫曼树）
            cur = root
            code = ''
            """
            # # 朴素的二叉树先序遍历难以解决回溯时编码的收缩问题
            # # 设计解决，方案也很难看，留此备注，这段逻辑注释掉了
            # stack = []
            # while cur is not None or len(stack) > 0:
            #     if cur:  # 向左
            #         stack.append(cur)
            #         cur = cur.lch
            #         code += '0'
            #     else:  # 向右
            #         cur = stack.pop()
            #         code = code[:-1]
            #         if cur.info:
            #             huffman_code[cur.info] = code
            #         cur = cur.rch
            #         code += '1'
            #
            #     print(code)
            #     print(huffman_code)
            """

            # 利用额外字段Node.weight标记访问状态（~DFS ~refer严版数据结构）
            # 前面已经将所有节点的weight置为0了
            # 0=未访问，1=访问了左子树，2=左右子树均已访问
            while len(huffman_code) < n:
                if cur.weight == 0:
                    cur.weight = 1
                    if cur.lch:
                        cur = cur.lch
                        code += '0'
                    else:
                        huffman_code[cur.info] = code
                elif cur.weight == 1:
                    cur.weight = 2
                    if cur.rch:
                        cur = cur.rch
                        code = code + '1'
                else:
                    cur = cur.parent
                    code = code[:-1]
                # print(code)
                # print(huffman_code)
        init_huffman_code()
        print(f'huffman code:\n{huffman_code}')

        # 对源文件进行转码
        content_bin = ''
        with open(file_path, mode='rb') as f:
            for i in range(file_size):
                bytes_in = f.read(1)
                content_bin += huffman_code[bytes_in]
        # print(content_bin)
        print(f'binary content size = {len(content_bin)}')

        # 末尾补零凑足字节
        gap = 0 if len(content_bin) % 8 == 0 else 8 - len(content_bin) % 8
        content_bin += gap*'0'
        print(f'gap = {gap}')

        size = len(content_bin) // 8
        print(f'size after add gap zero = {len(content_bin)}')
        print(f'byte counts = {size}')

        # 存储压缩文件
        compressed_file_path = save_path+'.pwzip'
        with open(compressed_file_path, mode='wb') as f:
            # 写入补零信息
            f.write(six.int2byte(gap))
            # 写入正式内容
            for i in range(0, size):
                f.write(six.int2byte(int(content_bin[8 * i: 8 * i + 8], base=2)))
        print('compressed file saved successfully')

        # 存储霍夫曼编码
        huffman_code_file_path = compressed_file_path + '.huffman'
        with open(huffman_code_file_path, mode='wb') as f:
            # f.write(json.dumps(huffman_code))
            # json.dump(huffman_code, f)  # ERROR: keys must be str, int, float, bool or None, not bytes
            pickle.dump(huffman_code, f)
        print('huffman code file saved successfully')

        print('compress done.')
        print('-'*50 + '\nHuffmanCodingUtil.compress() <<<\n' + '-'*50)
        return True

    @staticmethod
    def decompress(file_path: str, code_path: str):
        print(f'decompressing... {file_path}')

        # 加载霍夫曼编码文件
        print(f'using code file... {code_path}')
        with open(code_path, 'rb') as f:
            huffman_code = pickle.load(f)
        print(f'load huffman code:\n{huffman_code}')

        # 编码文件kv转置方便执行解压解码
        huffman_reverse = {}
        for k, v in huffman_code.items():
            huffman_reverse[v] = k
        print(f'init huffman code:\n{huffman_reverse}')

        # 加载压缩文本
        size = os.path.getsize(file_path)
        content_decompress = b''
        with open(file_path, 'rb') as f:
            """
            temp = b'\x00'
            print(temp)
            print(str(temp)[4:-1])
            print(int(str(temp)[4:-1], 16))
            # b'\x00'
            # 00
            # 0
            """
            first_byte = f.read(1)
            gap = int(str(first_byte)[4:-1], base=16)
            print(f'gap zero counts: {gap}')
            for i in range(size-2):
                content_decompress += huffman_reverse[f.read(1)]
            # 处理最后的gap
            last_byte = f.read(1)
            last_byte = last_byte[0:8-gap]
            print(last_byte)
        return True


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
                                   command=lambda: path_input.set(askopenfilename(initialdir='.')))
        open_file_entry.grid(row=2, column=0)
        open_file_btn.grid(row=2, column=1)

        # 选择存储目录
        path_output = tk.StringVar()
        save_file_entry = ttk.Entry(func_frm, textvariable=path_output, width=60)
        save_file_btn = ttk.Button(func_frm, text='save to...', width=15,
                                   command=lambda: path_output.set(asksaveasfilename(initialdir='.')))
        save_file_entry.grid(row=3, column=0)
        save_file_btn.grid(row=3, column=1)

        # 分割线
        ttk.Separator(func_frm, orient=HORIZONTAL).grid(row=4, columnspan=2, sticky=EW, pady=15)

        # 选择字典文件
        path_dict = tk.StringVar()
        save_file_entry = ttk.Entry(func_frm, textvariable=path_dict, width=60)
        save_file_btn = ttk.Button(func_frm, text='select code...', width=15,
                                   command=lambda: path_dict.set(askopenfilename(initialdir='.')))
        save_file_entry.grid(row=5, column=0)
        save_file_btn.grid(row=5, column=1)

        # 分割线
        ttk.Separator(func_frm, orient=HORIZONTAL).grid(row=6, columnspan=2, sticky=EW, pady=15)

        # 压缩/解压缩按钮 ~及功能
        def compress_func_route():
            if path_dict.get() == '':
                print('start compressing...')
                try:
                    HuffmanCodingUtil.compress(path_input.get(), path_output.get())
                except Exception as e:
                    print('error............')
                    print(e)
            else:
                print('start decompressing...')
                try:
                    HuffmanCodingUtil.decompress(path_input.get(), path_dict.get())
                except Exception as e:
                    print('error............')
                    print(e)

        start_btn = ttk.Button(func_frm, text='Start to compress/decompress!', command=compress_func_route)
        start_btn.grid(row=7, columnspan=2, rowspan=5, sticky=EW, pady=5, padx=15)

    menu.add_command(label='General File Compressor', command=init_compressor)


if __name__ == '__main__':
    """unit test"""

    # 窗口
    win = tk.Tk()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    win.geometry(f'600x400+{(screen_width - 600) // 2}+{(screen_height - 400) // 2}')
    win.title('HuffmanCodeCompressor')
    frm = ttk.LabelFrame(win)
    frm.pack()

    # 菜单
    menubar = tk.Menu(win)
    win.config(menu=menubar)

    # 测试
    init_func_file_compressor(menubar, frm)

    win.mainloop()
