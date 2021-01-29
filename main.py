import re
from itertools import chain

from sudachipy import tokenizer
from sudachipy import dictionary


tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C

txt = """逃げ出したい夜の往来　行方は未だ不明
回り回って虚しくって　困っちゃったワンワンワン
失ったつもりもないが　何か足りない気分
ちょっと変にハイになって　吹かし込んだ四輪車""".replace(" ", " ")


x = re.split("\u3000|\n", txt)
# print(x)

tmp = []
for ls in x:
    tmp.append([(m.surface(), m.part_of_speech())
                for m in tokenizer_obj.tokenize(ls, mode)])


# for item in tmp:
#     for x in item:
#         print(x)

tmp = list(chain.from_iterable(tmp))

indices = [i for i, item in enumerate(tmp) if item[1][0] in (
    '名詞', '副詞', '代名詞', '動詞') and item[1][1] != '非自立可能']+[len(tmp)]
# print(indices)

x = 0
result = []
for i in indices:
    result.append(tmp[x:i])
    x = i

result = [''.join([txt[0] for txt in item]) for item in result][1:]
print(result)
