import pandas


fp = pandas.read_excel('./test2003.xls')
data = fp.head()
print(data)
