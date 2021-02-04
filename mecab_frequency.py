from konlpy.tag import Hannanum
from eunjeon import Mecab
hannanum = Hannanum()
mecab = Mecab() 
from collections import Counter


morphs = []

filepath = "./경로.확장자"
f = open(filepath,'r',encoding='utf-8')
lists = f.read()
y = mecab.nouns(lists)
# print(lists)

# 명사분리후 frequency 분석
count = Counter(y)
words = dict(count.most_common()) 
morphs.append(words)
print(morphs)

#frequency 분석후 다 찍어내기
f1 = open("./경로.확장자",'w',encoding='utf-8')
for morpy in morphs:
    f1.write(str(morpy))
    f1.write('\n')
f1.write(morphs)


