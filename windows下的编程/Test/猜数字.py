import random

target = random.randint(0, 100)
print(target)
print('请输入0～100之间的数,连续输入三次，如果三个数刚好都等于这个数将获得胜利,\n'
      '如果有一个,则输出有一个是对的,否则将进行判断,将以多的条件为准.')
value1, value2, value3 = 0, 0, 0
while True:

    while True:
        try:
            value1 = int(input('请输入你要猜的数字1：'))
        except ValueError as e:
            print('请输入int型数据')
        else:
            break

    while True:
        try:
            value2 = int(input('请输入你要猜的数字2：'))
        except ValueError as e:
            print('请输入int型数据')
        else:
            break

    while True:
        try:
            value3 = int(input('请输入你要猜的数字3：'))
        except ValueError as e:
            print('请输入int型数据')
        else:
            break

    if isinstance(value1, int) & isinstance(value2, int) & isinstance(value3, int):
        if value3 == value2 == value1 == target:
            break
        elif target in (value1, value2, value3):
            print('其中有一个数是对的.')
        else:
            hh = '小了' if (value1 < target, value2 < target, value3 < target).count(True) >= 2 else '大了'
            print(hh)
    else:
        print('请输入int型数据')

print('very good !')
