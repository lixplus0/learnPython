import re

def solve_title(_first_line):
    reg1 = '@[a-zA-Z]+{'
    line_title = re.match(reg1, _first_line).group()
    reg2 = '{.+?,'
    author_first = re.search(reg2, _first_line).group()[1:-1]
    year = _first_line.split('#')[-1].split('\\')[0]
    return line_title + author_first + year

def main():
    file_path = r"D:\Research\LxWork.txt"
    with open(file_path, 'r', encoding='UTF-8-sig') as data_file:
        for line in data_file.readlines():
            if line[0] == '@':
                print(solve_title(line))

if __name__ == '__main__':
    main()
