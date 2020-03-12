import os


# 转换文件格式和编码方式
def to_lf(path, isLF, encoding='utf-8'):
    """
    :param path: 文件路径
    :param isLF: True 转为Unix(LF)  False 转为Windows(CRLF)
    :param encoding: 编码方式，默认utf-8
    :return:
    """
    newline = '\n' if isLF else '\r\n'
    tp = 'Unix(LF)' if isLF else 'Windows(CRLF)'
    with open(path, newline=None, encoding=encoding) as infile:
        str = infile.readlines()
        with open(path, 'w', newline=newline, encoding=encoding) as outfile:
            outfile.writelines(str)
            print("文件转换成功，格式：{0} ;编码：{1} ;路径：{2}".format(tp, encoding, path))


if __name__ == "__main__":
    rootdir = 'D:\\code\\markdown\\*.*'
    isLF = True  # True 转为Unix(LF)  False 转为Windows(CRLF)
    path_list = os.listdir(rootdir)
    # path_list.sort(key=lambda x:int(x[:-4])) #对读取的路径进行排序
    for filename in path_list:
        path = os.path.join(rootdir, filename)
        to_lf(path, isLF)
