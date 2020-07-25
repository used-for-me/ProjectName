import subprocess as sub


# def func():
#     print('this is func')
#
#
# # 计数功能
# def hh():
#     a = 0
#     while True:
#         yield a
#         a = a + 1
#
#
# ls_out = sub.Popen(['ls'], stdout=sub.PIPE)
# # preexec_fn 调用函数
# ls_in = sub.Popen(['python3', 'inpipe.py'], stdin=ls_out.stdout, stdout=sub.PIPE, preexec_fn=func)
# A = hh()
# while True:
#     # 另一个程序的输出,如文件一般
#     s = ls_in.stdout.readline()
#     if s is not None and s != b'':
#         print(s)
#     aa = next(A)
#     if aa < 10:
#         print(aa)
#     else:
#         break
ls = sub.Popen(['who'])
print(ls)
