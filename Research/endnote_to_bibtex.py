# -*- coding: utf-8 -*-
"""
    本程序用于将EndNote导出的bibtex转化为'authoryear'的格式
    在EndNote导出时，一定要选择BibTeX Export-PythonData
"""
import os
import re

def solve_title(_first_line):
    reg1 = '@[a-zA-Z]+{'
    line_title = re.match(reg1, _first_line).group()
    reg2 = '{.+?,'    # ?非贪婪
    author_first = re.search(reg2, _first_line).group()[1:-1]
    year = _first_line.split('#')[-1]
    return line_title + author_first + year

def to_file(_line, _new_file):
    """字符串行写入文件"""
    with open(_new_file, 'a', encoding='utf-8') as new_file:
        new_file.write(_line)


def main():
    file_path = r"D:\Research\LxWork.txt"
    new_file = os.path.splitext(file_path)[0] + '.bib'
    if os.path.exists(new_file):
        os.remove(new_file)

    with open(file_path, 'r', encoding='UTF-8-sig') as data_file:    # Endnote默认导出的文本是utf8 bom格式
        for line in data_file.readlines():
            if line[0] == '@':
                new_line = solve_title(line)
            else:
                new_line = line
            to_file(new_line, new_file)

if __name__ == '__main__':
    main()
