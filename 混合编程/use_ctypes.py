import platform
# from ctypes import CDLL
from ctypes import cdll
from ctypes import c_float

libc = None
libc1 = None
if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')

elif platform.system() == 'Linux':
    # libc.so.6 相当与stdio.h
    libc = cdll.LoadLibrary('libc.so.6')
    # 本地so文件
    libc1 = cdll.LoadLibrary('./my.so')
# 第二种形式
# libc = CDLL('libc.so.6')

# 编码形式很重要
# string = "Hello World!\n"        # 定义一个字符串
# string = string.encode("utf-8")
# libc.printf("ff".encode("utf-8"))


# int类型可以直接使用
# print(libc1.add_int(4, 2))

# float类型需要转换
# add_float = libc1.add_float
# add_float.restype = c_float
# print(add_float(c_float(5), c_float(5)))

