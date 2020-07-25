from collections import Counter
import pprint

alist = ['asd', 'bb', 'cc', 'a', 'bb', 'ff', 'kk', 'ff', 'asd', 'asd', 'asd', 'bb']
c = Counter(alist)
print(c)
try:
    print(c.pop('bb'))
except KeyError as e:
    print(e.args, '5')
else:
    print(c)
finally:
    pprint.pprint(c)


# set(ls.most_common(10))-set(ls.most_common(8))
