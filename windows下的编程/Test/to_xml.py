import re

title = ''
with open('python module', 'r+') as fp, open('python_module.xml', 'w') as ffp:
    ffp.writelines('<python>'+'\n')
    for j, i in enumerate(fp):
        print(1+j, i)

        if i.endswith('title\n'):
            if title != '':
                kk = '</modules'+'>'+'\n'
                ffp.writelines(kk)
            kk = '<modules title='+'\''+i[:-6]+'\''+'>'+'\n'
            ffp.writelines(kk)
            title = i
        elif re.findall("[A-Za-z1-9-]+，.+。\n", i):

            kk = '<'+i[:i.find('，')]+'>'+i[i.find('，')+1:-2]+'</'+i[:i.find('，')]+'>'+'\n'
            ffp.writelines(kk)

with open('python_module.xml', 'a') as ffp:
    kk = '</modules' + '>' + '\n'
    ffp.writelines(kk)
    ffp.writelines('</python>'+'\n')
