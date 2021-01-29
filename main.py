import re
from itertools import chain

from sudachipy import tokenizer
from sudachipy import dictionary


tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C


txt = ''
with open('./input.txt') as f:
    txt = f.read()
    # print(txt)

x = re.split("\u3000|\n", txt)
tmp = []
for ls in x:
    tmp.append([(m.surface(), m.part_of_speech())
                for m in tokenizer_obj.tokenize(ls, mode)])

tmp = list(chain.from_iterable(tmp))
# print(tmp)
# for item in tmp:
#     print(item)

indices = [i+1 for i, item in enumerate(tmp)
           if (item[1][0] in ['補助記号'])
           or (item[1][1] in ['格助詞'] and tmp[min(i+1, len(tmp)-1)][1][0] not in ['補助記号'])]
indices = [0] + indices + [len(tmp)]

# print(indices)

delete_indices = [i for i, item in enumerate(tmp)
                  if item[1][0] in ['形状詞']]

# print(delete_indices)

for item in delete_indices:
    try:
        indices.remove(item)
    except:
        # ('に', ['助詞', '格助詞', '*', '*', '*', '*'])
        # ('も', ['助詞', '係助詞', '*', '*', '*', '*'])
        try:
            indices.remove(item-1)
        except:
            pass
        indices.append(item)
indices = sorted(indices)

# print(indices)

x = 0
result = []
for i in indices:
    result.append(tmp[x:i])
    x = i

result = ' '.join([''.join([txt[0] for txt in item]) for item in result][1:])
# result = re.sub(r"", " ", result)
print(result)
# print(len(result.split()))
