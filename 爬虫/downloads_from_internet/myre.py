import re



# aa = re.findall(r'<a.*>[\n.]?\s*(第.*章.+\([0-9]{0,3}\))+\s*</a>', open('bb.txt', 'r').read())
# print(aa)
# while True:
#     aa = input('string=')
#     bb = re.findall(r'^(?=.*[a-z])^(?=.*[A-Z])^(?=.*\d)(?=.*[,._]).{8,}$', aa)
#     print(bb)
# cc = re.findall(r'(?!.*w]*)((?P<a>.)(?P=a)(?P<b>.)(?P=b))', open('bb.txt', 'r').read())
# print(cc)
# cc = re.findall(r'((.)(.)\2\3)', open('bb.txt', 'r').read())
# print(cc)
# dd = re.findall(r'(((http[s]?://)|(www\.))\w+(\.\w+)*(/\w+)*)', open('bb.txt', 'r').read())
# for i in dd:
#     print(i[0])
re.findall(r"\.{0,3}/\w", '')

