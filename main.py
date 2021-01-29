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
print(tmp)

# [('願っ', ['動詞', '非自立可能', '*', '*', '五段-ワア行', '連用形-促音便'])]
# item[1][0] は大分類．item[1][1] は小分類
indices = [i for i, item in enumerate(tmp) if item[1][0] in (
    '名詞', '副詞', '代名詞', '動詞')
    and item[1][1] != '非自立可能'
    and item[1][1] != '数詞']+[len(tmp)]

print(indices)

x = 0
result = []
for i in indices:
    result.append(tmp[x:i])
    x = i

result = ' '.join([''.join([txt[0] for txt in item]) for item in result][1:])
print(result)
