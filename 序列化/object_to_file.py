# import json
# import pickle
# import struct
# import shelve
#

# import json

# json_date = {'1': 'good', '2': 'day'}
# a = json.dumps(json_date)
# print(a)
# # dict 类型
# print(type(json.loads(a)))
#
# with open('./file/json.txt', 'w') as fp:
#     json.dump(json_date, fp)
#
# with open('./file/json.txt', 'r') as fp:
#     print(json.load(fp))

# import pickle
# a, b, c, d, e = 'str', 1, ['dd'], {'k': 'value'}, (1,)
# pickle_dates = [a, b, c, d, e]
#
# with open('./file/pickle.txt', 'wb') as fp:
#     try:
#         # protocol=Ture 可以压缩
#         pickle.dump(len(pickle_dates), fp, protocol=True)
#         for pickle_date in pickle_dates:
#             pickle.dump(pickle_date, fp)
#     except :
#         print('pickle 异常')
#
# with open('./file/pickle.txt', 'rb') as fp:
#     n = pickle.load(fp)
#     for i in range(n):
#         x = pickle.load(fp)
#         print(x)
#
# # import struct
# # 麻烦，不使用，不好用
# struct_date1, struct_date2 = 1, 'string'
# sn = struct.pack('i', struct_date1)
# with open('./file/struct.txt', 'wb') as fp:
#     fp.write(sn)
#     fp.write(struct_date2.encode('utf-8'))
#
# with open('./file/struct.txt', 'rb') as fp:
#     sn = fp.read(4)
#     tu = struct.unpack('i', sn)
#     struct_date1 = tu
#     print(struct_date1)
#     s = fp.read().decode('utf-8')
#     print(s)
#
# import shelve
# # 像字典一样赋值
# a_list = {'k': 'v', 'good': 'day'}
# b_list = {'k': 'v', 'good': 'day'}
#
# # 不要先建立文件，自己会建立，如果先建立会报错
# with shelve.open('./file/shelve.dat') as fp:
#     fp['a_list'] = a_list
#     fp['b_list'] = b_list
#
# with shelve.open('./file/shelve.dat') as fp:
#     print(fp['a_list'])
#     print(fp['b_list']['k'])
