import pandas as pd
import re

def match(source,target):
    tag = []
    for ch in target:
        if ch in source:
            tag.append(ch)
    if len(tag) < 3:
        return None
    else:
        return ''.join(tag)

# 词频统计
def word_count(string,n):
    # 匹配两个汉字及以上
    z = re.compile('[\u4E00-\u9FA5]{'+n+'}')
    i = z.findall(string)
    dict = {}
    for j in i:
        if (j in dict):
            dict[j] += 1
        else:
            dict[j] = 1
    print(dict)
    print(len(dict))
    return dict

# 将list拼接成字符串
def concat_string(obj):
    res = []
    for t in obj:
        res.append(filter(t))
    return '|'.join(res)

# 对dict排序,截取(x,y) y > n的部分
def sort_sub(dict,n=3):
    sl = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    # print(sl)
    return [x[0] for x in sl if x[1] >= n]

def filter(string):
    pattern = re.compile(r'[0-9 \-()\[\]《》\.、【】·（）]')
    return re.sub(pattern,'',string)

if __name__ == '__main__':
    file_path = 'C:/Users/Administrator/Desktop/album_name.txt'
    data = pd.read_table(file_path,header=None,names=['name'])
    data['tag'] = None
    # print(data)

    # print(data['name'].str.split(n=-1,expand=True))

    # print(data.groupby('name').size())

    # print(data['name'][:3])

    # for n in data['name'][:10]:
    #     print(n)

    # print(match('碧血剑 金庸 华山聚会 芦伶 俞皋 施素 殷红 药召 穆声','碧血剑之三 金蛇郎君'))


    # print('|'.join(res))
    #
    # di = word_count('|'.join(res),str(2))
    # print(sort_sub(di))

    source = concat_string(data['name'][:21])

    print(source)
    tag = []
    base = sort_sub(word_count(source,str(2)),2)
    print(base)
    print(len(base))
    for n in range(3,8):
        tmp = sort_sub(word_count(source,str(n)))
        for i,x in enumerate(base):
            for y in tmp:
                if x in y:
                    base[i] = y

    print(base)
    print(list(set(base)))
    print(len(list(set(base))))
    # print([v for v in sorted(di.values(),reverse=True)])
    # sl = sorted(di.items(), key=lambda item: item[1], reverse=True)
    # print(sl)
    # print(len(sl))
    # fl = [x for x in sl if x[1] > 2]
    # print(fl)
    # print(len(fl))


    # 2-10 递归


    # num = 201
    # res = {}
    # ptag = []
    # for i,outer in data['name'][:num].items():
    #     is_match = False
    #     for inner in data['name'][i+1:num]:
    #         tag = match(filter(inner),filter(outer))
    #         if tag:
    #             ptag.append(tag)
    #             is_match = True
    #             continue
    #     if not is_match:
    #         pass
    #
    # ptag = list(set(ptag))
    # print(ptag)


    # for index, name in data['name'][:num].items():
    #     stag = data.loc[index,'tag']
    #     for tag in ptag:
    #         if stag:
    #
    #             pass
    #         else:
    #             if tag in filter(name):
    #                 stag = tag
    #     data.loc[index, 'tag'] = stag
    #
    # print(data.fillna(value={'tag':'未分类'}))
    # # print(data[:num])
    # print(data.groupby('tag').sum())

    pass