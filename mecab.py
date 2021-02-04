# Made by Mose Gu 'http://cpslab.skku.edu/people-Moses-Gu.php'
#this code is to extract nouns from text file

from konlpy.tag import Hannanum
from eunjeon import Mecab
hannanum = Hannanum()
mecab = Mecab() 


filepath = ("./경로.확장자") #directory of word or text file
f = open(filepath,'r',encoding='utf-8')
rd = f.read()
y = mecab.nouns(rd)
# print(rd)


f = open("./경로2.확장자",'w',encoding='utf-8') #save path
frequency = {}
for i in y:
    print(i)


f.writelines(str(y)) #메모장에 콘엘피와이 단어다찍어내기
print(str(y))


